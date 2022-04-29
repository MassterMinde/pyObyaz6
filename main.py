# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(x):
    b = (x & 0o00000000000000000000110000000000) << 3
    c = (x & 0o00000000111111111111000000000000) << 3
    d = (x & 0o00000111000000000000000000000000) >> 14
    e =  x & 0o11111000000000000000000000000000
    a =  x & 0o00000000000000000000001111111111
    return hex(e | c | b | d | a)


print(main(0xc23595db))
