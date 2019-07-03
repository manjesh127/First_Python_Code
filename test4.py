# ======>> loops <<======
i = 1
while i <= 5:
    print('| * '*i)
    i = i+1
print('done')

number = 6
number_count = 0
number_limit = 3

while number_count < number_limit:
    gess = int(input("enter your gess number : "))
    number_count += 1
    if gess == number:
        print("you won ")
        break

else:
    print('sorry play again')

command = ""
start=False
while command!="quit":
    command=input('> ').lower();
    if command=="start":
        if start:
            print('car is already start')
        else:
            start=True
            print('car start...');
    elif command=="stop":
        if not start:
            print('car is already stop')
        else:
            start=False
            print('car stop...')
    elif command=="help":
        print("""

        stop : to stop the car
        start: to start the car
        quit : to quit the game
        """)
    elif command=="quit":
        break
    else:
        print("sorry i dont understand")


# =============================>> for loop << ============================
for item in "python":
    print(item)
for item in ["manje","singh","maad"]:
    print(item)
for item in range(10):
    print(item)
for item in range(5,10):
    print(item)
for item in range(5, 10, 2):
    print(item)

prices = [10, 12, 9]
total = 0
for price in prices:
    total += price
print(f"total :{total}")

# ============================>> nested loop <<==============================
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

number = [8, 6, 4, 2, 1]
for x in number:
    print("*"*x)

number = [2, 3, 4, 5]
print(number)
print(number[2:])
print(number[0])


# ==============   find the biggest number -==================
numbers = [2, 3, 51, 1, 6, 9]
max = 0
for number in numbers:
    if number>max:
        max=number
print(max)

# ===================>>  unpacking  <<=====================
cordn = (1, 2, 3)
x, y, z = cordn
print(x)

# ===========>> dictionary - can define and store key valu pair  imp <<< =================
customer = {
    "name": "manjesh singh",
    "feb_Number": 16,
    "developer": True
}
print(customer["feb_Number"])
print(customer.get("anyKey","keyValu"))
customer["birthday"]="1 august"
print(customer["birthday"])

# ===============>>>   example  <<========================
phoneNO = input("user phone number : ")
digit_maping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phoneNO:
    output += digit_maping.get(ch, "!")+ " "
print("output is ", output)


# =====================>>  emoji <<<==========================
mess = input(">")
words = mess.split(" ")
# print("\U0001F614")
emoji = {
    ":)": "\U0001f600",
    ":(": "\U0001F614"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
