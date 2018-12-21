import functools


def make_pretty(func):
    print('mayur')
    @functools.wraps(func)	
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
    
#ordinary()

#ordinary = make_pretty(ordinary)	
#ordinary()


#print(ordinary.__name__)
