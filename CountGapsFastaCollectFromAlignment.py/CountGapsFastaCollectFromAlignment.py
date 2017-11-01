"""

python CountGapsFastaCollectFromAlignment.py test.bmge.fas 0.7 test.fas

sys.argv[1] is the trimmed alignment that you want to count gaps in
sys.argv[2] is the percent gaps i.e., "-" ## dashes that are allowed
sys.argv[3] is the untrimmed alignment file that you want to get sequences from



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
	outfile = open("%s.missing%s.list.txt" %(filename,missing), "w")
	
	for j in range(len(lines)):
		line = lines[j]
		if line[0] == ">":
			header = line.split(">")[1]
			header = header.strip()
			next_line = lines[j+1]
			lencontig = len(next_line)
			numdashes = next_line.count("-")
			print header
			percentmissing = float(numdashes)/lencontig
                        print percentmissing
			if percentmissing <= float(missing):
				print "Fine, Collect This"
				outfile.write(header)
				outfile.write("\n")
			else:
				print "Too Gappy, Discard This"
	outfile.close()



def collectseqspercentcuttoff(gene,missing,alignment):
	filename = gene.split(".")[0]
	listfile= open("%s.missing%s.list.txt" %(filename,missing), "r")
	listlines = listfile.readlines()
	list = []	
	for line in listlines:
		list.append(line.strip())	
	infile = open(alignment, "r")
	filename = gene.split(".")[0]
	lines = infile.readlines()
	infile.close()
	outfile = open("%s.missing%s.alignment.fas" %(filename,missing), "w")
	print list
	for j in range(len(lines)):
		line = lines[j]
		if line[0] == ">":
			header = line.split(">")[1]
			header = header.strip()
			next_line = lines[j+1]
			if header in list:
				outfile.write(">")
				outfile.write(header)
				outfile.write("\n")
				outfile.write(next_line)
	outfile.close()


oneline(sys.argv[1]) # input file you want to work on
oneline(sys.argv[3]) #3 is alignment not trimmed
collectmissingdatapercentcuttoff(sys.argv[1],sys.argv[2]) #1 input file, #2 percent data missing that is allowable "0.7" i.e., 70% gaps are allowed!

collectseqspercentcuttoff(sys.argv[1],sys.argv[2],sys.argv[3]) #3 is alignment not trimmed

"""
files = (fname [:-4] for fname in glob.glob('*.fas'))
for file in files:
	oneline(file)
    collectlength(file, sys.argv[1])
"""

