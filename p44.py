f = open("f.txt", "r+")
print(f.tell())
print(f.readline())
print(f.tell())
print("tell func tells about the where is the file pointer")
f.close