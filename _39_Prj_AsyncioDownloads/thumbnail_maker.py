# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
import multiprocessing
import asyncio
import aiohttp
import aiofiles

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.INFO, force=True, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = multiprocessing.JoinableQueue()
        self.dl_size = multiprocessing.Value('i', 0)       # Size of all images downloaded
        self.resized_size = multiprocessing.Value('i', 0)  # Size of all generated/resized images
        self.dl_size_lock = multiprocessing.Lock()  # Lock for updating download size

    async def download_image_coro(self, session, url, dl_size_lock):
        img_filename = urlparse(url).path.split('/')[-1]
        img_filepath = self.input_dir + os.path.sep + img_filename

        try:
            async with session.get(url) as response:
                async with aiofiles.open(img_filepath, mode='wb') as f:
                    content = await response.content.read()
                    await f.write(content)
            with dl_size_lock:
                self.dl_size.value += os.path.getsize(img_filepath)
            self.img_queue.put(img_filename)
            logging.info(f"downloaded {img_filename}")
        except Exception as e:
            logging.error(f"error downloading {url}: {e}")

    async def download_images_coro(self, img_url_list, dl_size_lock):
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_image_coro(session, url, dl_size_lock) for url in img_url_list]
            await asyncio.gather(*tasks)

    def download_images(self, img_url_list):
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)
        logging.info("beginning image downloads")
        start = time.perf_counter()
        asyncio.run(self.download_images_coro(img_url_list, self.dl_size_lock))
        end = time.perf_counter()
        logging.info(f"downloaded {len(img_url_list)} images in {end - start} seconds")

    def perform_resizing(self):
        os.makedirs(self.output_dir, exist_ok=True)
        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]

        while True:
            start = time.perf_counter()
            filename = self.img_queue.get()
            if filename is None:
                self.img_queue.task_done()
                break

            try:
                orig_img = Image.open(os.path.join(self.input_dir, filename))
                totalSizeThumbnails = 0
                for basewidth in target_sizes:
                    img = orig_img
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((basewidth, hsize), Image.LANCZOS)
                    new_filename = os.path.splitext(filename)[0] + '_' + str(basewidth) + os.path.splitext(filename)[1]
                    out_filepath = os.path.join(self.output_dir, new_filename)
                    img.save(out_filepath)
                    totalSizeThumbnails += os.path.getsize(out_filepath)
                with self.resized_size.get_lock():
                    self.resized_size.value += totalSizeThumbnails
                os.remove(os.path.join(self.input_dir, filename))
                end = time.perf_counter()
                logging.info(f"reduced '{filename}' to thumbnails of size '{totalSizeThumbnails}' in {end - start} seconds")
            except Exception as e:
                logging.error(f"error resizing {filename}: {e}")
            finally:
                self.img_queue.task_done()

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        num_processes = multiprocessing.cpu_count()
        processes = []
        for _ in range(num_processes):
            p = multiprocessing.Process(target=self.perform_resizing)
            p.start()
            processes.append(p)

        self.download_images(img_url_list)

        for _ in range(num_processes):
            self.img_queue.put(None)

        for p in processes:
            p.join()

        end = time.perf_counter()
        logging.info(f"END make_thumbnails in {end - start} seconds")
        logging.info(f"Initial size of downloads: [{self.dl_size.value}], Final size of images: [{self.resized_size.value}]")

