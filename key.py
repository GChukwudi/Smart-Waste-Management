import secrets

def generate_hex_secret_key(length=32):
    return secrets.token_hex(length)

# Generate a 32-character hexadecimal secret key
hex_secret_key = generate_hex_secret_key(32)
print("Generated Hexadecimal Secret Key:", hex_secret_key)
