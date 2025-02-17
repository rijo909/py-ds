# pattern 1
# * * * *
# * * * *
# * * * *
# * * * *
print()
square_len = 4
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        print(" * ", end=" ")
    print() # default param in end is newline (\n)

# pattern 2
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
print()
square_len = 4
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        print(f" {i} ", end=" ")
    print() # default param in end is newline (\n)

# pattern 3
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
print()
square_len = 4
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        print(f" {j} ", end=" ")
    print() # default param in end is newline (\n)

# pattern 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
print()
square_len = 4
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        if i >= j:
            print(f" {j} ", end=" ")
    print() # default param in end is newline (\n)

# pattern 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
print()
square_len = 4
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        if i <= j:
            print(f" {j} ", end=" ")
    print() # default param in end is newline (\n)

# pattern 6
# 1
# 2 3
# 4 5 6
# 7 8 9 10
print()
square_len = 4
c = 0
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        if i >= j:
            c+=1
            print(f" {c} ", end=" ")
    print() # default param in end is newline (\n)

# pattern 7
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
print("\n"*5)
square_len = 5
for i in range(1, square_len+1):
    for j in range(1, square_len+1):
        # if i >= j:
        #     print(f" {i} ", end=" ")
        # else:
        #     print(f" {j} ", end=" ")
            print(f" {max(i, j)} ", end=" ")
    print() # default param in end is newline (\n)