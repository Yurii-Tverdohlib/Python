from urllib.request import urlopen


def fileDownload(httpUrl):
    response = urlopen(httpUrl)
    reddenFile = response.read()
    toText = str(reddenFile)
    splittedData = toText.split('\\n')
    data = open('text.txt', 'w')
    data.writelines(splittedData)
    data.close()
    return data.name


def SplitFile(name):
    with open(name) as file:
        for line in file:
            line = str(line).lower().strip('\n').split(' ')
            yield line


def CountWords(generator, name):
    countOfWord = 0
    for line in generator(name):
        countOfWord += len(line)
    return countOfWord


def GetWordStats(generator, fileName):
    lib = dict()
    for line in generator(fileName):
        for iterator in line:
            if not iterator in lib:
                lib[iterator] = 1
            else:
                lib[iterator] += 1
    return lib


def RunTest():
    urlName = input().decode('UTF-8')
    file = fileDownload(urlName)
    CountWords(SplitFile, file)
    GetWordStats(SplitFile, file)


if __name__ == '__main__':
    RunTest()
