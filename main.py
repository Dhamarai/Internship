# 1.Printing python version
import sys
print("Python version:",sys.version)

# 2.printing current date and time
from datetime import datetime
print("Current date and time:",datetime.today())

# 3.printing name in reverse order
first_name = input("Enter first name:")
last_name = input("Enter last name:")
reverse1= first_name[::-1]
reverse2= last_name[::-1]
print(reverse2 +" "+ reverse1)

# 4.list and tuple
str1 = input("Enter numbers:")

lst1=[]
for i in str1:
    if i==',':
        continue
    lst1.append(i)

print("List:",lst1)
print(tuple("Tuple:",lst1))

# 5.print extension of the file
file = input("Enter the filename:")
ind = file.rfind(".")
print(file[ind+1 : len(file)])


# 6.Printing first and last element
color_list=["Red","Green","White","Black"]
print(color_list[0],color_list[-1])

# 7.print exam schedule
from datetime import datetime
exam_st_date=datetime(2014,12,11)
exam=exam_st_date.strftime("%d/%m/%Y")
print("The examination starts from",exam)

















