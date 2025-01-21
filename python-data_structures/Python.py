#!/usr/bin/python3
import os

files_content = {
    '0-square_matrix_simple.py': '''#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
''',

    '0-main.py': '''#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
''',

    '1-search_replace.py': '''#!/usr/bin/python3

def search_replace(my_list, search, replace):
''',

    '1-main.py' : '''#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
''',

    '2-uniq_add.py' : '''#!/usr/bin/python3
def uniq_add(my_list=[]):
''',

    '2-main.py' : '''#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
''',
    '3-common_elements.py' : '''#!/usr/bin/python3
def common_elements(set_1, set_2):
''',
    '3-main.py' : '''#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
''',
    '4-only_diff_elements.py' : '''#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
''',
    '4-main.py' : '''#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
''',
    '5-number_keys.py' : '''#!/usr/bin/python3
def number_keys(a_dictionary):
''',
    '5-main.py' : '''#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
''',
    '6-print_sorted_dictionary.py' : '''#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
''',
    '6-main.py' : '''#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
''',
    '7-update_dictionary.py' : '''#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
''',
    '7-main.py' : '''#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
''',
    '8-simple_delete.py' : '''#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
''',

    '8-main.py' : '''#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
''',
    '9-multiply_by_2.py' : '''#!/usr/bin/python3
def multiply_by_2(a_dictionary):
''',
    '9-main.py' : '''#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
''',
    '10-best_score.py' : '''#!/usr/bin/python3
def best_score(a_dictionary):
''',
    '10-main.py' : '''#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
''',
    '11-multiply_list_map.py' : '''#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
''',
    '11-main.py' : '''#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
''',
    '12-roman_to_int.py' : '''#!/usr/bin/python3
def roman_to_int(roman_string):
''',
    '12-main.py' : '''#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
''',
    '.gitignore' : '''*main.py
create_files.py
''',
'README.md' : '''Temporary readme''',
}


def create_files():
    for filename, content in files_content.items():
        with open(filename, 'w') as f:
            f.write(content)
        # Make executable only if not README.md or .gitignore
        if filename not in ['README.md', '.gitignore']:
            os.chmod(filename, 0o755)

if __name__ == "__main__":
    create_files()