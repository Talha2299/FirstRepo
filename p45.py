f = open("f.txt", "r+")
f.seek(5)
print(f.readline())
f.seek(10)
print(f.readline())
print("seek func for reset the pointer to the input location")
f.close