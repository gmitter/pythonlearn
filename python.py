#ClassOne.py
class Calculator(object):
    #define class to simulate a simple calculator
    def __init__ (self):
        #start with zero
        self.current = 0
    def add(self, amount):
        #add number to current
        self.current += amount
    def getCurrent(self):
        return self.current
    
legal= Calculator ()   
legal.add(2)
'''legal.add(3)
legal.add(5)'''
print(legal.getCurrent())


myExample = {'someItem': 2, 'otherItem': 20}
myExample['newItem'] = 400
for a in myExample:
    print (a)

print(myExample['newItem'])