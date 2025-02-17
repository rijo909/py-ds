# Fibonacci series
# 0 1 1 2 3 5 8
n = int(input("Enter the number of series required : "))
lst_fib = [0, 1]
for i in range(n-2):
    lst_fib.append(lst_fib[-1] + lst_fib[-2])
# print(lst_fib)
for i, j in enumerate(lst_fib):
    if i != len(lst_fib)-1:
        print(j, end=", ")
    else:
        print(j)
