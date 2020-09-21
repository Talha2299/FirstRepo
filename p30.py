print("choose 1 or 2")
a = input("> ")
if a == "1":
    print("choose 1 , 2")
    a1 = input("> ")
    if a1 == "2":
        print("good")
    elif a1 == "1":
        print("bad") 
    else:
        print("you dosent choose anyone")

elif a == "2":
    print("choose 3, 4")
    b1 = input("> ")
    if b1 == "3":
        print("good")
    elif b1 == "4":
        print("bad") 
    else:
        print("you dosent choose anyone")

else:
    print("choose any one of them")