a="hello  all"
print (a)
print (len(a))

a="hello all"
print(a[2:7])

a="hii i am annu"
print ("am" in a)
print ("hlo" in a)
if "hii" in a:
    print ("yes,'hii' in a string")
else :
    print("no,'hii' in a string")

message="i am annu rao"
print(message[3:5])
print (message[-5:-3])
print (a.lower())
print(message.replace('annu','anisha'))


a="annu"
b="rao"
c=a+""+b
print(c)
#concantinate


a="annu"
print(a[2])
#indexing

a="hii annu "
print(a[3:7])
#slicing


a="hello"
print(a.upper())
#upper()

a="RIGHT"
print(a.lower())
#lower()

a="   hii annu    "
print(a.strip())
#strip=remove space

a="my name is annu"
print(a.replace("annu","anisha"))
#replace()

a="annu anisha anny"
print(a.split())
#split()=convert string to list

a="hlo my name is annu rao"
print(a.find("name"))
#find()

a="hlooooooooooo"
print(len(a))
#len()

a="hii i am annu"
print(a.title())
#title=first letter of each word capital



x=10 #global variable
def mess ():
    print(x)
mess ()
print(x)


def text():
    y=20 #local variable
    print(y)
text()



x=10 #global variable
def mess():
    y=20 #local variable
    print("Global:",x)
    print("local:",y)
mess()  
print("global outside function",x) 





#list_name=["annu","anisha","anny"]
fruits=["apple","banana","cherry"]
print(fruits)


#append()=add an item to the end of the list
a=["apple","banana","cherry"]
a.append("orange")
print(a)

#insert()=add an item at the specified index
a=["apple","banana","cherry"]
a.insert(1,"orange")
print(a)

#remove()=remove the specified item
a=["apple","banana","cherry"]
a.remove("banana")
print(a)

#pop()=remove the specified index
a=["apple","banana","cherry"]
a.pop(1)
print(a)

#delete()=remove the specified index
a=["apple","banana","cherry"]
del a[0]
print(a)

#CLEAR()=remove all the items from the list
a=["apple","banana","cherry"]
a.clear()
print(a)


#SLICE()=return a part of the list
a=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(a[2:5])


#replace()=replace the specified item with the new item
a=["apple","banana","cherry"]
a[1]="orange"
print(a)


#reverse()=reverse the order of the list
a=["apple","banana","cherry"]
a.reverse()
print(a)


#sort()=sort the list
a=["apple","banana","cherry"]
a.sort()
print(a)


#copy()=copy the list
a=["apple","banana","cherry"]
b=a.copy()
print(b)


#count()=return the number of times the specified item appears in the list
a=["apple","banana","cherry","apple"]
print(a.count("apple"))


#count()=return the number of times the specified item appears in the list
a=["apple","banana","cherry","apple"]
print(a.count("apple"))



#index()=return the index of the first occurrence of the specified item
a=["apple","banana","cherry"]
print(a.index("banana"))



#list length
a=["apple","banana","cherry"]
print(len(a))

#push()=add an item to the end of the list
a=["apple","banana","cherry"]
a.append("orange")
print(a)

#nested list
a=["apple","banana","cherry",["kiwi","melon","mango"]]
print(a)


#list concatenation
a=["apple","banana","cherry"]
b=["orange","grape","mango"]
c=a+b
print(c)


#loop through a list
a=["apple","banana","cherry"]
for x in a:
    print(x)

#extend()=add the elements of a list (or any iterable), to the end of the current list
a=["apple","banana","cherry"]
b=["orange","grape","mango"]
a.extend(b)
print(a)

a=["a","b","c","o","g","m"]
print(a[1:4])
print(a)


a=["a","b","c","o","g","m"]
print(a[-4:-2])

#tuple
#change tuple to list
#add element to list
#change list to tuple
number=(1,2,3,4,)
print(number)
number1=list(number)
print(number1)
number1.append(5)
print(number1)
number=tuple(number1)
print(number)

#tuple
mess=("annu",(4,4.5,True),5)
print(mess)
text=list(mess)
print(text)
text.pop(2)
print(text)
mess=tuple(text)
print(mess)


#concatenate tuple
number=(1,2,3,4,5)
number1=(6,7,8,9,10)
number2=concat=number+number1
print(number2)


#unpacking a tuple
number=((1,2,3),(4,5,6),7,8,9)
n1,n2,*n3=number
print(n1)
print(n2)
print(n3)

#count in tuple
number=(1,2,3,4,5,6,7,8,9,10,5,5,5)
print(number.count(5))

#index in tuple
number=(1,2,3,4,5,6,7,5,8,9,5,10)
print(number.index(5))



#tuple
this_tuple=["apple","banana","cherry"]
print(this_tuple[-3:])
print(this_tuple[:2])

#tuple
a=("apple","banana","cherry")
print(a)
a1=list(a)
print(a1)
a1.append("orange")
print(a1)
a=tuple(a1)
print(a)

#syntax of set
#unordered, unindexed, no duplicate values
#allows different data types
a={"apple","banana","cherry"}
print(a)
a={"apple","banana","cherry","apple","banana","mango"}
print(a)
print(len(a))

a={1,2.0,3,"hlo",True,(1,2,3)}
print(a)

a={1,"hlo",2.4,True,(1,2,3)}
print(a)
print(type(a))

#change list to set
#change set to list
a=["apple","banana","cherry"]
a1=set(a)
print(a1)
a=list(a1)
print(a)

#change tuple to set
#change set to tuple
a=('apple','banana','cherry')
a1=set(a)
print(a1)
a=tuple(a1)
print(a)

#empty set
a=set()
print(a)
print(type(a))

#dictionary
a={}
print(a)
print(type(a))


a={1,2,3,4,5}
print(1 in a)
print(6 not in a)

#for loop in set
number={1,2,3,4,5}
for x in number:
    print(x)

 #add()=add an item to the set
number={1,2,3,4,5}
number.add(6)
print(number)

#concatenate two sets
number={1,2,3,4,5}
number1={6,7,8,9,10}
number2=number.union(number1)
print(number2)

#add two sets using update()
number={1,2,3,4,5}
number1={6,7,8,9,10}
number.update(number1)
print(number)


#add two different data types using update()
number={1,2,3,4,5}
number1=(6,7,8,9,10)
number.update(number1)
print(number)

#remove()=remove the specified item
number={1,2,3,4,5}
number.remove(3)
print(number)


#discard()=remove the specified item
number={1,2,3,4,5}
number.discard(3)
print(number)
number.discard(6)
print(number)

#pop()=remove the specified index
number={0,1,2,3,4,5}
number.pop()
print(number)

#clear()=remove all the items from the set
number={1,2,3,4,5}
number.clear()
print(number)


#del()=delete the set
number={1,2,3,4,5}
del number

#union()=return a set that contains all items from both sets
number={1,2,3,4,5}
number1={6,7,8,9,10}
number2=number.union(number1)
print(number2)


#intersection()=return a set that contains only the items that are present in both sets
number={1,2,3,4,5}
number1={4,5,6,7,8}
number2=number.intersection(number1)
print(number2)

#difference()=return a set that contains the items that are present in the first set but not in the second set
number={1,2,3,4,5}
number1={4,5,6,7,8}
number2=number.difference(number1)
print(number2)


#symmetric_difference()=return a set that contains the items that are present in either set, but not in both
number={1,2,3,4,5}
number1={4,5,6,7,8}
number2=number.symmetric_difference(number1)
print(number2)


#isdisjoint()=return True if both sets have no items in common, otherwise return False
number={1,2,3,4,5}
number1={6,7,8,9,10}
number2=number.isdisjoint(number1)
print(number2)

#pop()=remove the specified index
number={0,1,2,3,4,5}    
print(number)
number.pop()
print(number)

a={1,2,3,4,5}
ai=tuple(a)
print(ai)


#update()=add the elements of a set (or any iterable), to the end of the current set
number={1,2,3,4,5}
number1={6,7,8,9,10}
number.update(number1)
print(number)

a=[1,2,2,3,4]
a1=set(a)
print(a1)
a=list(a1)
print(a)

email=["anishayadav@gmail.com","john.doe@gmail.com","jane.smith@gmail.com","anishayadav@gmail.com"]
email1=set(email)
print(email1)




#dictionary
#use of dictionary is to store data values in key:value pairs.
#syntax of dictionary
#dictionary_name={key1:value1,key2:value2,key3:value3}
#data type=key:value pair
#key:value pair=keys are unique, values can be duplicate
#values can be any data type, keys can be any immutable data type
# student={}
# print(student)


# student={"name":"annu","age":21,"city":"hyderabad"}
# print(student)

# languages={"python":"programming language","c++":"programming language","english":"language"}
# print(languages)
# print(len(languages))


# languages=dict()
# print(type(languages))

# student=dict( name="annu",age=21,city="hyderabad")
# print(student)

#tuple and list to dictionary
# #tuple and list can be converted to dictionary using dict() function
 #student=[("name","annu"),("age",21),("city","hyderabad")]
 #print(student)
 #student1=dict(student)
 #print(student1)

#list with different data types to dictionary
student=[("name","annu"),("age",21),("city","hyderabad")]
student1=dict(student)
print(student1)

#accessing keys in dictionary
#use when you want to access the value of a key in a dictionary.
#if the key does not exist, it raises a KeyError.
student={"name":"annu","age":21,"city":"hyderabad"}
print(student["name"])


#get()=return the value of the specified key
#use get() method to access the value of a key in a dictionary. 
# If the key does not exist, it returns None instead of raising an error.
student={"name":"annu","age":21,"city":"hyderabad"}
print(student.get("name"))
print(student.get("age","age  not found"))
print(student.get("email"))
print(student.get("email","email not found"))


#update()=update the value of the specified key
#use update() method to update the value of a key in a dictionary.
student={"name":"annu","age":21,"city":"hyderabad"}
print(student)
student.update({"age": 22})
print(student)
student["email"]= "annu@gmail.com"
print(student)
student.update({"cource":"python","year":2024})
print(student)


#pop()=remove the specified key and return the corresponding value
#use pop() method to remove a key-value pair from a dictionary.
student={"name":"annu","age":21,"city":"hyderabad"}
age=student.pop("age")
print(student)

#popitem()=remove the last inserted key-value pair and return it as a tuple
#use popitem() method to remove the last inserted key-value pair from a dictionary.
student={"name":"annu","age":21,"city":"hyderabad"}
student1=student.popitem()
print(student1)


#discard()=remove the specified key-value pair from a dictionary
#use discard() method to remove a key-value pair from a dictionary.
# Note: discard() is typically used with sets, not dictionaries.


#remove()=remove the specified key-value pair from a dictionary
#use remove() method to remove a key-value pair from a dictionary.
#example:
student={"name":"annu","age":21,"city":"hyderabad"}



#dictonary methods
#keys()=return a view object that displays a list of all the keys in the dictionary
#values()=return a view object that displays a list of all the values in the dictionary
#items()=return a view object that displays a list of all the key-value pairs in


#nested dictionary
#nested dictionary is a dictionary that contains another dictionary as a value.
#example of nested dictionary
student={"name":"annu","age":21,"city":"hyderabad","marks":{"maths":90,"science":85,"english":95}}
print(student)
print(student["marks"]["maths"])


python={"annu","annyy","anisha"}
java={"akshu","anu","ashu","annu"}
print(python.intersection(java))


#.keys()=return a view object that displays a list of all the keys in the dictionary
#.values()=return a view object that displays a list of all the values in the dictionary
#.items()=return a view object that displays a list of all the key-value pairs in the dictionary



student:{
    "name":"annu",
    "age":21,
    "city":"hyderabad",
    
    "marks":{
     "maths":90,
     "science":85,
     "english":95,
    },
    "course":{
     "python":2024,
     "java":2023,
       },
    }
print(student)                                                        
print(student.get("marks").get("hindi", "marks not found"))









