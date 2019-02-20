import sys
from eVotUM.Cripto import eccblind

def printUsage():
	print("Usage: python init-app.py [-init]")


def parseArgs():
	if(len(sys.argv)>1):		
		if(sys.argv[1]=='-init'):
			maininit()
		else:
			printUsage()
	else:
		main()

def maininit():
	initComponents, pRDashComponents = eccblind.initSigner()
	f=open("Signercomponents.txt",'w+')
	f.write(initComponents+"\n")
	f.write(pRDashComponents)
	f.close()
	
def main():
	initComponents, pRDashComponents = eccblind.initSigner()
	print("pRDashComponents: %s" % pRDashComponents) 

if __name__ == "__main__":
	parseArgs()
