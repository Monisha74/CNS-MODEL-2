import hashlib

stored_hashes = {
    "5c97a12eae8f6747c5d1c9d2a9f89e31421bdc45",  
    "d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2"   
}

paper = input("Enter your research paper text: ")

paper_hash = hashlib.sha1(paper.encode()).hexdigest()

print("\nSHA-1 hash of the research paper:")
print(paper_hash)

if paper_hash in stored_hashes:
    print("  Duplicate detected! This paper has already been submitted.")
else:
    print(" Original submission. No duplication found.")
