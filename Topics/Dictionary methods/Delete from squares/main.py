squares = {1: 1, 3: 9, 4: 16, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}
# num = int(input('Insert num:'))
# if num not in squares.keys():
#     print('There is no such key')
# else:
#     print(squares.pop(num))
# print(squares)

print(squares.pop(int(input('Insert num: ')), 'There is no such key'))
print(squares)
