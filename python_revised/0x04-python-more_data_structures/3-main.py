#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Python", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(set(sorted(c_set)))

