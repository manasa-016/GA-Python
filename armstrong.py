num = int(input("Enter a number: "))

digits = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")