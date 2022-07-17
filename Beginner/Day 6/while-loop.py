count = 10
while count:
    print(count, end=", ")
    count -= 1
else:
    print("Loop Ended")

count = 10
while count:
    if count in (3,6,9):
        count -= 1
        continue
    else:
        print(count, end=", ")
    count -= 1
else:
    print("Loop Ended")

