# Write a Python program to accept a filename from the user and print the extension of that.

filename = input("Write a filename: ")
print("File extension: ", repr(filename.split(".")[-1]))