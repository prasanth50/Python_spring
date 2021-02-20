import hashlib
long_url = input('Enter the url to shorten:')

def url_shortner(newurl):

    result = hashlib.md5(newurl.encode())
    x = result.hexdigest()
    z = list(x)
    return "".join(z[:7])

y = url_shortner(url_shortner)
print('The shorten url is \n https://bit.ly/' + y)
url_shortner = input("Enter the url to find original:") 

def get_original_url(m,n):
    newresult = hashlib.md5(n.encode())
    x = newresult.hexdigest()
    z = list(x)
    k = 'https://bit.ly' + ''.join(z[:7])
    if k==m:
        return n
    else:
        return "404 not found"

print(get_original_url(shorten_url,long_url))            

''' In this program I used Pyshortners module to make the given URL short
Pros: It is easy and convenient as we are using a module that has all the pre-defined functions enclosed in it.
Cons: Since the module is imported it has some limitations.
'''