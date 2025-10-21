#Encryption
#ask the user to input his/her integer

users_integer = input("Enter a 4 digits integer for encryption: ")

#convert the input from string to integer

number = int(users_integer)

#implicitly define the integer
#abcd is 4 digits
#a is 1st digit, b is 2nd digit, c is third digit and d is forth digit. 

a = number // 1000                      #this will remove last 3 digits
b = number // 100 % 10                  #this will remove last 2 digits and extract the last digit
c = number // 10 % 10                   #this will remove last 1 digit and extract the last digit
d = number % 10                         #this will extract the last digit

#add 7 to each of the digits and modulus the sum by 10

a = (a + 7) % 10
b = (b + 7) % 10
c = (c + 7) % 10
d = (d + 7) % 10

#Swap the 1st and the 3rd digits; the 2nd and the 4th digits: c,d,a,b

first_digit = c
second_digit = d
third_digit = a 
forth_digit = b

#convert the digits from integer to string

result = str(first_digit) + str(second_digit) + str(third_digit) + str(forth_digit)

#then print out the result

print("==> Encrypted integer is " + result)

#Decryption
#ask the user to input his/her integer

users_integer = input("Enter a 4 digits integer for decryption: ")

#convert the input from string to integer

number = int(users_integer)

#implicitly define the integer
#abcd is 4 digits
#a is 1st digit, b is 2nd digit, c is third digit and d is forth digit. 

a = number // 1000                       #this will remove last 3 digits
b = number // 100 % 10                   #this will remove last 2 digits and extract the last digit
c = number // 10 % 10                    #this will remove last 1 digit and extract the last digit
d = number % 10                          #this will extract the last digit

#add 3 to each of the digits and modulus the sum by 10

a = (a + 3) % 10
b = (b + 3) % 10
c = (c + 3) % 10
d = (d + 3) % 10

#Swap the 1st and the 3rd digits; the 2nd and the 4th digits: c,d,a,b

first_digit = c
second_digit = d
third_digit = a 
forth_digit = b

#convert the digits from integer to string

result = str(first_digit) + str(second_digit) + str(third_digit) + str(forth_digit)

#then print out the result

print("==> Decrypted integer is " + result)

input("Press enter to terminate")