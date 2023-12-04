#1
while True:
    user_input = input("Enter a word (or 'STOP' to end): ")

    if user_input.upper() == "STOP":
        break

    lowercase_input = user_input.lower()
    print("Lowercase output:", lowercase_input)

print("Program stopped.")
#2
salaries = {'Jake': '$100K', 'Anand': '$120K'}

for person, salary in salaries.items():
    print(f"{person}'s salary is {salary}.")
#3
my_num = (4, 30, 2017, 2, 27)

formatted_string = "{} {} {} {} {}".format(my_num[3], my_num[4], my_num[2], my_num[0], my_num[1])

print(formatted_string)