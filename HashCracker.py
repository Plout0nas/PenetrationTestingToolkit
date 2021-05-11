import hashlib

# hashType = (input('Enter the type of hash you want to bruteforce: '))
# filePath = str(input('Enter the path of the file to bruteforce: '))
# decryptHash = str(input('Enter the hash: '))


def hashcracker(filePath, hashType, decryptHash, label):

    with open(filePath, 'r') as file:
        for line in file.readlines():
            # Finding md5 type of hashed password
            if hashType == 'md5':
                hashObject = hashlib.md5(line.strip().encode())
                hashedWord = hashObject.hexdigest()
                if hashedWord == decryptHash:
                    print('Found MD5 password: ' + line.strip())
                    label.setText('Found MD5 password: ' + line.strip())
                    return
            # Finding sha1 type of hashed password
            if hashType == 'sha1':
                hashObject = hashlib.sha1(line.strip().encode())
                hashedWord = hashObject.hexdigest()
                if hashedWord == decryptHash:
                    print('Found SHA-1 password: ' + line.strip())
                    label.setText('Found SHA-1 password: ' + line.strip())
                    return
            # Finding sha256 type of hashed password
            if hashType == 'sha256':
                hashObject = hashlib.sha256(line.strip().encode())
                hashedWord = hashObject.hexdigest()
                if hashedWord == decryptHash:
                    print('Found SHA-256 password: ' + line.strip())
                    label.setText('Found SHA-256 password: ' + line.strip())
                    return

        print('Password is not in the file!')
        label.setText('Password is not in the file!')
