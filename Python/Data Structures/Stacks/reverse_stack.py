# create class for stack 
class Stack:

    # create empty list
    def __init__(self):
        self.Elements = []
    
    # push() to insert an element
    def push(self, value):
        self.Elements.append(value)
    
    # pop() to remove an element
    def pop(self):
        return self.Elements.pop()
    
    # empty() check if the stack is empty or not
    def empty(self):
        return self.Elements == []
    
    # show() display the stack
    def show(self):
        for value in reversed(self.Elements):
            print(value)

    # Insert_Bottom() insert a value at the bottom
    def BottomInsert(s, value):

        # check if the stack is empty or not
        if s.epmty():

            # if stack is empty, call push() method
            s.push(value)
        else:
            popped = s.pop()
            BottomInsert(s, value)
            s.push(popped)
    
    # Reverse() reverse the stack
    def Reverse(s):
        if s.empty():
            pass
        else:
            popped = s.pop()
            Reverse(s)
            BottomInsert(s, popped)

# create object of stack class
stk = Stack()

stk.push(2)
stk.push(4)
stk.push(6)
stk.push(8)
stk.push(10)

print("Original Stack")
stk.show()

print("\nStack after reversing")
stk.Reverse(stk)
stk.show
