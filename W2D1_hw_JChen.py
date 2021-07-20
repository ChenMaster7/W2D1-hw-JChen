# Exercise 1: Print all cubed numbers up to the total value of 1000. Aka break loop if cubed number is >1000.
max_input_num = 100
cubed_num_list = []
for base in range(1,max_input_num):
    cubed_num = base**3
    if cubed_num <= 1000:
        cubed_num_list.append(cubed_num)
    else:
        break
print(f"The list of cubed numbers up to {max_input_num} is {cubed_num_list}")




# Exercise 2: Get first prime numbers up to 100. [Doesn't work]
max_input_num = 100
num = list(range(1, max_input_num+1))  # from 2 to input number
prime = []
for current_num in num:  # index count
    count = 0
    for divider in range(2, current_num+1):
        if current_num <= 1 or current_num % divider != 0:
            count += 1
            break
    if count > 0:
        prime.append(current_num)


    # for divider in range(2, num[index]+1):  # sets the divider, which ranges from 2 to the current last number
    #     if num[index] % divider == 0:  # checks if divisible. If it is divisible, then break loop and skip to next number.
    #         break
    #     prime.append(num[index])  # if none are divisible, then it is a prime. Record the current number as a prime.
    #     break




# Exercise 3: Take user's input for their age. If <18, print kids. If 18-65, print adults. Else, print seniors.
age = input("How old are you? Please enter a number \n")

try:  # check if input can be an int.
    age = int(age)
except ValueError:
    try:  # check if input can be a float. Round down and convert to int.
        age = float(age)
        age = math.floor(age)
    except ValueError:
        print("Please enter a number.")

# categorize
if age < 18:
    print("you are a kid")
elif (age >= 18) and (age < 65):
    print("you are an adult")
else:
    print("you are a senior")