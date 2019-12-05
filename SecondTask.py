def htmlDecorator(function):
    def wrapper(string):
        func = function(string)

        make_replace = func.replace('&', '&amp').replace('"', '&quot').replace('<', '&lt').replace('>', '&gt')

        return make_replace

    return wrapper


@htmlDecorator
def decorate(some_text):
    return some_text


def main():
    some_text = input()
    print(decorate(some_text))


if __name__ == '__main__':
    main()