data = []
with open("data.txt") as f:
	for line in f:
		data+=[line.split(",")]

for i in range(len(data)):
	if not i==len(data)-1:
		data[i][len(data[i])-1] = data[i][len(data[i])-1][:-1]
	data[i] = [int(n) for n in data[i]]

# Get the checksum of the data
checksum = 0
for line in data:
	checksum+=max(line)-min(line)

print("Checksum = " + str(checksum))

data = [[5,9,2,8],
		[9,4,7,3],
		[3,8,6,5]]

# Get the sum of the divisions of the only two divisors of each row
tot = 0
for line in data:
	for f in line:
		for s in line:
			if s!=f and max(f,s)%min(f,s)==0:
				tot+=max(f,s)/min(f,s)

print("Total from sum of divisions = " + str(tot))