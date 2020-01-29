# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = input("Write a number: ")
n1 = int("%s"% n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s"% (n, n, n))
print("Result: ", n1+n2+n3)