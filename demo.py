#!/usr/bin/env python3
"""
Demonstration of Python imports from the README examples
"""

print("=== Basic OS Module Import Examples ===")

# Example 1: Import entire module
import os
print(f"os.name: {os.name}")

# Example 2: Import specific function
from os import name
print(f"name: {name}")

print("\n=== Absolute Import Examples ===")
print("Run these in Python REPL from the lib/ directory:")
print(">>> from absolute_package.package1 import module1")
print(">>> module1.function1()")
print(">>> from absolute_package.package2.subpackage1.module6 import function1")
print(">>> function1()")

print("\n=== Relative Import Examples ===")
print("Run this command from the lib/ directory:")
print("$ python -m relative_package.subpackage1.subpackage2.module2")