name="JOe"
print(name)
num=32
print(float(num))

print(type(num)) #int
print(type(name)==str) #True

print("game"!=40) #True
print(1=="s") #False

print(isinstance(name,str)) #True
print(isinstance("hell",int)) #False

age=2.99
print("Age type: ",type(age))

newAge=float(32)
print("New age type: ",type(newAge))

print("What's for dinner?")
dinner=input()
print(f"The dinner is {dinner}! Thanks "+name+":)")

