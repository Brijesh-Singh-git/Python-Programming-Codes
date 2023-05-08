num1 = int(input("Enter the first NUmber: "))
num2 = int(input("Enter the second NUmber: "))

# By Default in Python the input will be taken as String so we have to convert the string into Number using TypeCasting

print("The entered vales are: " + num1,num2)

print("----------------------------------------")

num1,num2 = num2,num1

print("The swapped values are: " + num1,num2)
