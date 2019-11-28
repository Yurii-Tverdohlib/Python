import os
from urllib import request
from threading import Thread


class DownloadFiles(Thread):
    def __init__(self, url, number):
        Thread.__init__(self)
        self.number = number
        self.url = url

    def run(self):
        fileRequestOpen = request.urlopen(self.url)
        Nameoffile = os.path.basename(self.url)
        Size = 1024 * 2
        with open(Nameoffile, "wb") as handler:
            while True:
                fileInfo = fileRequestOpen.read(Size)
                if not fileInfo:
                    break
                handler.write(fileInfo)
        print(f"Thread {self.number} finished to download {self.url}")


if __name__ == "__main__":
    print("Type your url to download file: ")
    urls = input()
    potik1 = DownloadFilesWithUrl(urls, 1)
    potik1.start()
    potik2 = DownloadFilesWithUrl(urls, 2)
    potik2.start()