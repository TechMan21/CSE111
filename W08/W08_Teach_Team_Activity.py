print()
column_row = int(input('How many columns and rows do you want in your multiplication table? '))

for i in range (1, column_row + 1):
    print(i, end = ' ')
    for j in range (i + 1, column_row, 2):
        print(j)

print()
print()
