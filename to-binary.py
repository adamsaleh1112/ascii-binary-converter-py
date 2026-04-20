import struct

input_file = "numbers.txt"
output_file = "numbers.bin"

# read
with open(input_file, 'r') as f:
    numbers = [int(line.strip()) for line in f]
binary_data = struct.pack(f'{len(numbers)}i', *numbers)
# write
with open(output_file, 'wb') as f:
    f.write(binary_data)

print("Done")
