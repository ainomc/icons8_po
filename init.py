# -*- coding: utf-8 -*-
"""Initialization module.
    Parsed arguments from command line, like : '-login po_tests@gmail.com
    -password 123 -server https://demo.icons8.com/'
    Write this data to the param.json
    And run tests
    """

import json
import os
import glob
import argparse
from sys import platform

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-login', '--login', nargs='+', type=str)
parser.add_argument('-password', '--password', nargs='+', type=str)
parser.add_argument('-server', '--server', nargs='+', type=str)
args = parser.parse_args()

# Write arguments to the param.json
with open('param.json', 'r+') as outfile:
    json_data = json.load(outfile)
    json_data['login'] = args.login[0]
    json_data['password'] = args.password[0]
    json_data['server'] = args.server[0] + 'icon/'
    outfile.seek(0)
    outfile.write(json.dumps(json_data))
    outfile.truncate()

# Find all path to tests_* files and create list
list_test_fies = glob.glob(os.path.join(os.getcwd(), 'tests', 'tests_*'))

# Convert path to universal path what can be used in linux
for file_num in range(len(list_test_fies)):
    list_test_fies[file_num] = \
        os.path.join(os.getcwd(), 'tests', list_test_fies[file_num])

# Convert list to one string with spaces (' ') between each path
str_list = " ".join(str(x) for x in list_test_fies)

# If you need start only one test file change str_list on like this:
# str_list = os.path.join(os.getcwd(), 'tests', 'tests_icons_mobile_page.py')

# Run tests with all tests files
if "win" in platform:
    # os.system(r'python -m pytest -v tests\tests_landing_page.py -s -l')
    os.system(r'python -m pytest -v %s -s -l --html=html_report/report.html' % str_list)
    # tests_icons_mobile_page.py
elif "linux" in platform:
    os.system(r'python -m pytest -v %s -s -l '
              r'--junitxml=/var/lib/jenkins/workspace/icons8selenium_po_tests/report/junitxml --html=html_report/report.html' % str_list)
