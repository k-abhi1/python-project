#enter a number
n1=int(input("enter a first number"));
op=input("enter the op (+,-,*,/,%):")
n2=int(input("enter a second number"));

if op=="+":
    print(n1+n2);
elif op=="-":
    print(n1-n2);
elif op=="*":
    print(n1*n2);
elif op=="/":
    print(n1/n2);
elif op=="%":
    print(n1%n2);
else:
    print("invalid operator")
    
