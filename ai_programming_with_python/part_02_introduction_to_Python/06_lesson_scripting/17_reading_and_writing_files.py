with open('new_file.txt', 'r') as f:
    file_data = f.read()
    print(file_data)

f = open('some_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()


f = open('new_file.txt', 'w')
f.write('Writing contents to a file')
f.close()
