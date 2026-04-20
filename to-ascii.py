import struct

input_file = "numbers.bin"
output_file = "restored_numbers.txt"

#read
with open(input_file, 'rb') as f:
    binary_data = f.read()
num_integers = len(binary_data) // 4
numbers = struct.unpack(f'{num_integers}i', binary_data)

# write
with open(output_file, 'w') as f:
    for num in numbers:
        f.write(f"{num}\n")

print("Done")
