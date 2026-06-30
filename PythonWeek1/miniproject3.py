print("Simple Calculator")
num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))

print("\nResults")
print("Addition:", num1+num2)
print("Subtraction:", num1-num2)
print("Multiplication:", num1*num2)
print("Division:", num1/num2)
print("Floor Division:", num1//num2)
print("Remainder:", num1%num2)
print("Power:", num1**num2)


# Create a program that calculates the area of a rectangle.
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)



# Student Percentage Calculator

print("Student Percentage Calculator")

name = input("Enter Student Name: ")

subject1 = int(input("Enter Subject 1 Marks: "))
subject2 = int(input("Enter Subject 2 Marks: "))
subject3 = int(input("Enter Subject 3 Marks: "))
subject4 = int(input("Enter Subject 4 Marks: "))
subject5 = int(input("Enter Subject 5 Marks: "))


Totalmarks = subject1 + subject2 + subject3 + subject4 + subject5


percentage = (Totalmarks / 500) * 100

print("\n===== Student Report =====")
print("Name:", name)
print("Total Marks:", Totalmarks)
print("Percentage:", percentage, "%")
