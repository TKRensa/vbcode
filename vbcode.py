#algorithm to encode number
def VBEncodeNumber(n):
    bytes = []
    while True:
        bytes.insert(0,n%128)
        if n<128:
            break
        else:
            n = int(n/128)


    bytes[len(bytes)-1] += 128
    return bytes

#using the above algorithm to encode number
def VBEncode(numbers):
    bytestream = []
    for n in numbers:
        bytes = VBEncodeNumber(n)
        bytestream.extend(bytes)
    return bytestream

#decode numbers
def VBDecode(bytestream):
    numbers = []
    n = 0
    for i in range(0,len(bytestream)):
        if(bytestream[i]<128):
            n = 128*n + bytestream[i]
        else:
            n = 128*n + (bytestream[i]-128)
            numbers.append(n)
            n = 0
    return numbers

#create difference from original numbers
def createDif(bytestream):
    numbers = []
    numbers.append(bytestream[0])
    for i in range(0,len(bytestream)-1):
        dif = bytestream[i+1]-bytestream[i]
        numbers.append(dif)
    return numbers

#get original numbers from difference
def deleteDif(bytestream):
    originalNumbers = []
    reverseDif = 0
    for i in range(0,len(bytestream)):
        reverseDif = reverseDif + bytestream[i]
        originalNumbers.append(reverseDif)
    return originalNumbers

#import number data from file
def importText():
    res=[]
    for lines in open('FILEPLACE/test.txt', 'r',encoding="utf-8", errors='ignore'):
        item=lines[:-1].split('\s')
        item = item[0].split("\t")
        newitem = [item[0],item[1].split(",")]
        res.append(newitem)
    
    return res
  
#encode the above data
def encodeText(input):
    encodedFile = []
    for lines in input:
        arrangedNum = sorted(lines[1])
        #convert string list to int list
        intArrangedNum = list(map(int,arrangedNum))
        numWithDif = createDif(intArrangedNum)
        
        encodedNum = VBEncode(numWithDif)
        newitem = [lines[0],encodedNum]
        encodedFile.append(newitem)
    
    return encodedFile

#export the encoded data
def exportEncodedText(list_row):
    f = open('FILEPLACE/encodedtest.txt', 'w', errors='ignore')
    for lines in list_row:
        f.write(lines[0] + "\t" + ",".join(map(str,lines[1])) + "\n")
    f.close()

#codes to check if it works
input = importText()
print(encodeText(input))
listText = encodeText(input)
exportEncodedText(listText)

testnum = [12552,5,12,128,1502,2352]
testnum2 = sorted(testnum)

