# correct_data_coding_errors.py
# reads raw data file and writes clean data file with data coding errors corrected

def main():
    subdirectory = 'data'
    input_filename = 'raw_data.txt'
    output_filename = 'cleaned_data.txt'
    do_correct_data_coding_errors(subdirectory, input_filename, output_filename)


def do_correct_data_coding_errors(directory, infile_name, outfile_name):
    infile_full_name = directory + '/' + infile_name
    outfile_full_name = directory + '/' + outfile_name
    infile = open(infile_full_name, 'r', encoding='utf-8')
    outfile = open(outfile_full_name, 'w', encoding='utf-8')
    records_proccessed = 0

    for line in infile:
        line = line.strip()
        city_name, state_name, value = line.split(',')
        city_name = city_name.strip().title()
        state_name = state_name.strip().title()
        print(f'{city_name},{state_name},{value}', file=outfile)
        records_proccessed += 1
    infile.close()
    outfile.close()

    print(f'Input file: {infile_full_name}')
    print(f'Output file: {outfile_full_name}')
    print(f'{records_proccessed} records were processed.')


if __name__ == '__main__':
    main()

