n = 4678
c = 0
sum = 0
while n>0:
    c=n%10
    sum = sum+c
    n=n//10
print(sum)