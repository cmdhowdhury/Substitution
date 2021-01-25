#!/usr/bin/python
import sys
import re

if len(sys.argv) < 2:
   print("usage:  python decrypt filename");#where decrypt is the name of your py file
   sys.exit()

f = open(sys.argv[1], "r")

text = f.read()

#process your text in some way:
output = text.lower()
outputWS = re.sub(r'[^\w]', '', output)
outputS = re.sub(r'[^\w\s]', '', output)
freq_out = {}

for i in outputWS:
    freq_out[i] = freq_out.get(i, 0) + 1

#print(freq_out)

for i in freq_out:
    freq_out[i] = (freq_out[i] / len(outputWS))

#print(freq_out)

freq_out = sorted(freq_out.items(), key=lambda x: x[0])

print(freq_out[0:26] + '\n')

#print the results
print(freq_out[1])

