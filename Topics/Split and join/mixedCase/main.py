list_ = input().split()
list_ = [word.capitalize() for word in list_]
list_[0] = list_[0].lower()
print(''.join(list_))
