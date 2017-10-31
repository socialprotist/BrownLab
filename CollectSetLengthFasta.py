"""

python CollectSetLengthFasta.py input.fas 300 

sys.argv[1] is the input file. 
sys.argv[2] is the length of the sequence that you want to collect

this will then make a file called >>>> input.length300.fas <<<< only has sequences that are 300 in length or greater. 



"""





import os
import glob
import sys



def oneline(short):
 infile = open(short, "r")
 lines = infile.readlines()
 infile.close()
 outfile = open(short,'w')
 for i,line in enumerate(lines):
	if line[0] == ('>'):
		if i>0:
			outfile.write("\n")
		outfile.write(line)
	else:
		outfile.write(line.strip())
 outfile.close()





def collectlength(gene,length):
	infile = open(gene, "r")
	filename = gene.split(".")[0]
	lines = infile.readlines()
	infile.close()
	outfile = open("%s.length%s.fas" %(filename,length), "w")
	
	for j in range(len(lines)):
		line = lines[j]
		if line[0] == ">":
			header = line.split(">")[1]
			header = header.strip()

			next_line = lines[j+1]
			lencontig = len(next_line)
			print lencontig
			if lencontig >= int(length):
				outfile.write(">")
				outfile.write(header)
				outfile.write("\n")
				outfile.write(next_line)
	outfile.close()




oneline(sys.argv[1]) # input file you want to work on
collectlength(sys.argv[1],sys.argv[2]) # input file, length to collect


"""
files = (fname [:-4] for fname in glob.glob('*.fas'))
for file in files:
	oneline(file)
    collectlength(file, sys.argv[1])
"""