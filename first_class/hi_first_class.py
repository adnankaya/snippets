def h1(text):
    return f"<h1>{text}</h1>"


def h2(text):
    return f"<h2>{text}</h2>"


def print_header(func, text):
    return func(text)


print(print_header(h1, "title1"))
print(print_header(h2, "title2"))


def f1(param):
    def f2():
        print(param)
        return
    return f2


f = f1("selam f1")
print("type of f : ",type(f))
print("name of f: ",f.__name__)
f()