import random

'''Write a program that generates 26 text files named
A.txt, B.txt, and so on up to Z.txt. To each file append
a random number between 1 and 100. Create a summary file
(summary.txt) that contains the name of the file and the
number in that file: A.txt: 67 B.txt: 12...Z.txt: 98'''


def generate_files_and_summary():
    data_dict = {}

    for letter in range(ord('A'), ord('Z')+1):
        file_name = chr(letter) + ".txt"
        random_number = random.randint(1, 100)
        data_dict[file_name] = random_number

        with open(file_name, "a") as file:
            file.write(str(random_number) + "\n")

    with open("summary.txt", "w") as summary_file:
        for file_name, number in data_dict.items():
            summary_file.write(f"{file_name}: {number}\n")

    # print("List of created files:")
    # for file_name, number in data_dict.items():
        # print(f"{file_name}: {number}")

    with open("summary.txt", "r") as summary_file:
        contents = summary_file.read()
        print("\nContents of summary.txt:")
        print(contents)

    print(len(data_dict), 'files have been created')


generate_files_and_summary()
