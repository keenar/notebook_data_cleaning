# analyse_employee.data.py
# test program

subdirectory = 'data'
input_filename = 'grades.txt'
path_and_filename = subdirectory + '/' + input_filename

with open(path_and_filename, 'r') as data_file:
    for line in data_file:
        data = line.split()
        print(data)

with open(path_and_filename, 'r') as file:
    for line in file:
        name, grade, age = line.strip().split(',')
        print(name)

