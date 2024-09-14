import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

dictionary = open( 'dictionary.txt', 'r').read() # I have just opened the file
dictionary_as_a_list = dictionary.split("\n") # Here i have just converted it into a list

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check(dictionary_as_a_list):
    for i in range(1,65537):
        user_pw = dictionary_as_a_list[i] # Here I passed the list as the password
        user_pw_hash = hash_pw(user_pw)
    

    #user_pw = input("Please enter correct password for flag: ")
    #user_pw_hash = hash_pw(user_pw)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        continue
    #print("That password is incorrect")
# Syntax of strip : <variable>.strip()
#This will remove the whitespaces from the hash


level_5_pw_check(dictionary_as_a_list)

