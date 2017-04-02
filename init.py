# -*- coding: utf-8 -*-
import json
import os
import glob
import argparse
from sys import platform

#runner demo - python init.py -login ainomc@gmail.com -password 123 -server https://demo.icons8.com/

parser = argparse.ArgumentParser()
parser.add_argument('-login', '--login', nargs='+', type=str)
parser.add_argument('-password', '--password', nargs='+', type=str)
parser.add_argument('-server', '--server', nargs='+', type=str)
args = parser.parse_args()


with open('param.json', 'r+') as outfile:
    json_data = json.load(outfile)
    json_data['login'] = args.login[0]
    json_data['password'] = args.password[0]
    json_data['server'] = args.server[0]
    outfile.seek(0)
    outfile.write(json.dumps(json_data))
    outfile.truncate()

list_test_fies = glob.glob(os.path.join(os.getcwd(), 'tests', 'tests_*')) # find all tests files
for file_num in range(len(list_test_fies)):
    list_test_fies[file_num] = os.path.join(os.getcwd(), 'tests', list_test_fies[file_num])

str_list = " ".join(str(x) for x in list_test_fies) # convert list to string
str_list = os.path.join(os.getcwd(), 'tests', 'tests_sleeklogos_page.py')
#str_list = os.path.join(os.getcwd(), 'tests', 'tests_iconpharm_page.py')
#str_list = os.path.join(os.getcwd(), 'tests', 'tests_landing_page.py')
if "win" in platform:
    os.system(r'python -m pytest -v %s -s --showlocals' % str_list)
elif "linux" in platform:
    os.system(r'python -m pytest -v %s -s --showlocals --junitxml=/var/lib/jenkins/workspace/icons8selenium_po_tests/xml/junitxml' % str_list)