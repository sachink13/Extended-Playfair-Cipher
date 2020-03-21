import string
import itertools

#divide plaintext to groups of 2
def chunker(seq,size):
    it = iter(seq)

    while True:
        chunk = tuple(itertools.islice(it,size))
        if not chunk:
            return
        yield chunk

#clean the plaintext,that is add X between 2 consequtive same letters/numbers
def prepare_input(dirty):
    
    dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters or int(c) in range(10)])
    clean = ""
        
    if len(dirty)<2:
        return dirty

    for i in range(len(dirty)-1):
        clean +=dirty[i]

        if dirty[i] == dirty[i+1]:
            clean +='X'

    clean += dirty[-1]

    if len(clean) & 1:
        clean +="X"

    return clean

#generate the table based on key
def generate_table(key):
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    table = []

    for i in key.upper():
        if i not in table and i in alphanumeric:
            table.append(i)

    for i in alphanumeric:
        if i not in table:
            table.append(i)

    return table

#encoding the given plaintext based on the key 
def encode(plaintext,key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    for char1,char2 in chunker(plaintext , 2):
        row1, col1 = divmod(table.index(char1),6)
        row2, col2 = divmod(table.index(char2),6)

        if row1 == row2:
            ciphertext += table[row1*6 + (col1+1)%6]
            ciphertext += table[row2*6 + (col2+1)%6]
        elif col1 == col2:
            ciphertext += table[((row1+1)%6)*6 + col1]
            ciphertext += table[((row2+1)%6)*6 + col2]
        else:
            ciphertext += table[row1*6 + col2]
            ciphertext += table[row2*6 + col1]

    return ciphertext

#main function
print("*** EXTENDED PLAYFAIR CIPHER ***")
key=input("Enter the key:")
plaintext="".join(input("Enter the message to be encoded:").split(" "))
cleantext=prepare_input(plaintext)
table=generate_table(key)
#print(table)
print("The message is encoded as:",encode(plaintext,key))
