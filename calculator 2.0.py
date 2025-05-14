

x=int(input("Enter DOB :"))
y=int(input("Enter current year :"))
print(f"age={y-x}")

x=int(input("Enter first no :"))
y=int(input("Enter second no :"))
op=input ("Enter op")
if op == "+" :
    print(f"sum={x+y}")
elif op == "-" :
    print(f"sub={x-y}")
elif op == "/" :
    print(f"div={x/y}")
elif op == "*" :
    print(f"mul={x*y}")
else :
    print("error")
