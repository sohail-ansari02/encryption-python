def toggle_bits(input_file_path, output_file_path):
    # Open the input file in binary mode and read its content
    with open(input_file_path, 'rb') as input_file:
        data = input_file.read()

    # Toggle each bit by using bitwise NOT (~) and masking with 0xFF
    toggled_data = bytes(~byte & 0xFF for byte in data)

    # Save the toggled data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(toggled_data)

# # Example usage:
# input_file = 'res_test.jpg'
# output_file = 'res_'+ input_file
# decrypt.toggle_bits(input_file, output_file)
