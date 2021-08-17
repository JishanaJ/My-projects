#!/usr/bin/env python
# coding: utf-8

# # 1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[1]:


def findPair(A, target):
    A.sort()
    
    (low, high) = (0, len(A) - 1)
    while low < high:
 
        if A[low] + A[high] == target: 
            print("Pair found", (A[low], A[high]))
            return
        if A[low] + A[high] < target:
            low = low + 1
        else:
            high = high - 1
 
    print("Pair not found")
  
if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(A, target)


# # 2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array

# In[2]:


def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[ ]:


#Another method for the same

def reverseList(A):
  print( A[::-1])     
A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseList(A) 


# # 3. Write a program to check if two strings are a rotation of each other?

# In[3]:


def checkRotation(s1, s2): 
    temp = '' 
  
    if len(s1) != len(s2): 
        return False
    
    temp = s1 + s1 
  
    if s2 in temp: 
        return True 
    else: 
        return False
    
string1 = "HELLO"
string2 = "LOHEL"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")
  


# # 4. Python program to print the first non-repeating character

# In[7]:



NO_OF_CHARS = 256

def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index

string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is " + string[index])


# # Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
# 

# In[8]:


def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return    
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
disks = int(input('Enter the number of disks: '))    
tower_of_hanoi(disks, 'A', 'B', 'C')


# # Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[11]:


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

def postToPre(post_exp):
 
    s = []
 
    length = len(post_exp)
 
    for i in range(length):
 
        if (isOperator(post_exp[i])):
 
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
            
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# # Q7.Write a program to convert prefix expression to infix expression.

# In[12]:


def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# # Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[13]:


def areBracketsBalanced(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
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
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
 
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# # Q9. Write a program to reverse a stack.

# In[14]:


class Stack:

    def __init__(self):
        self.Elements = []
    def push(self, value):
        self.Elements.append(value)
    def pop(self):
        return self.Elements.pop()
    def empty(self):
        return self.Elements == []
    def show(self):
        for value in reversed(self.Elements):
            print(value)

def BottomInsert(s, value):
    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 

stk = Stack() 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# # Q10. Write a program to find the smallest number using a stack.

# In[31]:


from collections import deque
 
 
class MinStack:
    def __init__(self):
        self.s = deque()
        self.min = None
    def push(self, x):
 
        if not self.s:
            self.s.append(x)
            self.min = x
 
        elif x > self.min:
            self.s.append(x)
 
        else:
            self.s.append(2*x - self.min)
            self.min = x
    def pop(self):
            if not self.s:
                self.print("Stack underflow!!")
 
            top = self.s[-1]
            if top < self.min:
                self.min = 2*self.min - top
            self.s.pop()
    def minimum(self):
 
        return self.min
 
 
if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(6)
    print(s.minimum())
 
    s.push(7)
    print(s.minimum())
 
    s.push(5)
    print(s.minimum())
 
    s.push(3)
    print(s.minimum())
    s.pop()
    print(s.minimum())
 
    s.pop()
    print(s.minimum())


# In[ ]:




