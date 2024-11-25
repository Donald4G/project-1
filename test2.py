#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#flat = [num for row in matrix for num in row]
#print(matrix)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#transpose = [[row[i] for row in matrix] for i in range(3)]
#print(transpose)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#parity = ['Even' if x % 2 == 0 else 'Odd' for x in range(10)]
#print(parity)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()