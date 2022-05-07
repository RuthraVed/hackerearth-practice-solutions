from time import time

# Defining a decorator to time execution of any fucntion
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'In {(t2-t1):.4f}s ', end="")
        return result
    return wrap_func
