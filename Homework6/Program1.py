import os
path = input('Enter the path:')
while True:
    print(os.path.exists(path))