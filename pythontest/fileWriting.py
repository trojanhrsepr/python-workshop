f1 = open("data.txt", "w+")

f1.write("asd dfgh\n")
f1.write("zxc xcbxv\n")
f1.close()

encode = {}
f2 = open("data.txt", "r")

for elem in f2:
    firstname, lastname = elem.rstrip("\n").split()
    print("%s %s" %(firstname.upper(), lastname))
f2.close()

