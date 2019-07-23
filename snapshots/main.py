import multiprocessing as mp
import time
import urllib.request


def download(url: str, destination: str):
    urllib.request.urlretrieve(url, destination)

n = 15
fps = 12.0
left_port = 8080
right_port = 8081
wait_time = 1.0 / fps


for i in range(0, n):
    pool = mp.Pool()
    pool.starmap(download, [
        (f"http://192.168.0.116:{left_port}/?action=snapshot", f"/output/left_{i}.jpg"),
        (f"http://192.168.0.116:{right_port}/?action=snapshot", f"/output/right_{i}.jpg")
    ])
    time.sleep(wait_time)
