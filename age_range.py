age = int(input())
if age <= 12:
    print("child")
if 13 <= age < 20:
    print("teenager")
if 20 <= age <= 30:
    print("young adult")
if 31 <= age <= 59:
    print("middle age")
if 60 <= age:
    print("old age")

print("or")

if not (age > 12):
    print("child")
if 13 <= age and age < 20:
    print("teenager")
if 20 <= age and age <= 30:
    print("young adult")
if not (31 > age) and not (age > 59):
    print("middle age")
if not (60 > age):
    print("old age")
