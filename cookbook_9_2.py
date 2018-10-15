import time
from functools import wraps
from inspect import signature


def timethis(func):
    '''
    Decorator that reports the executionn time
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
    	start = time.time()
    	ret = func(*args, **kwargs)
    	end = time.time()
    	print(ret, end - start)
    	return ret

    return wrapper


@timethis
def countdown(n):
	while n > 0:
		n -= 1


if __name__ == '__main__':
    print(123)
    func = countdown(10000)
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)
    print(signature(countdown))
