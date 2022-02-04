# analyse_state_name_values
# list all unique state name values and count of each

def main():
    subdirectory = 'data'
    input_filename = 'raw_data.txt'
    do_analyse_state_name_values(subdirectory, input_filename)


def do_analyse_state_name_values(directory, filename):
    path_and_filename = directory + '/' + filename
    with open(path_and_filename, 'r', encoding='utf-8') as infile:
        state_names = {}

        for line in infile:
            city_name, state_name, value_as_string = line.strip().split(',')
            state_names[state_name] = state_names.get(state_name, 0) + 1

        infile.close()

        key_values = list(state_names.keys())
        key_values.sort()
        for key_value in key_values:
            print(f'{key_value}: {state_names[key_value]}')


if __name__ == '__main__':
    main()
