import hmac
import hashlib
import base64
import binascii

def generate_tsig_key(key_name, key_secret, algorithm='HMAC_MD5', key_file='TSIG.key', private_file='TSIG.private'):
    # Generate TSIG signature
    tsig_signature = hmac.new(key_secret.encode(), digestmod=hashlib.sha256).digest()

    # Base64 encode the TSIG signature
    tsig_base64 = base64.b64encode(tsig_signature).decode()

    # Prepare the TSIG key string
    tsig_key_string = f'{key_name} {algorithm} {tsig_base64}'

    # Write TSIG key to a file
    with open(key_file, 'w') as file:
        file.write(tsig_key_string)

    # Convert the TSIG secret to hexadecimal format
    tsig_hex = binascii.hexlify(key_secret.encode()).decode()

    # Write TSIG private file
    with open(private_file, 'w') as file:
        file.write(f'{key_name}:{algorithm}:{tsig_hex}')

    print(f'TSIG key file "{key_file}" and TSIG private file "{private_file}" generated successfully.')


# Example usage
key_name = 'mykey'
key_secret = 'mysecretkey'
generate_tsig_key(key_name, key_secret)
