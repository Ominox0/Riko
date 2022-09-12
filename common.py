from var import Var
v = Var()
class Get():
    def Input(self,Name,Text):
        v.VarAdd(Name,input(Text))
class Open():
        def __init__(self,Name,FileName,Mode="r+",encoding="UTF-8"):
            self.Name = Name
            self.FileName = FileName
            self.Mode = Mode
            self.encoding = encoding
        def Read():
            with open(self.FileName, self.Mode, self.encoding) as File:
                v.VarAdd(self.Name,File.read())
                File.close()
        def Write(Text):
            with open(self.FileName, self.Mode, self.encoding) as File:
                File.write(Text)
                File.close()
class util():
    def min(self,obj):
        pass
    def max(self,obj):
        pass
