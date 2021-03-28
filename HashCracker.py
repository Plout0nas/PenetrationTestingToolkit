import hashlib

hashType = (input('Enter the type of hash you want to bruteforce: '))
filePath = str(input('Enter the path of the file to bruteforce: '))
decryptHash = str(input('Enter the hash: '))


with open(filePath, 'r') as file:
    for line in file.readlines():
        # Finding md5 type of hashed password
        if hashType == 'md5':
            hashObject = hashlib.md5(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == decryptHash:
                print('Found MD5 password: ' + line.strip())
                exit(0)
        # Finding sha1 type of hashed password
        if hashType == 'sha1':
            hashObject = hashlib.sha1(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == decryptHash:
                print('Found SHA-1 password: ' + line.strip())
                exit(0)
        # Finding sha256 type of hashed password
        if hashType == 'sha256':
            hashObject = hashlib.sha256(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == decryptHash:
                print('Found SHA-256 password: ' + line.strip())
                exit(0)

    print('Password is not in the file!')
