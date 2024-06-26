import sys

if len(sys.argv) != 2:
    print("Usage:  python3 csv_fixer.py filename.csv")
    exit()
infile = open(sys.argv[1], 'rb')
content = infile.read()
infile.close()
content = content.replace(b'\r\n', b'\n')
content = content.replace(b',,,\n', b'')
if not content.endswith(b'\n'):
    content += b'\n'
outfile = open(sys.argv[1][:-4]+"_FIXED.csv", 'wb')
outfile.write(content)
outfile.close()
