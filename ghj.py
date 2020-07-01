a= int(input("enter the number : "))
b=0
c=1
d=0
if a<=0:
   print("Enter a positive number")
elif a==1:
   print("fibonacii sequence upto", a )
   print(b)
else: 
    print("fibonacii sequence upto",a)
    while d<a:
        print(b)
        e=b+c
        b=c
        c=e
        d+=1
   
