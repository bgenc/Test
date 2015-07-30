birthday = raw_input("Enter birthday in dd.mm.yyyy : ")
bd = birthday.split(".")

day = int(bd[0])
month = int(bd[1])
year = int(bd[2])

if month < 3:
    A = month + 10
    year = year - 1
else:
    A = month

B = day

C = year % 100

D = (year - C) / 100

print A,B,C,D

W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2 * D
R = Z % 7
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print "You were born on", days[R]