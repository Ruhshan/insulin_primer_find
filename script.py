from Bio import SeqIO
from Bio.Seq import Seq

for s in SeqIO.parse("insulin_receptor.fasta","fasta"):
	print "_______Forward_____"
	primers=file("forward_primers.txt").read().split()
	for p in primers:
		print p,
		pos=(str(s.seq).index(p),str(s.seq).index(p)+len(p))
		print '-'.join(map(str, pos))


for s in SeqIO.parse("insulin_receptor.fasta","fasta"):
	print "______Reverse_______"
	primers=file("reverse_primers.txt").read().split()
	for p in primers:
		print p,
		try:
			pos=(str(s.seq).index(str(Seq(p).reverse_complement())),str(s.seq).index(str(Seq(p).reverse_complement()))+len(p))
			print '-'.join(map(str, pos))
		except:
			print "Not_Found"
