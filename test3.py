# ===========>> conditions stat <<=================
hot = False
cold = False
if hot:
    print('hot day')
    print('roj nahao')
elif cold:
    print('it is cold days')
    print('chay pio')
else:
    print('lovely day')

print('enjoy your day')

# ============>> example <<<==============
price = 1000000
has_credit = True
if has_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price

print(f"down payment is {down_payment}")

# ================>> example 2 <<<================
is_high_income = True
is_high_credit = True
criminal_record = False
# if multiple condition we want use and or directly
if is_high_credit and is_high_income:
    print("you are eligible for loan")
elif is_high_income:
    print('your credit is low')
elif is_high_credit:
    print('your income is low')
else:
    print("you are not eligible for loan both are low")

# ==================>>> example 3 <<<=================
temp = 30
if temp == 30:
    print('it is hot day')
else:
    print("its cold day")
print("thanks")

# =====================>>> example 4 <<================
name = 'manjesh singh'
print(len(name))
if len(name) <= 3:
    print('name must be atleast 3 character')
elif len(name) >= 20:
    print('name mustbe less than 20 character')
else:
    print('name condition is good')

# ===================>>   example 5 <<====================
waight = int(input('enter your wait :'))
unit = input('(L)bs or (K)g ')
if unit.upper() == "L":
    convert = waight*0.45
    print(f"you are {convert} kg")
else:
    convert = waight/0.45
    print(f"you are K {convert} kg")
