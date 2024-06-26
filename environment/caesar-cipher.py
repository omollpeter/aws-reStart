def getDoubleAlphabet(alphabet):
    """Concatenates string alphabet with itself and returns the answer"""
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    """Requests and returns the message to encrypt"""
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    """Defines how far you will shift letters"""
    shiftAmount = input("Please enter a key (whole number from 1 - 25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    """
    Encrypts and returns the encrypted message
    """
    encryptedMessage = ""
    upperCaseMessage = message.upper()
    for currentChar in upperCaseMessage:
        position = alphabet.find(currentChar)
        newPosition = position + int(cipherKey)
        if currentChar in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentChar
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    """Decrypts encrypted caesar-cipher message"""
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Alphabet:", myAlphabet)
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f"Alphabet2: {myAlphabet2}")
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print("Encrypted message:", myEncryptedMessage)
    myDecryptedMessage = encryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2[::-1])
    print("Decrypted message:", myDecryptedMessage)

runCaesarCipherProgram()