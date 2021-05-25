#!/usr/bin/env python
"""This script add in 'classname' attribute of Junit test report branch from
$QA_CHANGE environment variable.
"""
from __future__ import print_function
import fnmatch
import os
import sys
import xml.etree.ElementTree as ET


def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        results.extend(
            os.path.join(base, f) for f in
            fnmatch.filter(files, pattern))
    return results


def add_branch(element, branch):
    name = element.get('classname')
    if '.' in name:
        name, _, restpart = name.partition('.')
        func_name = element.get('name')
        element.set('name', "{0}.{1}".format(restpart, func_name))
    element.set('classname', "{0}.{1}".format(branch, name))
    print(" " * 5, element.get('classname'), element.get('name'))


def process_elements(element, branch):
    for child in element:
        if child.tag == 'testcase':
            add_branch(child, branch)
        else:
            process_elements(child, branch)


def main(path, branch):
    print(
        "Start looking for reports in '{}' to setup branch '{}'".format(
            path, branch))
    print(os.path.join(path, '*.xml'))
    for report in recursive_glob(path, '*.xml'):
        print(" -> ", report)
        xml = ET.parse(open(report, 'r'))
        process_elements(xml.getroot(), branch)
        xml.write(open(report, 'wb'))


if __name__ == "__main__":
    print("Started with args:", " ".join(sys.argv[1:]))
    if len(sys.argv) > 2:
        path = sys.argv[1]
        branch = sys.argv[2]
    else:
        sys.exit('Usage: junitxml_add_branch.py artifacts branch_name')
    if branch.startswith('refs'):
        branch = 'change_{}'.format(branch.split('/')[3])
    elif not branch:  # empty
        branch = "empty"
    else:
        branch = branch.replace('.', '_').replace('-', '_')
    main(path, branch)
