string = input()
html_tag = input()


def decoratorHtml(html_tag):
    def decorator(function):
        def wrapper(n1):
            return "<" + html_tag + ">" + function(n1) + "<" + html_tag + "/>"

        return wrapper

    return decorator


@decoratorHtml(html_tag)
def decorate(string):
    return string


def main():
    print(decorate(string))


if __name__ == '__main__':
    main()