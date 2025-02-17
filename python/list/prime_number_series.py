upper_limit = int(input("Enter upper limit of prime number series : "))
lower_limit = int(input("Enter limit of prime number series : "))
prime_lst = []
# while num1 <= len(prime_lst)-1:
#     print(num1)
#     for i in range(num1-1):
#         c = 0
#         for j in range(2, i//2):
#             if i%j == 0:
#                 c+=1
#         if c==0 and i != 1:
#             prime_lst.append(i)
#             print("\n")
# print(prime_lst)
for i in range(upper_limit, lower_limit-1):
    c=0
    for j in range(1, i+1):
        if i%j == 0:
            c+=1
    if c==2 and i != 1:
        prime_lst.append(i)
print(prime_lst)