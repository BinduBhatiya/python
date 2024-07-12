# unpack tuples :
# Unpacking is the process of assigning the tuple items as values to variables.

info = ('Bindu',21,'DSU') 
(name, age, university) = info
print('name : ',name)                                   # name :  Bindu
print('age : ',age)                                     # age :  21
print('university: ',university)                        # university:  DSU

# but what if we have more number of item then the variables ?
info = ('elephat','cat','horse','dove','salmon')
(*animals,birds,fish) = info
print('animals : ',animals)                             # animals :  ['elephat', 'cat', 'horse']
print('birds : ',birds)                                 # birds :  dove
print('fish : ',fish)                                   # fish :  salmon
