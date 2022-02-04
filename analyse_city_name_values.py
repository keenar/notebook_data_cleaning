# analyze_city_name_values.py
# lists all unique city name values from input file and count of each


def main():
    subdirectory = 'data'
    input_filename = 'raw_data.txt'
    do_analyse_city_name_values(subdirectory, input_filename)


def do_analyse_city_name_values(directory, filename):
    path_and_filename = directory + '/' + filename
    with open(path_and_filename, 'r', encoding='utf-8') as infile:

        city_names = {}

        for line in infile:
            city_name, state_name, value_as_string = line.strip().split(',')
            city_names[city_name] = city_names.get(city_name, 0) + 1

    infile.close()

    key_values = list(city_names.keys())
    key_values.sort()
    for key_value in key_values:
        print(f'{key_value}: {city_names[key_value]}')


if __name__ == '__main__':
    main()
