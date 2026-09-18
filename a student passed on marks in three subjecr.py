hindi=float(input("enter marks"))
english=float(input("enter marks"))
maths=float(input("enter marks"))
total_marks=hindi+english+maths
percentage=(total_marks/300)*100
if percentage>=45:
    print("passed")
else:
    print("failed")