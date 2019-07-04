from pathlib import Path


# absolute path                 #ex:existing in our harddisk
# ie= /user/local/bin
# relative path                 #ex:ecommerce

# path = Path("ecommerce")
# print(path.exists())                     #check the dir  inside is available or not

# path = Path("emails")
# # print(path.mkdir())      # to make the new dir inside dir
# print(path.rmdir())      # to remove the dir

path = Path()

# for file in path.glob('*.py'):                    # to print all py file  for current dir
#     print(file)
for file in path.glob('*'):                         # all print
    print(file)
