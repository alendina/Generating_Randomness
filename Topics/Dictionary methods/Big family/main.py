# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())
big_family = first_family
big_family.update(second_family)
print(big_family)
# Work with the 'first_family' and 'second_family' and create a new dictionary
