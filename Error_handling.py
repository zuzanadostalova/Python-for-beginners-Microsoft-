# x = 206 
# y = 206
# if x == y
#     print("Success!!!")
# syntax error

# x = 206 
# y = 206
# if x == y:
#     print("Success!!!")
# REPAIRED syntax error, colon was missing...broken car

# x = 42
# y = 0
#     print(x/y)
# runtime eror

x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero")
else:
    print("Something else went wrong")
finally:
    print("This is our cleanup code")
# REPAIRED runtime eror...closed road / you need to build a bridge to get over a river 

# x = 206
# y = 42
# if x < y:
#     print(str(x), "is greater than", str(y), sep=" " )
# logic error

# x = 206
# y = 42
# if x > y:
#     print(str(x), "is greater than", str(y), sep=" " )
# REPAIRED logic error...wrong destination