"""
luhm formula to check validity of cards
1.reverse the digits
2.leave the odd digits
3.double the even digits , if > 10 , sum the 2 digits
4.add all the odd + even digits
5.modulo 10 , if == 0 , valid , else invalid
"""

number = input ("Enter a 16 digit credit card no: ")

reverse_number = number[::-1]
#trans_table = str.maketrans({"-":""," ":""})
reverse_number_split = reverse_number.split("-")
reversal_number = "".join(reverse_number_split)


print(reversal_number)

sum_even = 0
sum_odd = 0

even_digit = reversal_number[1::2]
print(even_digit)
for digit in even_digit:
    multiply_even = int(digit) *2
    if multiply_even >= 10:
        multiply_even = int(multiply_even)//10 + int(multiply_even)%10
    sum_even += multiply_even
print(sum_even)
    
odd_digit = reversal_number[::2]
for digit in odd_digit:
    sum_odd += int(digit)
print(sum_odd)

total_sum = sum_even + sum_odd
print(total_sum)

if total_sum % 10 == 0:
    print ("Vaiid")
else:
    print ("Invalid")



    
