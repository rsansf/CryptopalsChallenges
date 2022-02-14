import binascii


def single_hex_byte_hex(hex_string, single_hex_byte):
    hex_bytes = bytearray(int(hex_string[i:i + 2], 16) for i in range(0, len(hex_string), 2))
    xor_result = bytearray(a ^ bytes(single_hex_byte) for a in hex_bytes)
    return binascii.hexlify(xor_result)


def english_text_scoring_method(input_bytes):
    character_frequencies = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015,
                             'h': .06094,
                             'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507,
                             'p': .01929,
                             'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360,
                             'x': .00150,
                             'y': .01974, 'z': .00074, ' ': .13000}
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])
