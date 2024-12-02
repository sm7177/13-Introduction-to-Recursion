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









def fact(n):
    if(n==0 or n==1):
        return 1
    
    return n*fact(n-1)

n=int(input("Enter a number:"))
print(fact(n))