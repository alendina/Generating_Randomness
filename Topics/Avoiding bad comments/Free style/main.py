import os

file_name = input("Please write the name of the file to work with:\n")

if os.path.exists(file_name):
    file = open(file_name)
    content = file.read()
    file.close()

    new_content = preprocess(content)  # the previously defined function

    new_file = open(file_name + '_preprocessed.txt', 'w')
    new_file.write(new_content)
    new_file.close()

    print("All done!")

else:
    print("The file you entered does not exist!")