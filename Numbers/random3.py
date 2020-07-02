import secrets
import os
import string

game = ['rock','paper','scissors']
print(secrets.choice(game))

#generate temp pass
def generateTempPass(numChars=8):
    potentialChars = string.ascii_letters + string.digits + string.punctuation
    result = "".join([secrets.choice(potentialChars) for i in range(numChars)])
    #print(result)
    return result

def generateStrongPass():
    while True:
        result = generateTempPass()
        print(result)
        if any(c.isupper() for c in result) and any(c.isdigit() for c in result):
            break
    print(result)

generateStrongPass()

resultUrl = "https://example.com?token="
resultUrl += secrets.token_urlsafe(15)
print(resultUrl)