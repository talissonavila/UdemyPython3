import re
from pprint import pprint


regex_for_valid_numbers = re.compile(r'^[+-]?\d+(?:\.\d+)?$')

string = '+0.0'

pprint(re.findall(regex_for_valid_numbers, string))
