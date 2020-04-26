# Write your code here
flowers = {}

# HINT: create a dictionary from flowers.txt
with open('flowers.txt') as f:
    for line in f:
        flowers[line.split(":")[0]] = line.split(':')[1][:-1]

# HINT: create a function to ask for user's first and last name


def get_full_name():
    full_name = input('Enter your first name and last name: ')
    return full_name


def main():
    # print the desired output
    first_name, last_name = get_full_name().split(' ')
    print(first_name+flowers.get(first_name[0]))


if(__name__ == '__main__'):
    main()
