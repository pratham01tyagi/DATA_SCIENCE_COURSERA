#######################################################################################################################
#                                              DIRECTORIES

'''
#They are similar to list but the only difference is that they hold key and values instead of index and element
#KEYS- they are unique values which could be of any data type and also they are Immutable.
#VALUES- they are similar to elements of lists which hold the information also they could be mutable , immutable & dublicate too.
# directories are stored in the {}.

D={"k1":1,"k2":"hi","k3":[3,3,3],'k4':(1,1,1),"k5":5}

#1.to print all the  keys in table- 
print(D.values())       #output-dict_keys(['k1', 'k2', 'k3', 'k4', 'k5'])

#2.to print all the values in table-
print(D.values())     #output-dict_values([1, 'hi', [3, 3, 3], (1, 1, 1), 5])

#3.here we get the values with the help of keys.
print(D['k4'])        #output-(1, 1, 1)

#4. adding a new key and value-
D["k6"]= 2007
print(D.keys())        #output-dict_keys(['k1', 'k2', 'k3', 'k4', 'k5', 'k6'])
print(D.values())      #output-dict_values([1, 'hi', [3, 3, 3], (1, 1, 1), 5, 2007])

#5.deleating te key and its value-
del(D["k6"])
print(D.keys())        #output-dict_keys(['k1', 'k2', 'k3', 'k4', 'k5'])
print(D.values())      #output-dict_values([1, 'hi', [3, 3, 3], (1, 1, 1), 5])

#6checking if key exist using in command-
print("k6"in D)        #output-False
print("k5"in D)        #output-True
'''
#######################################################################################################################