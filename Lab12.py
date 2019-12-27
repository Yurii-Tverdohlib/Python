import os
import hashlib
import threading


class Duplicate:
    blockSize = 512

    def DuplicateFind(self):
        path = "B://"
        listOfFolders = self.FindFolders(path)
        threads = []
        for i in range(listOfFolders.__len__()):
            thread = threading.Thread(target=self.FindDuplicatesInFolder(listOfFolders[i]))
            threads.append(thread)
            thread.start()
        for i in threads:
            i.join()

    def FindDuplicatesInFolder(self, path):
        hashes = {}
        for root, directories, files in os.walk(path):
            for name in files:
                self.path = os.path.join(root, name)
                filehash = self.HashFileWithMd5(self.path)
                hashes[filehash].append(self.path)
        duplicate_files = []
        for k, v in hashes.items():
            if list(hashes.values()).count(v) > 1:
                duplicate_files.append(k)

    def HashFileWithMd5(self, path):
            with open(path, 'rb') as file:
                md5_hash = hashlib.md5()
                chunk = file.read(self.blockSize)
                while chunk:
                    md5_hash.update(chunk)
                    chunk = file.read(self.blockSize)
                    return md5_hash.hexdigest()

    def FindFolders(self, path):
        folders = []
        for r, d, f in os.walk(path):
            for folder in d:
                folders.append(os.path.join(r, folder))
        return folders


if __name__ == '__main__':
    a = Duplicate()
