import binascii


def hex_xor(hex_string_1, hex_string_2):
    hex_bytes_1 = bytearray([int(hex_string_1[i:i+2], 16) for i in range(0, len(hex_string_1), 2)])
    hex_bytes_2 = bytearray([int(hex_string_2[i:i+2], 16) for i in range(0, len(hex_string_2), 2)])
    xor_result = bytearray(a ^ b for a, b in zip(hex_bytes_1, hex_bytes_2))
    return binascii.hexlify(xor_result)