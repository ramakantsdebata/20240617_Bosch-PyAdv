# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
from queue import Queue
from threading import Thread

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s]"
logging.basicConfig(filename='logfile.log', level=logging.INFO, force=True, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = Queue()
        self.url_queue = Queue()


    def download_image(self):
        os.makedirs(self.input_dir, exist_ok=True)
        
        logging.info("beginning image downloads")

        start = time.perf_counter()
        while not self.url_queue.empty():
            try:
                # Need to guard again while getting, as another thread might 
                # have extrated the last url between the last 'empty' check 
                # and the 'get' attempt on next line.
                
                url = self.url_queue.get(block=False)
                
                # As we know that the url_queue will NOT be re-populated after 
                # all urls are extracted, we can unblock and terminate the thread.
                # (block = False) configures the get to be non-blocking (don't 
                # wait for next item to appear in the queue), and throw an 
                # exception 'Queue.Empty'.

                # download each image and save to the input dir 
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                logging.info("downloaded - {}".format(img_filename))
                self.img_queue.put(img_filename)
                self.url_queue.task_done()
            except Queue.Empty:
                logging.info("URL queue EMPTY !")
        end = time.perf_counter()

    def perform_resizing(self):
        # ensure output folder is in place
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        while True:
            filename = self.img_queue.get()
            if filename is None:
                self.img_queue.task_done()
                break

            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                
                # save the resized image to the output dir with a modified file name 
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
            logging.info("done resizing image {}".format(filename))
            self.img_queue.task_done()
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        for url in img_url_list:
            self.url_queue.put(url)

        # Creating a pool of 4 threads and starting those
        num_dl_threads = 4
        for idx in range(num_dl_threads):
            t1 = Thread(target=self.download_image, name=f"t_Dwnld[{idx}]")
            t1.start()

        t2 = Thread(target=self.perform_resizing, name="t_Resize")
        t2.start()

        # Block the main thread till all the urls 
        # are picked off by the download threads
        self.url_queue.join() 
        # This is why url_queue.task done was done 
        # after the actual download finished, so as
        # to avoid a pre-mature poisoning

        # Now, send the poison pill to the img_queue 
        # for the resize thread to terminate
        self.img_queue.put(None)

        t2.join()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))

