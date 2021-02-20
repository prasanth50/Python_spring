import pyshorteners
try:
    link = input('Enter the url :')
    shortner = pyshorteners.Shortener()
    x = shortner.tinyurl.short(link)
    print(x)

except:
    print("HTTP 404")    

''' In this program I used Pyshortners module to make the given URL short
Pros: It is easy and convenient as we are using a module that has all the pre-defined functions enclosed in it.
Cons: Since the module is imported it has some limitations.
'''
