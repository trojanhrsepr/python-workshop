import pprint
f1 = open("data1.txt", "w+")

f1.write("asd,dfgh,asd,50,40,60\n")
f1.write("zxc,xcbxv,sdf,34,54,12\n")
f1.close()

stud1 = {}
f2 = open("data1.txt", "r")
for elem in f2:
    elem = elem.rstrip("\n")
    if elem:
        name, dept, loc, *mlst = elem.split(",")
        stud1[name] = {}
        stud1[name]["dept"] = dept
        stud1[name]["loc"] = loc
        stud1[name]["marks"] = [int(e) for e in mlst]
f2.close()
pprint.pprint(stud1)
