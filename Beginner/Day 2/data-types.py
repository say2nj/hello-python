# Data Types

# ---------- String -------------
print("Hello"[4])
print("123")
print(type("123"))
# print(23+4+"27") --error

# ------------ Integer ------------
print(123_456_789)
print(type(123_456_789))

# ----------- Float ------
print(3.14159)
print(type(3.14159))

# ----------- Boolean -------
print(True)
print(False)
print(type(True))

# ----------- String Concatenation ---------------

# name_length = len(input("Enter your name: "))
# # print("Your name has "+name_length+ " characters.") -- error: cannot add integer to string
# print("Your name has ",name_length, " characters.")

# ----------- Data Type Conversion ---------
a = 1234
print(type(a))
a = str(a)
print(type(a))

print(70 + float("12.7"))

print(str(None))

print(float("1254"))
print(float(65))
print(float(True))

print(int(54.55))

print(int(True))

# ------- F-strings -------

print(round(8/3,2))
print(type(8//3))

num = 2
num **=3
print(num)

num = 2
# num //=3
num %=3
print(num)

some_value =3.14159
print(f"Printing some value {some_value}")
print("Some value: %.2f" %(some_value))