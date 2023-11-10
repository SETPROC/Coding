str = input()
for i in str:
    if ord(i) <= 90:
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
    