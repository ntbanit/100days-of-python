# read all lines from a file

def read_file(file_path):
    result_lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            # if at least 4 characters and all is lower case
            if len(line) >= 10 and line.islower():
                result_lines.append(line)
    return result_lines
result_lines = read_file('test_data_input.txt')
# write result_lines to a new file
with open('test_data_output.txt', 'w') as file:
    for line in result_lines:
        file.write(f'{line}\n')