'''
#1 Armstrong Numbere

num=int(input("Enter the Number"))
sum=0
temp = num

while temp >0 :
    rem = temp%10
    sum += rem**3
    temp= temp//10

if sum==num:
    print(num,"is  armstrong number")
else:
    print(num,"is not armstrong number")


#2palindrome Number

num=int(input("Enter the Number"))
rev=0
temp=num

while temp>0:
    rem=temp%10
    rev = rev*10+rem
    temp = temp//10

if num==rev:
    print(num,"is a palindrome number")
else:
    print(num,"is not palindrome number")


#3.spy numner

num=int(input("Enter the Number"))
sum = 0
product = 1
temp= num
while (num>0):
    rem = num % 10
    sum = sum + rem
    product= product * rem
    num = num // 10

if product==sum:
    print(temp ,"is a spy number")

else:
    print(temp,"is not spy number")



#4.strong number

num=int(input("Enter the Number"))
sum =0
temp=num

while temp>0:
    fact = 1
    rem = temp%10
    for i in range(1,rem+1):
        fact=fact*i

    sum =sum+fact
    temp=temp//10

if num== sum:
    print(num,"is strong number")

else:
    print(num,"is not strong number")



#5.neon number

num=int(input("enter the Number"))
sum = 0
temp =num
sq= num * num    #num=9
                 #sq=9*9=81

while sq>0: 
    rem =sq % 10    81% 1
    sum = sum + rem
    sq= sq // 10

if sum==temp:
    print(num,"is a neon number")
else:
    print(num,"is not neon number")


#.perfect number

num=int(input("Enter the Number"))

sum = 0
for i in range(1, num):
    if(num % i == 0):
        sum = sum + i
if (sum == num):
    print(num," is a Perfect number")
else:
    print(num,"is not a Perfect number")



#.count the digit

num =int(input("Enter the number"))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: ",count)

'''

#power of number

num=int(input("enter the Number"))

power=int(input("Enter power for givrn number"))

result=1
while power!=0:
    result**= num
    power=-1
print("answer is" + str(result))
