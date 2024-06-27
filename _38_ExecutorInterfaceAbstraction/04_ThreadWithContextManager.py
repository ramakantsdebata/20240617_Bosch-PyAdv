from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

def load_url(url, time_out):
    with urlopen(url, timeout=time_out) as conn:
        return conn.read()

with ThreadPoolExecutor(max_workers=2) as executor:
    # Valid URL
    url1 = "http://www.google.com/"
    # Invalid URL
    url2 = "http://www.random-url.com/"
    
    f1 = executor.submit(load_url, url1, 60)
    f2 = executor.submit(load_url, url2, 60)
    
    try:
        data1 = f1.result()
        print(f"'{url1}' page is {len(data1)} bytes")
    except Exception as ex:
        print(f"Exception downloading page {url1}: {str(ex)}")
    
    try:
        data2 = f2.result()
        print(f"'{url2}' page is {len(data2)} bytes")
    except Exception as ex:
        print(f"Exception downloading page {url2}: {str(ex)}")
