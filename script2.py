from Bio import SeqIO
from Bio.Seq import Seq
pref="""<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<p>Forward primers positions are highlighted with <span style="color:blue">BLUE</span> color</p>
<p>Reverse primers positions are highlighted with <span style="color:red">RED</span>  color</p>
"""
suf="""
</body>
</html>"""
for s in SeqIO.parse("insulin_receptor.fasta","fasta"):
	sequence="<p>"+str(s.seq)+"</p>"
	primers=file("forward_primers.txt").read().split()
	for p in primers:
		sequence=sequence.replace(p,'<span style="color:blue">'+p+'</span>')
	n=20
	new_seq=""
	count=0
	for c in sequence:
		if c in "ATGCN":
			count+=1
			new_seq+=c
			if count==50:
				new_seq+="\n"
				count=0
		else:
			new_seq+=c
	primers=file("reverse_primers.txt").read().split()
	for p in primers:
		r=str(Seq(p).reverse_complement())
		new_seq=new_seq.replace(r,'<span style="color:red">'+r+'</span>')
	print pref+new_seq+suf
