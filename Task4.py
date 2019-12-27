def Wraps(RL):
    def Wrapper(YT):
        YT.__name__ = RL.__name__
        YT.__doc__ = RL.__doc__
        return YT
    return Wrapper
def Wrapper(wrap):
    @Wraps(wrap)
    def wrapper(a):
        wrap(a)
    return wrapper
@Wrapper
def Lab3(a):
    pass
print(Lab3.__name__)
print(Lab3.__doc__)
