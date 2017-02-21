# File: func.py


class MyError(Exception):
    """
    This class represents my own Exception.
    """
    pass


def myexcept_raise_func():
    """
    This function raises a MyError.
    """
    raise MyError()


def raise_func():
    """
    This function raises a KeyError.
    """
    raise KeyError
    raise IndexError


def except_func():
    """
    This function catches all Exeptions which were mentioned in the problem.
    """
    try:
        raise_func()
    except KeyError as keyError_data:
        print("Caught a KeyError with a following data:")
        print(keyError_data)
    except IndexError as indexError_data:
        print("Caught an IndexError with a following data:")
        print(indexError_data)
    except MyError as myError_data:
        print("Caught a MyError with a following data:")
        print(myError_data)
    except:
        print("Caught an unknown error")
    finally:
        print("Catching finished")


except_func()
