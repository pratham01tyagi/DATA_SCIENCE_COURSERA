#######################################################################################################################
#                                               SETS
'''
#NOTE-->they are also type of collections like list and tuples
#but unlike list and tuples they are unordered this means that sets do not record element position.
#also they have unique elemenets no element is repeating there.
# we use {} to store them.

S={1,2,3,'a','b','c'} 

#1. CONVERTING A LIST TO A SET-
l=[1,2,2,3,4,'a','a','s']
#NOTE--> as here we see that l has repeating elements now we will convert it to a set where we dont have any repeating element.
S1=set(l)
print(S1)      #output-{1, 2, 3, 4, 's', 'a'}
print(l)       #output-[1, 2, 2, 3, 4, 'a', 'a', 's']

#2.ADDING AN ELEMENT TO SET-
S={1,2,3,'a','b','c'} 
S.add('r')     # here we can pass only one value at a time otherwise it will give error.
print(S)       #output-{1, 2, 3, 'c', 'b', 'a', 'r'}

#3.REMOVING AN ITEM-
S.remove(1)
print(S)      #output-{2, 3, 'r', 'c', 'a', 'b'}

#4. CHECKING FOR ITEM USING IN COMMAND-
print("2"in S)   # output-False as here 2 is a str.
print(2 in S)    # output-True  as 2 is int here .

#5.AMPERSAND "&" between 2 sets-
#NOTE --> here the elements which both have in common will be counted only.
set1={'a','s',1,2,3}
set2={1,2,3,4}
set3=set1&set2
print(set3)         #output{1, 2, 3}
#6.UNION OF 2 SETS-
set4=set1.union(set2)
print(set4)         #output-{'a', 1, 2, 3, 4, 's'}
#7.CHECKING FOR IS_SUBSET OF 2 SETS-
set1={'a','s',1,2,3}
set2={1,2,3,4}
set3={1,2,3}
#NOTE --> checking is set2 is subset of set1.
print(set2.issubset(set1))    #output-False.
print(set3.issubset(set1))    #output-True.
'''
#######################################################################################################################