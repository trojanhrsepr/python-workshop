# Adding two numbers

num1 = input("Enter value 1: ")
num2 = input("Enter second value: ")

res = int(num1) + int(num2)
print("Sum = ",res)
print("Sum of %s and %s is %s" % (num1, num2, res))
print("Sum of {0} and {1} is {2}".format(num1, num2, res))

data = 'Monday'
a = data[:2].upper() + data[2:-2] + data[-2:].upper()
print(a)
a = data[:3].lower() + data[len(data):-4:-1].upper()
print(a)

ip = '192.168.1.255'
print(ip.split(".")[-1])

data = '19-mar-2017 02:45:23'
print(data.split(".")[-1][-3])

data = 'today.xlsx'


data = 'math-57-soc-75-sci-76'
print(data.split("-")[1::2])

data='arun-blr-10,20,30'
mlst = (data.split("-")[-1].split(","))
total = int(mlst[0]) + int(mlst[1]) + int(mlst[2])

print(sum(int(e) for e in data.split("-")[-1].split(",")))

print(sum(map(int, data.split("-")[-1].split(","))))

data = "20-15-30-40"
print("-".join(str(int(e) + 1) for e in data.split("-")))
res = "21-16-31-41"

sent = input("Enter string: ").lower()
if sent.split()[0] == sent.split()[-1]:
    print("same")
else:
    print("Diff")


