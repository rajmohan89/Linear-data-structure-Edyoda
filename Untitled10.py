#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])
array = [5, 2, 3, 4, 1, 6, 7]
summ = 7
print("Array= ", array)
find(array, len(array), summ)


# In[3]:


def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is:",A)



# In[14]:


def checkString(s1, s2, indexFound, Size):
    for i in range(Size):
 
        # check whether the character is equal or not
        if(s1[i] != s2[(indexFound + i) % Size]):
            return False
 
        # %Size keeps (indexFound+i) in bounds,
        # since it ensures it's value is always less than Size
    return True
 
 
# driver code
s1 = "abcd"
s2 = "cdab"
 
if(len(s1) != len(s2)):
    print("s2 is not a rotation on s1")
 
else:
 
    indexes = []  
    Size = len(s1)
    firstChar = s1[0]
    for i in range(Size):
        if(s2[i] == firstChar):
            indexes.append(i)
 
    isRotation = False
 
   
    for idx in indexes:
 
        isRotation = checkString(s1, s2, idx, Size)
 
        if(isRotation):
            break
 
    if(isRotation):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")


# In[13]:


string = "geeksforgeeks"
index = -1
fnc = ""
 
if len(string) == 0 :
  print("EMTPY STRING");
 
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is", fnc)


# In[15]:


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  
  
N = 3
TowerOfHanoi(N, 'A', 'C', 'B')


# In[16]:


def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
 
    # length of expression
    length = len(post_exp)
 
    # reading from right to left
    for i in range(length):
 
        # check if symbol is operator
        if (isOperator(post_exp[i])):
 
            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            # Push string temp back to stack
            s.append(temp)
 
        # if symbol is an operand
        else:           
            s.append(post_exp[i])    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    # Function call
    print("Prefix : ", postToPre(post_exp))


# In[17]:


def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True


# In[ ]:





# In[21]:


def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 
# Below is the function that
# reverses the given stack
# using insertAtBottom()
 
 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
 
def createStack():
    stack = []
    return stack
 
 
def isEmpty(stack):
    return len(stack) == 0

 
def push(stack, item):
    stack.append(item)
 

def pop(stack):
 
    if(isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()

def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
    print()
 
stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)


# In[22]:


class Node:
    # Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next = None
 
    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)
 
    # __repr__ is same as __str__
    __repr__ = __str__
 
 
class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
 
    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top, out))
 
    # __repr__ is same as __str__
    __repr__ = __str__
 
    # This method is used to get minimum element of stack
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
 
    # Method to check if Stack is Empty or not
 
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
            # If top not equal to None then stack is empty
            return False
 
    # This method returns length of stack
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count
 
    # This method returns top of stack
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
 
    # This method is used to add node to stack
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
 
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))
 
    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ((2 * self.minimum) - removedNode)
            else:
                print("Top Most Element Removed : {}" .format(removedNode))
 
 
# Driver program to test above class
if __name__ == '__main__':
   
  stack = Stack()
   
  # Function calls
  stack.push(3)
  stack.push(5)
  stack.getMin()
  stack.push(2)
  stack.push(1)
  stack.getMin()
  stack.pop()
  stack.getMin()
  stack.pop()
  stack.peek()


# In[ ]:




