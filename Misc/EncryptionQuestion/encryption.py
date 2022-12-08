# function to encrypt the plaintext
def encrypt(plaintext,key):
    # list to store the cipher/encrypted text
    ciphertext = []
    for i in plaintext:
        # replace the char of plain text to char in the key
        ciphertext.append(key[i])
    # returns the list of encrypted text
    return ciphertext

# function to decrypt the ciphertext
def decrypt(ciphertext,key):
    # list to store the plain text
    plaintext = []
    for i in ciphertext:
        # replace the char in ciphertext to plain text with the help of key
        plaintext.append(key.index(i))
    # return the list of the plaintext
    return plaintext

# function to write the encrypted/decrypted text in the "ciphertext"/"plain_text1" file 
def write_file(filename,message):
    # open the file in write binary mode 
    with open(filename,'wb') as f:
        # write the numeric data into file in binary format 
        f.write(bytes(message))

# function to read the files
def read_file(filename):
    # open the file in read binary mode 
    with open(filename,'rb') as f:
        # return the data from the given "filename"
        return (f.read())

# function to read the key
def read_key(filename):
    # list to store the key
    message = []
    # open the file in 'read binary' mode to read  
    with open(filename,'rb') as f:
        for i in f.read():
            message.append(i)
    return message
    

# To test the code
def test_encryption():
    # open the key file and read the data and assigned it to "key" variable
    key = read_key('key')
    # read the plain text file and assigned it to "plaintext" variable
    plaintext = read_file('plain_text.jpeg')
    # Encrypt the Plaintext and assigned it to "ciphertext" variable
    ciphertext = encrypt(plaintext,key)
    # write that "ciphertext" variable into the file named "ciphertext"
    write_file('ciphertext',ciphertext)
    # Decrypt the file with the help of key and assigned it to "plaintext1" variable
    plaintext1 = decrypt(ciphertext,key)
    # write the decrypted text into the "plain_text1" file
    write_file('plain_text1.jpeg',plaintext1)
    # if plain_text == plain_text1 then encryption and decryption is successful

test_encryption()
