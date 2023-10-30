from PIL import Image

listi=[]
def encrypt (loc,mssg):
    i=0
    extracted_bin = []
    msg=mssg
    data = ''.join(format(ord(i), "08b") for i in msg)
    with Image.open(loc) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel=list(img.getpixel((x, y)))
                for n in range(0,3):
                    if(i < len(data)):
                        #print(bin(pixel[0]))
                        test=False
                        for lal in range (2,10,2):
                        #print(bin(pixel[n]))
                        #print(lal)
                            # print(str(bin(pixel[n])[lal:lal+2])+" "+str(data[i:i+2]))
                            # if bin(pixel[n])[lal:lal+2]==data[i:i+2]:
                                if test=False:
                                    listi.append(lal)
                                    #print("added at :"+str(lal))
                                    test=True
                                    #pixel[n] = pixel[n] & ~1 | int(data[i])
                        if test==False:
                            #print("normal bin:"+str(bin(pixel [n])))
                            bb=bin(pixel [n])[:8]+data[i:i+2]
                            #print("changed bin: "+str(bb))
                            #print("added bits:"+str(data[i:i+2]))
                            ii=int(bb,2)
                            pixel[n]=ii
                            listi.append(8)
                            #print("added as LSB")
                        i+=2
            img.putpixel((x,y), tuple(pixel))
        img.save("torecv.png", "PNG")
    #print(listi)
    #print("length of list is :"+str(len(listi)))

def decrypt(loc,lis):
    j=0
    k=0
    extracted_bin = []
    try:
        with Image.open(loc) as img:
            width, height = img.size
            byte = []
            for x in range(0, width):
                for y in range(0, height):
                    pixel = list(img.getpixel((x, y)))
                    for n in range(0,3):
                        if j<(2*len(lis)):
                            ka=lis[k]
                            extracted_bin.append(bin(pixel[n])[ka:ka+2])
                            j+=2
                            k+=1
                        #extracted_bin.append(pixel[n]&1)
except Exception as e:
    print(e)
#data = "".join([str(x) for x in extracted_bin])
extracted_bin = [extracted_bin [xo: xo+4] for xo in range(0, len(extracted_bin), 4)]
#print(extracted_bin)
message=""
for z in range(len(extracted_bin)):
    lol=""
    st=0
    for ssa in range(0,4):
        lol += extracted_bin[z][ssa]
        st = int(lol, 2)
    # print(lol)
    # print(st)
    # pok=str(extracted_bin[z])
    message += chr(st)

    #   print("ERROR: :")
    #print(message)
    return message


def getList():
    return listi


if __name__== "__main__":
    print(" enter message")
    y = input()
    encrypt('tosend.jpg',y)
    p = getList()
    x = decrypt('torecv.png',p)
    print("decrypted msg is"+x)

