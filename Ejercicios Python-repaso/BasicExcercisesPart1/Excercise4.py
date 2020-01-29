# Write a Python program which accepts a sequence of comma-separated numbers 
# from user and generate a list and a tuple with those numbers.

data = input("Sample data: ")
data_list = data.split(",")
data_tuple = tuple(data_list)

print("List: ", data_list)
print("Tuple: ", data_tuple)