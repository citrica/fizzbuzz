number = int(input("Select a number between 1 and 100: "))
cont = 1

if 1 < number < 100:
    for cont in range(1, number+1):
        div3 = float(cont % 3)
        div5 = float(cont % 5)
        if (div3 == 0) and (div5 == 0):
            print("bizzbuzz")
        elif div3 == 0:
            print("fizz")
        elif div5 == 0:
            print("buzz")
        else:
            print(cont)
else:
    print("The number es incorrect. ")