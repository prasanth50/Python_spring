import shelve
db = shelve.open('/user/prasa/Python_spring/Homework6/','c')
db['bob'] = {'shoesize':42, 'gender':'m'}
db['bob']
{'shoesize': 42, 'gender': 'm'}
db['bob']['gender'] = 'u'
db['bob']
{'shoesize': 42, 'gender': 'm'}
db['bob'] = {'shoesize': 42, 'gender': 'u'}
db['bob']
{'shoesize': 42, 'gender': 'u'}