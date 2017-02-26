pValues = [ True, False ]
qValues = [ True, False ]
rValues = [ True, False ]

print( "p", "\t", "q", "\t", "r", "\t", "(p or q) and (not p and not q)" )

for p in pValues:
	for q in qValues:
		for r in rValues:
			print( p, "\t", q, "\t", r, "\t", (p or q) and not (p and q) )
