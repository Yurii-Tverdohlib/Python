def fileDownloader(url):
    from urllib.request import urlopen
    response = urlopen(url)
    fileToGet = response.read()
    fileToGet.decode('UTF-8')
    extractedFile = str(fileToGet)
    reformattedFile = extractedFile.split('\\n')
    fileToSave = open('file.txt', 'a')
    fileToSave.writelines(reformattedFile)
    fileToSave.close()
    return fileToSave.name


def lineConverter(fileName):
    with open(fileName) as fileToConvert:
        for line in fileToConvert:
            line = str(line).split(' ').strip('\\n')
            yield line


def wordCounter(func, fileName):
    count = 0
    for line in func(fileName):
        count += len(line)
    return count


def wordStatsCounter(func, fileName):
    count = {}
    for line in func(fileName):
        for i in line:
            if count.__contains__(i):
                count[i] += 1
            else:
                count[i] = 1
                break
    return count
