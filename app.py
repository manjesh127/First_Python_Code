# way to import packages
# import ecommerce.shipping
# from ecommerce import shipping
# # from ecommerce.shipping import calc_ship
# # print(ecommerce.shipping.calc_ship())
# shipping.calc_ship()


import random  # //build in module in python to generate random number

# for i in range(3):
#     # print(random.random())  # print random number
#     print(random.randint(10, 20))  # print range number between 10 to 20

# member = ['manjesh', 'singh', 'rahul', 'shailendra', 'saif', 'azam']

# leader = random.choice(member)  # choice to choose random value
# print(leader)

# ================================    example   =============================================


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())