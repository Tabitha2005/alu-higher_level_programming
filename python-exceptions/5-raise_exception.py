#!/usr/bin/python3
def raise_exception():
    raise TypeError("This is a custom type exception")

if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as e:
        print("Exception caught: ", e)
