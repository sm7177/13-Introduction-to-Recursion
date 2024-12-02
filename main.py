# def dream():
#     print("Dream")
#     dream()
    
# dream()





# def add():
#     x=4
#     y=5
#     z=x+y
    
#     print(z)
    
#     add()
    
# add()



# def printno(n):
#     if (n>10):
#         return
#     print(n)
    
#     printno(n+1)
    
# printno(1)









# def fact(n):
#     if(n==0 or n==1):
#         return 1
    
#     return n*fact(n-1)

# n=int(input("Enter a number:"))
# print(fact(n))











def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
    
n_terms=10

if n_terms<=0:
    print("Invalid input! Please enter a positive number.")
else:
    print("Fibonacci Series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))