from pip._vendor.msgpack.fallback import xrange


def outputer(txt):
    print(txt)


def random_list():
    import random

    list= random.sample(xrange(100), 10)

    list_sum = sum(list)

    average = list_sum / len(list)

    outputer('{} {} {}'.format(list, list_sum, average))


def main():
    random_list()


if __name__ == '__main__':
    main()
