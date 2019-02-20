import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verify-app.py -cert <certificado do assinante> -msg <mensagem original a assinar> -sDash <Signature> -f <ficheiro do requerente> ")

def parseArgs():
    if (len(sys.argv) != 9):
        printUsage()
    else:
        eccPublicKeyPath = sys.argv[2]
        data = sys.argv[4]
        signature = sys.argv[6]
        ficheiro = sys.argv[8]		
        main(eccPublicKeyPath,data,signature,ficheiro)

def showResults(errorCode, validSignature):
    print("Output")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPublicKeyPath,data,signature,ficheiro):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    
    f=open(ficheiro,'r')
    x=f.read()
    f.close()
    
    blindComponents,pRComponents = x.split('\n')
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
