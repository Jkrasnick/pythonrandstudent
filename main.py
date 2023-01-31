# This is a sample Python script.
from random import randint

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

students = ["Tyler", "Austin", "David", "Eric", "Jason", "Xinxin", "Conor", "Akira", "JD", "Aiden", "Kush", "Sydney",
            "Rohan", "Joe"]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def rand_student_generator():
    response = input("Press 1 to get a random student and 2 to exit: ")
    if response == "1":
        return students.pop(randint(0, len(students)))

    else:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(rand_student_generator())
    print(rand_student_generator())
    print(rand_student_generator())
    print(students);

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
