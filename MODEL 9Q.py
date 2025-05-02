from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key_store = {}

def register_user(username):
    key = DSA.generate(2048)
    key_store[username] = {
        'private': key,
        'public': key.publickey()
    }
    print(f"User '{username}' registered with key pair.")

def sign_document(username, document):
    if username not in key_store:
        print(" User not found.")
        return None

    private_key = key_store[username]['private']
    hash_obj = SHA256.new(document.encode())
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    print(f" Document signed by '{username}'.")
    return signature

def verify_document(username, document, signature):
    if username not in key_store:
        print(" User not found.")
        return

    public_key = key_store[username]['public']
    hash_obj = SHA256.new(document.encode())
    verifier = DSS.new(public_key, 'fips-186-3')

    try:
        verifier.verify(hash_obj, signature)
        print(f" Document from '{username}' is authentic and unaltered.")
    except ValueError:
        print(f" Verification failed! Document from '{username}' may be forged or altered.")

register_user("alice")
register_user("bob")

alice_doc = input("\nAlice, enter your form submission: ")
alice_signature = sign_document("alice", alice_doc)

bob_doc = input("\nBob, enter your form submission: ")
bob_signature = sign_document("bob", bob_doc)

print("\n--- Admin Verifying Submissions ---")
verify_document("alice", alice_doc, alice_signature)
verify_document("bob", bob_doc, bob_signature)
