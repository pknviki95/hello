class Dogs:
    #instruction = [] # bad use of static/class variable
    def __init__(self,name):
        self.name = name
        self.instruction = [] # good use of instance variable
    def do(self,command):
        return self.instruction.append(command)
dog1 = Dogs("Tom")
dog1.do("roll over")
dog2 = Dogs("Fido")
dog2.do("play dead")
print(dog1.name, dog1.instruction)
print(dog2.name, dog2.instruction)
