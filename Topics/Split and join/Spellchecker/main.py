dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
wrongs = []
sentence = input().split()
for word in sentence:
    if word not in dictionary:
        wrongs.append(word)
if len(wrongs) > 0:
    print('\n'.join(wrongs))
else:
    print('OK')