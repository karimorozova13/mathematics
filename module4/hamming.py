import numpy as np
from functools import reduce

def find_error(hamming_code,p):
    m = len(hamming_code)
    idx = 0
 
    for i in range(p):
        val = 0
        for j in range(1, m + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(hamming_code[-1 * j])
 
        idx += val*(10**i)

    return int(str(idx), 2)

    

def fix_error(bits, error_idx):
    bits = list(bits)
    bits[error_idx] = '1' if bits[error_idx] == '0' else '0'

    return ''.join(bits)

def remove_parity_bits(arr,p):
    m = len(arr)
    k = 0
    result = []

    for j in map(lambda x: 2**x, range(0, p-1)):
        result += arr[k+1:j]
        k = j

    result += arr[k+1::]
      
    return "".join(result)




def text_from_bits(bits, encoding='ascii'):
    print(bits)
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "little").decode(encoding) or "\0"


msg ='010011111010001110010101111001001100000011100100110010101110110001101111001000000111010001101111011011100010000001110011001001111011101000110100100100000011101000111010101000010001000010110001001101111011010100010000001100100011011010110111101000111'
msg2 = '10101111001000110100100110000101111000000100000011101000111100000110010101101110001000000110100101110101011101000110111001010110100101111011110010110110000101110011101000010111100101111001110100111001101110000011101000111010001101000'

test = msg
p = 0
while 2 ** p <= len(test) + p + 1:
    p += 1

idx = find_error(test,p)
print(idx,'idx');
fixed_msg = fix_error(test, idx)
removed_msg = remove_parity_bits(fixed_msg,p)
decoded_msg = text_from_bits(removed_msg)

print(decoded_msg, 'decoded_msg')