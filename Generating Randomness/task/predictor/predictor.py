import random

num = 100
balance = 1000
bin_list = ["000", "001", "010", "011", "100", "101", "110", "111"]
analysis_list = {x: [0, 0] for x in bin_list}


def input_data_for_analysis():
    all_str = []
    while len(all_str) < num:
        print('Print a random string containing 0 or 1:')
        print('')
        user_imp = input()

        all_str += [x for x in user_imp if x == '0' or x == '1']
        if (num - len(all_str)) <= 0:
            break
        print(f'The current data length is {len(all_str)}, {num - len(all_str)} symbols left')

    print(f"\nFinal data string:\n{''.join(all_str)}")
    return all_str


def generate_prediction(str_, len_str):
    global analysis_list
    generation = bin_list[random.randint(0, len(bin_list)-1)]
    generation = list(generation)
    for j in range(len_str - 3):
        last_3 = str_[j:j + 3]
        if analysis_list[last_3][0] >= analysis_list[last_3][1]:
            generation.append('0')
        else:
            generation.append('1')
    return ''.join(generation)


def compare_prediction(str1, str2):
    global balance
    n = len(str1) - 3
    r = len([j for j in range(3, len(str1)) if str1[j] == str2[j]])  # right
    w = n - r  # wrong
    per = round(100 / n * r, 2)
    balance = balance - r + w
    print(f'\nComputer guessed right {str(r)} out of {str(n)} symbols ({str(per)} %)')
    print(f'Your balance is now ${balance}')


# Input data for analysis
print('Please give AI some data to learn...')
print('The current data length is 0, 100 symbols left')
final_list = input_data_for_analysis()
# for test
# final_list = list('1010101101010101010011100101001010100101010000101000101010000100101011010001001000101011101000101010010100101')

# To analyse data
for i in range(len(final_list) - 3):
    text = final_list[i:i+4]
    analysis_list[''.join(text[0:3])][int(text[3])] += 1

# Game rules
print('''\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')

# Loop game
while True:
    print('\nPrint a random string containing 0 or 1:')
    test_str = input()
    if test_str == 'enough':
        print('Game over!')
        exit()
    test_list = ''.join([t for t in test_str if t == '0' or t == '1'])
    if len(test_list) <= 3:
        continue
    predict_list = generate_prediction(test_list, len(test_list))
    print('prediction: \n' + predict_list)
    compare_prediction(test_list, predict_list)
