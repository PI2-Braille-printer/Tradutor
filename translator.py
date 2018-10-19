import pybrl as brl
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

result = []
content = [x.strip() for x in lines]
for line in content:
    bra = brl.matrix(brl.braille(line))
    char_lines = []
    for i in range(0, 3):
        temp = [item[i] for item in bra]
        temp = [inner for outer in temp for inner in outer]
        char_lines.append(temp)
    
    for char_line in char_lines:
        result.append(''.join([str(e) for e in char_line]))

with open(sys.argv[2], 'wb') as f:
    for line in result:
        f.write(line + '\n')
