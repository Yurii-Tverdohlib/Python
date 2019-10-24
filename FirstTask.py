from pip._vendor.msgpack.fallback import xrange


def kseroks(lineika):
    print(lineika)


def random_list():
    import random

    list= random.sample(xrange(100), 10)

    list_sum = sum(list)

    average = list_sum / len(list)

    kseroks('{} {} {}'.format(list, list_sum, average))


def main():
    random_list()


if __name__ == '__main__':
    main()