import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python ofusca-app.py -msg <mensagem a assinar> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv)!= 5):
        printUsage()
    else:
        data = sys.argv[2]
        pRDashComponents = sys.argv[4]
        main(data,pRDashComponents)

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        f = open("BlindMsgCmp.txt",'w+')
        f.write(blindComponents + '\n')
        f.write(pRComponents)
        f.close()

    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main(data,pRDashComponents):
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
