import sys

if (len(sys.argv) != 3):
    print("txtrecordsplitter.py <encoded file> <seperator>")
    print("Example: txtrecordsplitter.py base64-script.txt \';\'")
    exit()

inFile = sys.argv[1]
seperator = sys.argv[2]
part = 1
try:
    outFile = open(f"txtrecord{part}.txt", "x")
except FileExistsError:
    if input("output files already exist. overwrite? Y/N").lower() == "y":
        outFile = open(f"txtrecord{part}.txt", "w")
    else:
        exit()
counter = 0
readSize = 255 - len(seperator)

with open(inFile, "r") as file:
    while True:
        line = file.read(readSize)
        if not line:
            break
        line += seperator + "\n"
        counter += readSize
        if counter >= 4000:
            outFile.close()
            part += 1
            outFile = open(f"txtrecord{part}.txt", "w")
            counter = 0
        outFile.write(line)
    print(f"file split into {part} txt records")