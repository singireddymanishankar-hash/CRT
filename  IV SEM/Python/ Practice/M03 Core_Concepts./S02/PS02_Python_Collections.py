SAMPLE_LIST = [1, 2, 3, 4, 5]

#1) create a list of 5 elements and print the list
my_list = list(SAMPLE_LIST)
print(my_list)

#2) accessing elements of list
print(my_list[0])
print(my_list[-1])

#3) creating list with repeated elements
print(my_list * 2)

#4) removing elements from list
my_list = list(SAMPLE_LIST)
my_list.remove(3)
print(my_list)

#5) slicing a list
my_list = list(SAMPLE_LIST)
print(my_list[1:4])
