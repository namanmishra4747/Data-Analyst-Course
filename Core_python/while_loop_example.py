num =12345
rev = 0

while num > 0:
    rem = num % 10
    num = num // 10
    rev = rev * 10 + rem
    print (rem, num)

print ("Your total sum is >>>", rev)

#hack

num =12345
rev = str (num) [ :: -1]
print (rev)