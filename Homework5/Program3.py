import time
start =time.time()
def make_adder(x):
   
    def add(y):
        return x+y
    return add
    end=time.time()
    print(end-start)
add3 = make_adder(3)
print(add3(4))
end=time.time()
print(end-start)