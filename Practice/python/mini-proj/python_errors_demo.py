#!/usr/bin/env python3
"""
python_errors_demo.py

Demonstrates common Python exceptions and their handling.

Usage:
    python python_errors_demo.py --error ZeroDivisionError
    python python_errors_demo.py --error all
"""

import argparse
import logging
import importlib

# Configure simple logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

def demo_zero_division():
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        logging.info("✅ Caught ZeroDivisionError: %s", e)

def demo_index_error():
    try:
        lst = []
        _ = lst[1]
    except IndexError as e:
        logging.info("✅ Caught IndexError: %s", e)

def demo_key_error():
    try:
        d = {}
        _ = d['missing']
    except KeyError as e:
        logging.info("✅ Caught KeyError: %s", e)

def demo_type_error():
    try:
        _ = '2' + 2
    except TypeError as e:
        logging.info("✅ Caught TypeError: %s", e)

def demo_value_error():
    try:
        _ = int('not a number')
    except ValueError as e:
        logging.info("✅ Caught ValueError: %s", e)

def demo_attribute_error():
    try:
        obj = 10
        _ = obj.nonexistent_method()
    except AttributeError as e:
        logging.info("✅ Caught AttributeError: %s", e)

def demo_name_error():
    try:
        _ = undefined_variable  # noqa
    except NameError as e:
        logging.info("✅ Caught NameError: %s", e)

def demo_file_not_found_error():
    try:
        with open('no_such_file.txt') as f:
            pass
    except FileNotFoundError as e:
        logging.info("✅ Caught FileNotFoundError: %s", e)

def demo_import_error():
    try:
        importlib.import_module('some_nonexistent_module')
    except ImportError as e:
        logging.info("✅ Caught ImportError: %s", e)

def demo_runtime_error():
    try:
        raise RuntimeError("Simulated runtime issue")
    except RuntimeError as e:
        logging.info("✅ Caught RuntimeError: %s", e)

ERROR_DEMOS = {
    'ZeroDivisionError': demo_zero_division,
    'IndexError': demo_index_error,
    'KeyError': demo_key_error,
    'TypeError': demo_type_error,
    'ValueError': demo_value_error,
    'AttributeError': demo_attribute_error,
    'NameError': demo_name_error,
    'FileNotFoundError': demo_file_not_found_error,
    'ImportError': demo_import_error,
    'RuntimeError': demo_runtime_error,
}

def main():
    parser = argparse.ArgumentParser(description="Demonstrate Python exceptions and handling.")
    parser.add_argument(
        '--error',
        choices=list(ERROR_DEMOS.keys()) + ['all'],
        default='all',
        help="Which error demo to run (default: all)"
    )
    args = parser.parse_args()

    to_run = ERROR_DEMOS.keys() if args.error == 'all' else [args.error]
    for err_name in to_run:
        logging.info(f"\n--- Demonstrating {err_name} ---")
        ERROR_DEMOS[err_name]()

if __name__ == "__main__":
    main()
