
def decimal_to_binary(decimal_num, num_bits):
    binary_num = bin(decimal_num & int("1 " *num_bits, 2))[2:]
    return binary_num.zfill(num_bits)

def twos_complement(binary_num):
    inverted_num = ""
    for bit in binary_num:
        inverted_num += "0" if bit == "1" else "1"

    carry = 1
    twos_comp = ""
    for bit in reversed(inverted_num):
        if bit == "0" and carry == 1:
            twos_comp += "1"
            carry = 0
        elif bit == "1" and carry == 1:
            twos_comp += "0"
        else:
            twos_comp += bit

    return twos_comp[::-1]

decimal_num = int(input("Enter a decimal number: "))
num_bits = int(input("Enter the number of bits: "))

if decimal_num >= 0:
    binary_rep = decimal_to_binary(decimal_num, num_bits)
    print("Binary representation:", binary_rep)
    print("Negative binary representation (Two's complement):", twos_complement(binary_rep))
else:
    print("Please enter a non-negative decimal number.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/