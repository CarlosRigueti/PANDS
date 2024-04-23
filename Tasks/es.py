def readText (moby-dick.txt)
with open (fileName, 'rt') as f:
    read = f.read()
    count = read.count ("e")
    print (count)
    readText("moby-dick.text")
    
    