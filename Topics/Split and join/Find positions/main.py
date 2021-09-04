sequence = input().split()
num = input()
total = [str(i) for i in range(len(sequence)) if sequence[i] == num]
if len(total) > 0:
    print(' '.join(total))
else:
    print('not found')
