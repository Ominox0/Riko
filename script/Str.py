def GetStr(index,Data):
    for i in range(index):
        Data.pop(0)
    text = ""
    for i in range(len(Data)):
        if '"' in Data[i]:
            for j in range(len(Data[i])):
                if Data[i][j] =='"':
                    for ij in range(len(Data[i])+j+1):
                        if Data[i][ij+j+1] =='"':
                            return text
                        else:
                            text += Data[i][ij+j+1]
    return None
def GVFT(index,Data):
    for i in range(index):
        Data.pop(0)
    text = ""
    for i in range(len(Data)):
        if '(' in Data[i]:
            for j in range(len(Data[i])):
                if Data[i][j] =='(':
                    for ij in range(len(Data[i])+j+1):
                        if Data[i][ij+j+1] ==')':
                            return text
                        else:
                            text += Data[i][ij+j+1]
