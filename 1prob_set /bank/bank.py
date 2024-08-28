x = input("Greeting: ") # ask for a input of greeting

x = x.lower().strip() #strip caplistation

if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20") #if the greeting start with H print $20
else:
    print("$100") #else print $100


