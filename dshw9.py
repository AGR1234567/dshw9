listsqwe=[]
w=input('Enter a word: ')

class Stack:
    def __init__(self,length):
        self.length=length
        self.lists=[]

    def display(self):
        print(self.lists)

    def add(self, w):
        if len(self.lists)<self.length:
            for j in w:
                self.lists.append(j)
        else:
            print('Stack Full')

    def remove(self):
        if len(self.lists)>0:
            x=self.lists.pop()
            print(x)
        else:
            print('Stack Empty')

s1=Stack(len(w))

s1.add(w)
for k in range(len(w)):
    s1.remove()