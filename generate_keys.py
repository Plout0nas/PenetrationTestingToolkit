from Crypto.PublicKey import RSA
from Crypto import Random

# generate RSA keys for encryption and decryption both public and private
# keep the private key hidden and use the public to encrypt
key = RSA.generate(bits=2048, randfunc=Random.new().read)

# save the private key
with open('private_key.pem', 'wb') as fout:
	fout.write(key.export_key())

# save the public key
with open('public_key.pem', 'wb') as fout:
	fout.write(key.publickey().export_key())
