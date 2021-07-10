#######################################################################################################################
#                                                          LIST

'''
# they are stored in []
#list are similar to the tuples but the only difference between them is that tuples are immutble and List are mutable.
#rest all features are same.

L=[1,2,[3,4,5],6,"hard rock"]
# here indexing is started from 0 and according to above list its upto 4 not 5 this list's length is 5.
# list are mutable it could be conformed by performing various operations on them.

#1.EXTEND LIST-
L.extend(['hi1','hi2'])
print(L)    # output is -[1, 2, [3, 4, 5], 6, 'hard rock', 'hi1', 'hi2']

#2.APPEND LIST-
L.append(['hello','pratham'])
print(L)     # output is -[1, 2, [3, 4, 5], 6, 'hard rock', 'hi1', 'hi2', ['hello', 'pratham']]

#NOTE -->
#here we must note that append and extend are not same.
#Append adds all the elements wanted into list directly but append make them in form of a single unit/list and then add them.

#3. CHANGING LIST-
L[0]=100
print(L)       #output is -[100, 2, [3, 4, 5], 6, 'hard rock', 'hi1', 'hi2', ['hello', 'pratham']]

#4. DELEATING ITEMS FROM LIST-
del(L[0])
print(L)      #output-[2, [3, 4, 5], 6, 'hard rock', 'hi1', 'hi2', ['hello', 'pratham']]     
print(L[0])   #output-2

#5. SPLIT THE LIST-
#NOTE--> here in the list we have the Item "hard rock" now we will break it intoo two segments or items.
# Also it will not affect the  orignal list. 
print("hard rock".split())   #output-['hard', 'rock']
print(L)                     # output-[2, [3, 4, 5], 6, 'hard rock', 'hi1', 'hi2', ['hello', 'pratham']]     

#6. SPLIT USING DILAMETERS-
l=[1,2,3,"a,b,c"]
#NOTE --> here as we can see that in our list we have a string having , in b/w its elements hence now this , would be used as the dilameters.
# and this wont affect the orignal list.
print("a,b,c".split(","))   #output-['a', 'b', 'c']
print(l)                    # output -[1, 2, 3, 'a,b,c'] 

#7.ALIASING(LIST ARE MUTABLE)-
#NOTE -->here as l1 and l2 refer to the same list this is called Aliasing.
# Also as list are MUTABLE they can have same refrance and be changed also.
# Change in one will change other too as the refrance is the same.
l1=[1,2,3,4,5,6]
l2=l1
l2[0]=100
print(l2)      #output-[100, 2, 3, 4, 5, 6]
print(l1)      #output-[100, 2, 3, 4, 5, 6]

#8.CLONING LIST-
#NOTE --> in cloning we make the copy of the values present at the refrance. 
# So if we make changes at l1 it wont affect l2.
l1=[1,2,3,4,5,6]
l2=l1[:]
l2[0]=100
print(l2)      #output-[100, 2, 3, 4, 5, 6]
print(l1)      #output-[1, 2, 3, 4, 5, 6]
'''
#######################################################################################################################
