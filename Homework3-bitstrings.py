#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8
#Homework3


def bitStringsum(first, second):
    output = ""
    for i in range(1,1+max(len(first),len(second))):
        outputBit = 0
        if (len(first)>=i ): outputBit = int(first[-i])
        
        if (len(second)>=i): outputBit += int(second[-i])
        output= str(outputBit) + output
    return output


def bitStringmin(bitstring):
    minimum=-1
    for bit in bitstring:
        if (minimum<0 and not bit == "0") or (int(bit)<minimum and int(bit)>0):
            minimum=int(bit)
    return minimum

def bitStringmax(bitstring):
    maximum=0
    for bit in bitstring:
        if int(bit)>maximum:
            maximum=int(bit)
    return maximum


def processBitstrings(first, second):
    output = ""
    bitsum=bitStringsum(first, second)
    minimum=str(bitStringmin(bitsum))
    maximum=str(bitStringmax(bitsum))
        
    for i in range(0,len(bitsum)):
        outputBit = "0"
        if bitsum[i]==minimum or bitsum[i]==maximum: outputBit ="1"
        output+= outputBit

    return output

def processBitstringlist(bitstrings):
    
    output = ""
    bitsum = bitstrings[0]
    for bit in bitstrings[1:]:
        bitsum=bitStringsum(bitsum, bit)
        
    minimum=str(bitStringmin(bitsum))
    maximum=str(bitStringmax(bitsum))
    
    for i in range(0,len(bitsum)):
        outputBit = "0"
        if bitsum[i]==minimum or bitsum[i]==maximum: outputBit ="1"
        output+= outputBit

    return output



