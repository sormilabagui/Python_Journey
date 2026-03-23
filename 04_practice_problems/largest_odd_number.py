numlist = []
for i in range(10):
    value = int(input("Enter value : "))
    numlist.append(value)

max = 0
for i in range(len(numlist)):   
    if (numlist[i] % 2) != 0:
        if max < numlist[i]:
            max = numlist[i]
            
print("\nMaximum odd number is ",max)
