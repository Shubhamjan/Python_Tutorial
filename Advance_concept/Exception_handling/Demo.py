class AgeError(Exception):
    pass

# try:
#     a = 10/0
# except ZeroDivisionError:
#     print("Divide by zero")
# else:
#     print("works fine")
# finally:
#     print("Always runs")

try:
    a = int("ten")
except TypeError as e:
    print("Error is ",e)
except ValueError as e:
    print("Error is ",e)

if 10>12:
    print("Good")
else:
    raise AgeError("Age is incorrect")
