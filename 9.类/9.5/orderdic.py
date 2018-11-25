"""记录顺序的词典"""
from collections import OrderedDict
term = OrderedDict()
term['object'] = 'for class'
term['function'] = 'operations'
term['repository'] = 'standard usage'
for key, value in term.items():
    print(key + ': ' + value)