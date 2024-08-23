studLst = ["amit-cse-23", "asd-fde-34"]
marks1 = []
for string1 in studLst:
    name, *stud, marks = string1.split('-')
    marks1.append(int(marks))
    print(name, marks)
print(sum(marks1))
