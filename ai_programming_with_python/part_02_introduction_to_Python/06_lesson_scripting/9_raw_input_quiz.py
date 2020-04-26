# get and process input for a list of names
names = input('Enter names separated by commas: ')
# get and process input for a list of the number of assignments
assignments = input('Enter remaining assignments separated by commas: ')
# get and process input for a list of grades
grades = input('Enter current grades separated by commas: ')

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


namesList = names.split(',')
assignmentsList = assignments.split(',')
gradesList = grades.split(',')

for item in zip(namesList, assignmentsList, gradesList):
    print(message.format(item[0], item[1], item[2],
                         int(item[2]) + 2 * int(item[1])))
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
