n = (int(input("input")))

while n<0 :
    a = (int(input("Enter no")))
def fibonacci(n) :

    if(n == 0):
        return 0;

    elif(n == 1):
        return 1;
    elif(n>1):

        a =(n-1)+(n-2)
        return a;
    
Answer = fibonacci(n)
print("number is : ",n)
print("Fibornoc value is",(n-1))
print(" Answer is :  ",Answer)
