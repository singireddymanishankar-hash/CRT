import hashlib

STORED_HASH = "e0bebd22819993425814866b62701e2919ea26f1370499c1037b53b9d49c2c8a"

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

for i in range(3):
    p2 = input("Enter password: ")
    if _hash_password(p2) == STORED_HASH:
        print("login successful")
        break
else:
    print("login failed")