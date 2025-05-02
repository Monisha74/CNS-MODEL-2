from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

blockchain = []

voter_keys = {}

def register_voter(voter_id):
    key = DSA.generate(2048)
    voter_keys[voter_id] = {
        'private': key,
        'public': key.publickey()
    }
    print(f" Voter '{voter_id}' registered successfully.")

def sign_vote(voter_id, vote_data):
    if voter_id not in voter_keys:
        print(" Voter not registered.")
        return None
    
    private_key = voter_keys[voter_id]['private']
    hash_obj = SHA256.new(vote_data.encode())
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    print(f" Vote signed by voter '{voter_id}'.")
    return signature

def verify_and_store_vote(voter_id, vote_data, signature):
    if voter_id not in voter_keys:
        print(" Unknown voter.")
        return

    public_key = voter_keys[voter_id]['public']
    hash_obj = SHA256.new(vote_data.encode())
    verifier = DSS.new(public_key, 'fips-186-3')

    try:
        verifier.verify(hash_obj, signature)
        print(f" Vote from '{voter_id}' is verified and recorded.")
        blockchain.append({
            'voter_id': voter_id,
            'vote_data': vote_data
        })
    except ValueError:
        print(" Vote verification failed! Possible tampering detected.")

register_voter("voter1")
register_voter("voter2")

vote1 = input("\nVoter1, enter your vote (e.g., 'Candidate A'): ")
signature1 = sign_vote("voter1", vote1)

vote2 = input("\nVoter2, enter your vote (e.g., 'Candidate B'): ")
signature2 = sign_vote("voter2", vote2)

print("\n--- Verifying and Recording Votes ---")
verify_and_store_vote("voter1", vote1, signature1)
verify_and_store_vote("voter2", vote2, signature2)

print("\n--- Blockchain (Vote Ledger) ---")
for block in blockchain:
    print(block)
