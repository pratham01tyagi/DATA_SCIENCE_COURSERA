#this we are learning in our coursera classes week 1 course4 of Python for data science, AI & devlopment
#######################################################################################################################
# in python we could do type casting4
########################################################################################################################
#                                                STRINGS BASICS
'''
name= 'pratham is a good boy. '
print(name)
print(name[0:10])
print(name[::3])

#Performing operation on string-
name= 'pratham is a good boy. '

#1.Checking length-----------------------
print(len(name))
#2.String concatination.---------------------------------
print("hello do you know? "+name)  
#3.Multiple times-----------------------------------
print(3*name)   
#4.Immutable--------------------------
name = 'xyz'
name= name +' is donkey'
print(name)
#5.using \n (escape sequence)----------------------
print('pratham \n is a good boy. ')
#6.using \t (escape sequence)------------------
print('pratham \t is a good boy. ')
#7.placing \ symbol------------------------------
print('pratham \\ is a good boy. ')
print(r'pratham \ is a good boy. ')


'''
#######################################################################################################################
#                                          String Methord
'''when we apply a methord to a string A then it make it change and we get a new string B'''
'''
Intro ='My name is Pratham'

#1.UPPER()
INTRO=Intro.upper()
print(INTRO)
#2.replace()
replaced_string=Intro.replace('Pratham','tyagi')
print(replaced_string)
#3.find()
print(Intro.find('Pratham'))
'''
#######################################################################################################################

