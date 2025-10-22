n = int(input())
if n <= 0:
    print("NotProceed")
else:
    base1 = int(input())
    base2 = int(input())
    if base2<base1: 
        print("NotProceed")
    else:
        print(base1, base2, end=" ")
        next_number = base1 + base2
        count = 2
        while count < n + 2:
            print(next_number, end=" ")
            count += 1
            base1, base2 = base2, next_number
            next_number = base1 + base2