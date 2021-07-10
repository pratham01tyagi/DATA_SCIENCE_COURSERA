#######################################################################################################################
#                                                  Tuples

'''in python Tuples can contain int, float ,str and also other touples also called touple nesting.
 In the tuple every element could be acessed by index no.
they are stored in ()'''

'''

tuple =(1,2,3,4,'int',1.3334,2.44446)
print(type(tuple))

#1.slicing the tuple
print(tuple[0:5])

#2.concanating tuples
tuple1 =(1,2,3,4,'int',1.3334,2.44446)
tuple2=(5,6,9,'float')+tuple1
print(tuple2)

#3.length of tuple
print("the length of tuple is- \t",str(len(tuple)),'\n and the tuple is -\t',str(tuple))

#4.tuples are immutable
tuple1=(1,2,3,4,5)
tuple2=tuple1
#tuple2[2]=6
#tuple dose not support item assingment. as tuples are immutable hence due to above line there will be an error.
#but we can give another ratings to the tuple1
tuple1=(1,3,6,5,4,3,28,9,8)
print('now the tuple1 is- ',tuple1,'and tuple 2 is -',tuple2)

#5.sorting the touple
print('this tuple is going to be sorted now-'+str(tuple1))
Sorted_tuple=sorted(tuple1)
print("now the touple lookes like-"+str(Sorted_tuple))

'''
#######################################################################################################################
#                                                 Nesting Touples
'''touples could be nested means touple can hold touples inside it as shown. bellow'''
'''
touple=(1,2,3,5,4,(89,67,78),'hi','bye',(1.0,2.90))
print(str(touple)+'\n and the length is -\t'+str(len(touple)))
print(touple[0])
print(touple[5])
print(touple[6])
#if you want to acess the touple in the touple for example 78  then things are shown below-
print(touple[5][2])
'''
#######################################################################################################################