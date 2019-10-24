import sys

def DEBUG(to_print):
    sys.stderr.write(str(to_print))

def is_voyelle(l):
    end_letter = ['a','e','i','o','u','y']
    return l in end_letter

