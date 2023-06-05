import sys

def encrypt_file(input_file, output_file, secret_key):
    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        for line in file_in:
            encrypted_line = ""
            for char in line:
                # Encrypt each character by shifting it by the secret key
                if char.isalpha():
                    encrypted_char = chr((ord(char) - ord('a') + secret_key) % 26 + ord('a'))
                    encrypted_line += encrypted_char
                else:
                    encrypted_line += char
            file_out.write(encrypted_line)

# Get the file names and secret key from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
secret_key = int(sys.argv[3])

# Encrypt the file
encrypt_file(input_file, output_file, secret_key)