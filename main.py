import re
import string
import random


def generate_password(char_list, min_char_count, max_char_count):
    generated_password = ""

    password_len = random.choice(range(int(min_char_count), int(max_char_count)+1))

    for i in range(password_len):
        generated_password = generated_password + random.choice(char_list)

    print(generated_password)


def create_list(given_parameters_list, given_char_count_min, given_char_count_max):
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

    print("Generated List: " + str(char_list))

    generate_password(char_list, given_char_count_min, given_char_count_max)


def usr_input_check(given_input):
    if usrInput == "Exit" or "-Q" or "-Quit" or "4":
        print("See you soon")
        exit()

    if re.search("^-create ", given_input):
        given_command_list = given_input.split(" ")

        if len(given_command_list) != 4:
            print("Something is wrong about given parameters")
            print("Example usage: -create 1+2+3")
            exit()

        given_command = given_command_list[1]
        given_char_count_min = given_command_list[2]
        given_char_count_max = given_command_list[3]
        print(given_command_list)
        print(given_char_count_min)
        print(given_char_count_max)
        print(given_command)

        try:
            if given_char_count_min.isdigit() and given_char_count_max.isdigit():
                given_parameters_list = given_command.split("+")
                print(given_parameters_list)
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
                        print("Example usage: -create 1+2+3")
                        exit()

                create_list(given_parameters_list, given_char_count_min, given_char_count_max)
            else:
                print("Something is wrong about given parameters")
                print("Example usage: -create 1+2+3")
                exit()

        except():
            print("Something is wrong about given parameters")
            print("Example usage: -create 1+2+3")
            exit()

    else:
        print("Something is wrong about given command")
        print("Example usage: -create 1+2+3")

print("-----------Parameters-----------")
print("1 - Contains Special Chars")
print("2 - Contains UpperCase Letters")
print("3 - Contains LowerCase Letters")
print("4 - Exit")
print("--------------------------------")

print("\n-------------HELP---------------")
print("Usage: -create {Parameters} {Min Char Count} {Mix Char Count}")
print("\nExample usage: -create 1+2+3 15 25\n")
print("Example output: f];JODAfl]>wKGx@Lhan',")
print("--------------------------------\n")

usrInput = input("Waiting For Entry: ")

usrInput = usrInput.strip()

usr_input_check(usrInput)
