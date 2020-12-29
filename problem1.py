sum = 0
for i in range(1000000):
    bina = int(str(bin(i)).replace('0b',''))
    if(i==int(str(i)[::-1]))or(bina==int(str(bina)[::-1])):
        #print("i : "+str(i))
        #print("bina : "+str(bina))
        sum+=i
print("Sum of numbers : ",sum)