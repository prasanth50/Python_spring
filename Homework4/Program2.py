def count_frequency(mylist):
    frequent = {}
    for i in mylist:
        if(i in frequent):
            frequent[i] += 1
        else:
            frequent[i] = 1
    return frequent
mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))
