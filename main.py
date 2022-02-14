from challenge1 import hex_to_base64
from challenge2 import hex_xor
if __name__ == "__main__":
    ''' CHALLENGE 1
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_base64(hex_string))
    '''
    hex_string_1 = "1c0111001f010100061a024b53535009181c"
    hex_string_2 = "686974207468652062756c6c277320657965"
    print(hex_xor(hex_string_1, hex_string_2))