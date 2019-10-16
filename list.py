#creating list
List = [] 
print("Intial blank List: ") 
print(List)


List = ['welcome'] 
print("\nList with the use of String: ") 
print(List)


List = ["Welcome", "India", "Welcome"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[2]) 


list=[]
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

#append
my_list=['A','B'] 
my_list.append('C') 
print(my_list)


my_list=['A','B','C'] 
another_list = [6,0,4,1] 
my_list.append(another_list) 
print(my_list) 


#extend
my_list=['A','B','C'] 
another_list = [6,0,4,1] 
my_list.extend(another_list) 
print(my_list) 


#pop
lis=[2,1,3,5,4,3,8]
del(lis[2:4])
print(lis)


#insert
list=[1,2,3,4,5]
list.insert(5,6)
print(list)


#remove
list=[1,2,3,4,5]
list.remove(5)
print(list)


#sort
list=[3,4,5,1,7,2]
list.sort()
print(list)


#reverse
list=[3,4,5,1,7,2]
list.reverse()
print(list)


#index
list1=[1,2,3,4,1,1,1,4,5] 
print(list1.index(4)) 
  
list2=['a','b','m','t','e']  
print(list2.index('t')) 



#count
list1=[1,2,3,4,1,1,1,4,5] 
print(list1.count(4)) 
  
list2=['a','b','m','t','e','e']  
print(list2.count('e')) 


#copy
list1=[1,2,3,4]  
list2=list1.copy()
print(list2) 
    