from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

private_key = DSA.generate(2048)
public_key = private_key.publickey()

document = input("Enter the legal document content: ")

hash_obj = SHA256.new(document.encode())

signer = DSS.new(private_key, 'fips-186-3')
signature = signer.sign(hash_obj)

print("\n Document has been signed digitally.")

received_hash = SHA256.new(document.encode())
verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(received_hash, signature)
    print(" Signature is valid. Document is authentic and unchanged.")
except ValueError:
    print(" Signature verification failed. Document may be forged or modified.")
