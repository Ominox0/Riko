nums=[]
strs=[]
bools=[]
class Var():
    def VarAdd(self, Name, Value):
        if Name not in nums and Name not in strs and Name not in bools:
            try:
                if type(float(Value))==float:
                    nums.append(Name)
                    nums.append(Value)
                    return True
            except ValueError:
                pass
            if Value=="true" or Value=="false" or Value=="none":
                bools.append(Name)
                bools.append(Value)
                return True
            else:
                strs.append(Name)
                strs.append(Value)
                return True
    def VarRemove(self, Name):
        for i in range(len(nums)):
            if i%2==0:
                if Name==nums[i]:
                    nums.pop(i+1)
                    nums.pop(i)
                    return True
        for i in range(len(strs)):
            if i%2==0:
                if Name==strs[i]:
                    strs.pop(i+1)
                    strs.pop(i)
                    return True
        for i in range(len(bools)):
            if i%2==0:
                if Name==bools[i]:
                    bools.pop(i+1)
                    bools.pop(i)
                    return True
    def VarUpdate(self, Name, Value):
        for i in range(len(nums)):
            if i%2==0:
                if Name==nums[i]:
                    nums[i+1]=float(Value)
        for i in range(len(strs)):
            if i%2==0:
                if Name==strs[i]:
                    strs[i+1]=Value
        for i in range(len(bools)):
            if i%2==0:
                if Name==bools[i]:
                    bools[i+1]=Value
    def VarRename(self, Name, NewName):
        for i in range(len(nums)):
            if i%2==0:
                if Name==nums[i]:
                    nums[i]=NewName
                    return True
        for i in range(len(strs)):
            if i%2==0:
                if Name==strs[i]:
                    strs[i]=NewName
                    return True
        for i in range(len(bools)):
            if i%2==0:
                if Name==bools[i]:
                    bools[i]=NewName
                    return True
    def VarGet(self, Name):
        for i in range(len(nums)):
            if i%2==0:
                if Name==nums[i]:
                    return nums[i+1]
        for i in range(len(strs)):
            if i%2==0:
                if Name==strs[i]:
                    return strs[i+1]
        for i in range(len(bools)):
            if i%2==0:
                if Name==bools[i]:
                    return bools[i+1]
    def VarDump(self):
        for i in range(len(nums)):nums.pop(0);
        for i in range(len(strs)):strs.pop(0);
        for i in range(len(bools)):bools.pop(0);
    def VarShow(self):
        if len(nums) >= 1:
            for i in range(len(nums)):
                if i%2==0:
                    print("<num> "+str(nums[i])+" : "+str(nums[i-1]))
        else:
            print("There is no numbers")
        if len(strs) >= 1:
            for i in range(len(strs)):
                if i%2==0:
                    print("<str> "+str(strs[i])+" : "+str(strs[i-1]))
        else:
            print("There is no strings")
        if len(bools) >= 1:
            for i in range(len(bools)):
                if i%2==0:
                    print("<bool> "+str(bools[i])+" : "+str(bools[i-1]))
        else:
            print("There is no bools")
    def ToStr(self, Name):
        for i in range(len(nums)):
            if i%2==0:
                if Name==nums[i]:
                    Value=nums[i+1]
                    strs.append(Name)
                    strs.append(Value)
                    nums.pop(i+1)
                    nums.pop(i)
                    return True
        for i in range(len(bools)):
            if i%2==0:
                if Name==bools[i]:
                    Value=bools[i+1]
                    strs.append(Name)
                    strs.append(Value)
                    bools.pop(i+1)
                    bools.pop(i)
                    return True
    def ToNum(self, Name):
        for i in range(len(strs)):
            if i%2==0:
                if Name==strs[i]:
                    Value=strs[i+1]
                    nums.append(Name)
                    nums.append(Value)
                    strs.pop(i+1)
                    strs.pop(i)
                    return True
    def ToBool(self, Name):
        for i in range(len(strs)):
            if i%2==0:
                if Name==strs[i]:
                    Value=strs[i+1]
                    bools.append(Name)
                    bools.append(Value)
                    strs.pop(i+1)
                    strs.pop(i)
                    return True
    def VarSave(self):
        from os import mkdir
        try:
            mkdir("Var/")
        except OSError:
            pass
        del mkdir
        from json import dumps
        VarStr={}
        VarNum={}
        VarBool={}  
        for i in range(len(strs)):
            if i%2==0:
                VarStr[strs[i]] = strs[i+1]
        for i in range(len(nums)):
            if i%2==0:
                VarNum[nums[i]] = nums[i+1]
        for i in range(len(bools)):
            if i%2==0:
                VarBools[bools[i]] = bools[i+1]
        with open("Var/str.json","w") as Vars:
            Vars.write(dumps(VarStr, indent=4))
            Vars.close()
        with open("Var/num.json","w") as Vars:
            Vars.write(dumps(VarNum, indent=4))
            Vars.close()
        with open("Var/bool.json","w") as Vars:
            Vars.write(dumps(VarBool, indent=4))
            Vars.close()
        del dumps
    def VarLoad(self):
        from json import load
        str1 = open("Var/str.json")
        num1 = open("Var/num.json")
        bool1 = open("Var/bool.json")
        Strs1 = load(str1)
        Nums1= load(num1)
        Bools1 = load(bool1)
        str1.close()
        num1.close()
        bool1.close()
        Keys = Strs1.keys()
        Values = Strs1.values()
        for i in range(len(Keys)):
            strs.append(Keys[i])
            strs.append(Values[i-1])
        Keys = Nums1.keys()
        Values = Nums1.values()
        for i in range(len(Keys)):
            nums.append(Keys[i])
            nums.append(Values[i-1])
        Keys = Bools1.keys()
        Values = Bools1.values()
        for i in range(len(Keys)):
            bools.append(Keys[i])
            bools.append(Values[i-1])
    def VarFlush(self):
        from shutil import rmtree 
        rmtree("Var/")
        del rmtree
