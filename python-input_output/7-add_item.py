#!/usr/bin/python3
# 7-add_item.py
# Travis Adamson
"""Adds arguments to existing list and saves to json file"""
import sys
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

try:
    new_list = load_from_json_file("add_item.json")
except FileNotFoundError as fnf:
    new_list = []
new_list.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
