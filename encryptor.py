
def encrypt(text):
    finalText = ""
    for letter in text:
        ascii = ord(letter)
        ascii += 1
        finalText += chr(ascii)
    return finalText


def decrypt(text):
    finalText = ""
    for letter in text:
        ascii = ord(letter)
        ascii -= 1
        finalText += chr(ascii)
    return finalText


def encryptArchive(fileRoute):
    archive = open(fileRoute, "r")
    text = archive.read()
    archive.close()
    encryptText = encrypt(text)

    archive = open(fileRoute, "w")
    archive.write(encryptText)
    archive.close()
    print("The encryption was successful")

def decryptArchive(fileRoute):
    archive = open(fileRoute, "r")
    text = archive.read()
    archive.close()
    decryptText = decrypt(text)

    archive = open(fileRoute, "w")
    archive.write(decryptText)
    archive.close()
    print("The decrypt was successful")

ansEncrypt = input("Press 'E' for encrypt an archive or press 'D' for decrypt: ")
routeFile = input("Enter the route file")

if ansEncrypt == "E":
    encryptArchive(routeFile)
else:
    decryptArchive(routeFile)

