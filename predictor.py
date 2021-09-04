import random

bin_list = ["000", "001", "010", "011", "100", "101", "110", "111"]
num = 100


def input_data():
    all_str = []
    while len(all_str) < num:
        print('Print a random string containing 0 or 1:')
        print('')
        str_ = input()

        all_str += [a for a in str_ if a == '0' or a == '1']
        if (num - len(all_str)) <= 0:
            break
        print(f'The current data length is {len(all_str)}, {num - len(all_str)} symbols left')

    print(f"\nFinal data string:\n{''.join(all_str)}")
    return all_str


def generate_prediction(len_str):
    global analysis_list
    generation = bin_list[random.randint(0, len(bin_list)-1)]
    # generation = '110' # test
    generation = list(generation)
    # print(generation)
    if len_str > 3:
        for _ in range(len_str-3):
            # last_3 = str(generation[-3]) + str(generation[-2]) + str(generation[-1])
            last_3 = ''.join(generation[-3:])

            # --- test 100101010010101001111010101001111101010
            # protection against sequence repetitions
            # if _ >= 1:
            #     if ''.join(generation[-5:]) == '01010' or ''.join(generation[-5:]) == '10101' \
            #             or ''.join(generation[-4:]) == '1111' or ''.join(generation[-4:]) == '0000':
            #         generation.append(str(random.randint(0, 1)))
            #         # print(generation[-1])
            #         continue
            # # ---

            if dict_data[last_3][0] >= dict_data[last_3][1]:
                generation.append('0')
            else:
                generation.append('1')
    return ''.join(generation)


def generate_prediction_random(len_str):
    global analysis_list
    generation = bin_list[random.randint(0, len(bin_list) - 1)]
    generation = list(generation)

    if len_str > 3:
        for _ in range(len_str - 3):
            generation.append(str(random.randint(0, 1)))
    return ''.join(generation)


def compare_prediction(str1, str2):
    n = len(str1)
    s = [j for j in range(3, len(str1) - 1) if str1[j] != str2[j]]
    # print(s)
    k = len(s)
    per = round(100 / n * k, 2)
    print(f'\nComputer guessed right {str(k)} out of {str(n - 3)} symbols ({str(per)} %)')


# input_list = '1010101101010101010011100101001010100101010000101000101010000100101011010001001000101011101000101010010100101'
#               1010101101010101010011100101001010100101010000101000101010000100101011010001001000101011101000101010010100101
# input_list = list(input_list)

input_list = input_data()

final_list = [input_list[symbol:symbol+4] for symbol in range(0, len(input_list) - 3)]
# print(final_list)
analysis_list = dict.fromkeys(bin_list, (0, 0))
for d in final_list:
    key = ''.join(d[0:3])
    x, y = analysis_list[key]

    if d[3] == '0':
        x += 1
    elif d[3] == '1':
        y += 1
    analysis_list[key] = (x, y)

# -- print analysis
# for i in bin_list:
#     print(f'{i}: {dict_data[i][0]}, {dict_data[i][1]}')
# --

print('\nPlease enter a test string containing 0 or 1:\n')
user_str = input()  # '0110001010100101' #  # test

# print(user_str) # test
predict_str = generate_prediction(len(user_str))
print('prediction: \n' + predict_str)
compare_prediction(user_str, predict_str)

# -- random prediction sequence
# predict_str = generate_prediction_random(len(user_str))
# print('prediction: \n' + predict_str)
# compare_prediction(user_str, predict_str)
