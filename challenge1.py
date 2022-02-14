import base64


def hex_to_base64(hex_string):
    # 2 hex characters equal to 1 byte.
    hex_bytes = bytearray([int(hex_string[i:i + 2], 16) for i in range(0, len(hex_string), 2)])
    return base64.b64encode(hex_bytes)
