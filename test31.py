from itertools import permutations
import itertools
from progressbar import ProgressBar
# perms = [''.join(p) for p in permutations('trumper2003',3)]
# print(perms)
bar = ProgressBar()
res = []
arrr = 'avivtrumperTRUMPER2003'
arr= []
for j in range(len(arrr)):
	if(arrr[j not in arr]):
		arr.append(arrr[j])
print(arr)


for L in bar(range(10, 13)):
    for subset in itertools.combinations(arr, L):
        res.append("".join(subset))
        if(subset == "trumper2003"):
			print("found pass")
			break
		
F = open("passwords.txt","w+")
for i in res:
	F.write(i+" ")
F.close()