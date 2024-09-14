#! /usr/bin/python
import binascii

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str)
    return ascii_str

hex_input = '0x70'
ascii_output = hex_to_ascii(hex_input)

print(format(ascii_output))
