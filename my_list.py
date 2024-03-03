# creating an empty list 
my_list =  []

# appending elements 10, 20, 30 and 40 to my_list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# inserting the value 15 at the second position on the list 
my_list.insert(1, 15)
print("new list")
print(my_list)

# extending my_list with another list [60 70 80]
extend_list = [50, 60, 70]
my_list.extend(extend_list)
print("extended list")
print(my_list)

# removing the last element from my_list 
remove_element = [70]
my_list.remove(70)
print(my_list)

# sorting my_list in an ascending order 
sorted(my_list) 
print("sort the list")
print(my_list)

# finding and printing the index of the value 30 from my list 
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)

