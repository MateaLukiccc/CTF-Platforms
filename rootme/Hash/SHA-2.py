#deleting non hex character k from hash and using hashes.com we get the password: 4dM1n

import hashlib

print(hashlib.sha1("4dM1n".encode()).hexdigest())