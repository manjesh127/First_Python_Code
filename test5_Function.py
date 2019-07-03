# ==================>>>  function in python define by keyword def (reserver)  <<<====================
# def greet_user():  # == :  define a block of code in function
#     print("hii manjesh you are inside function")
#     print("enjoy funtion")


# print("start")
# greet_user()
# print("finish")

# ===================>>>function with parameter (to use as pr global)<<=====================
# def greet_user(name):
#     print(f"hii {name} you are inside function")
#     print("enjoy funtion")


# print("start")
# greet_user("manjesh")
# greet_user("again_manjesh_call")
# print("finish")

# def two_parameter(first_name, last_name):
#     print(f"hii {first_name} {last_name} you are inside function")
#     print("enjoy funtion")


# print("start")
# two_parameter("manjesh", "singh")
# print("finish")

# ======================================>> keyword argument  <<==============================
# def keyword_argv(firsst, second):  # == :  define a block of code in function
#     print(f"hii {firsst} {second} you are inside function")
#     print("enjoy funtion")


# print("start")
# keyword_argv(second="singh", firsst="manjesh")  # this is define the argument
# print("finish")

# ====================================>>   return statment <<================================
# by default all function in python return none
# def squre(number):
#     # return number*number
#     print(number*number)


# result = squre(3)  # print 9
# print(result)  # print none because no any value are return in squre function return


# ==================================>> creating a reusable function  <<<===========================
# def imoji_converter(mess):
#     words = mess.split(" ")
#     emoji = {
#         ":)": "\U0001f600",
#         ":(": "\U0001F614"
#     }
#     output = ""
#     for word in words:
#         output += emoji.get(word, word) + " "
#     return output


# mess = input(": ")
# print(imoji_converter(mess))


# ==============================>>> exception <<<=================================
