#Password Auidit

import re

def password_audit(password):
    if len(password):
        if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[_@$]", password):
            print("Valid Password")
        else:
            print("Invalid Password")

password = input("Enter Password:")
password_audit(password)

import argparse

parser = argparse.ArgumentParser(description="Password Audit")
parser.add_argument("password", help="Password to audit")

args = parser.parse_args()

password = args.password

password_audit(password)

import pathlib

default_path = pathlib.Path("password_audit.txt")

default_path.write_text(password)

print(f"Password saved to {default_path.resolve()}")

outpath = input("Enter the path where you want to save the password:")

pathlib.Path(outpath).write_text(password)

print(f"Password saved to {pathlib.Path(outpath).resolve()}")

import sys

if len(sys.argv) == 1:
    password = input("Enter your password: ")
else:
    parser = argparse.ArgumentParser(description="Password Audit")
    parser.add_argument("password", help="Password to audit")
    args = parser.parse_args()
    password = args.password

password_audit(password)

import getpass

password = getpass.getpass("Enter your password:")

password_audit(password)
