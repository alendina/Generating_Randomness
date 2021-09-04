start_list = input().split()
new_list = [w for w in start_list if w.endswith('s')]
print('_'.join(new_list))