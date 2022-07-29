import re
import string
import random


def generate_password(char_list, min_char_count, max_char_count):
    generated_password = ""

    password_len = random.choice(range(int(min_char_count), int(max_char_count)+1))

    for i in range(password_len):
        generated_password = generated_password + random.choice(char_list)

    print(f"Generated Password: {generated_password}")


def create_list(given_parameters_list, given_char_count_min, given_char_count_max, password_count):
    char_list = []
    punctuation_added = False
    upper_case_added = False
    lower_case_added = False
    for member in given_parameters_list:

        if member == "1" and not punctuation_added:
            char_list = char_list + list(string.punctuation)
            punctuation_added = True
        if member == "2" and not upper_case_added:
            char_list = char_list + list(string.ascii_uppercase)
            upper_case_added = True
        if member == "3" and not lower_case_added:
            char_list = char_list + list(string.ascii_lowercase)
            lower_case_added = True

    random.shuffle(char_list)

    for i in range(int(password_count)):
        generate_password(char_list, given_char_count_min, given_char_count_max)


def usr_input_check(given_input):
    if given_input == "Exit" or given_input == "Quit" or given_input == "4" or given_input == "-q":
        print("See you soon")
        exit()

    if re.search("^-create ", given_input):
        given_command_list = given_input.split(" ")

        if len(given_command_list) != 5:
            if len(given_command_list) == 4:
                given_command_list.append("1")
            else:
                print("Something is wrong about given parameters")
                print("Example usage: -create 1+2+3 15 25")
                exit()

        given_command = given_command_list[1]
        given_char_count_min = given_command_list[2]
        given_char_count_max = given_command_list[3]
        given_password_count = given_command_list[4]

        try:
            if given_char_count_min.isdigit() and given_char_count_max.isdigit():
                given_parameters_list = given_command.split("+")
                for member in given_parameters_list:
                    member_match = False
                    if member == "1":
                        member_match = True
                    elif member == "2":
                        member_match = True
                    elif member == "3":
                        member_match = True

                    if not member_match:
                        print("Something is wrong about given parameters")
                        print("Example usage: -create 1+2+3 15 25")
                        exit()

                create_list(given_parameters_list, given_char_count_min, given_char_count_max, given_password_count)
            else:
                print("Something is wrong about given parameters")
                print("Example usage: -create 1+2+3 15 25")
                exit()

        except():
            print("Something is wrong about given parameters")
            print("Example usage: -create 1+2+3 15 25")
            exit()

    else:
        print("Something is wrong about given command")
        print("Example usage: -create 1+2+3 15 25")

print("-----------Parameters-----------")
print("1 - Contains Special Chars")
print("2 - Contains UpperCase Letters")
print("3 - Contains LowerCase Letters")
print("4 - Exit")
print("--------------------------------")

print("\n-------------HELP---------------")
print("Usage: -create {Parameters} {Min Char Count} {Mix Char Count} {Password Count}")
print("\nExample usage: -create 1+2+3 15 25 1\n")
print("Example output: f];JODAfl]>wKGx@Lhan',")
print("--------------------------------")

while True:
    usrInput = input("\nWaiting For Entry: ")

    usrInput = usrInput.strip()

    usr_input_check(usrInput)



