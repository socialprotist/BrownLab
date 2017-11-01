"""
python CountGapsFasta.py test.bmge.fas 0.7

sys.argv[1] is the trimmed alignment that you want to count gaps in
sys.argv[2] is the percent gaps i.e., "-" ## dashes that are allowed




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





def collectmissingdatapercentcuttoff(gene,missing):
	infile = open(gene, "r")
	filename = gene.split(".")[0]
	lines = infile.readlines()
	infile.close()
	outfile = open("%s.missing%s.fas" %(filename,missing), "w")
	
	for j in range(len(lines)):
		line = lines[j]
		if line[0] == ">":
			header = line.split(">")[1]
			header = header.strip()
			next_line = lines[j+1]
			lencontig = len(next_line)
			numdashes = next_line.count("-")
			print numdashes
			print lencontig
			print str(float(numdashes)/lencontig)
			if float(numdashes)/lencontig < float(missing):
				outfile.write(">")
				outfile.write(header)
				outfile.write("\n")
				outfile.write(next_line)
	outfile.close()




oneline(sys.argv[1]) # input file you want to work on
collectmissingdatapercentcuttoff(sys.argv[1],sys.argv[2]) #1 input file, #2 percent data missing that is allowable "0.5" i.e., 50%


"""
files = (fname [:-4] for fname in glob.glob('*.fas'))
for file in files:
	oneline(file)
    collectlength(file, sys.argv[1])
"""

