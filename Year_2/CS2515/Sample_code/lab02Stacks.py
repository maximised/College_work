""" Classes and methods that use the Stack ADT.

"""

from stackA import Stack


def test():
    """ Test the basic functionality of the stack.

    Is exactly the same as the class method in each stack implementation.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print('stack should be |-1-2-3-->, and is', stack)
    print('stack.length should be 3, and is', stack.length())
    print('stack.top() should be 3, and is', stack.top())
    print('stack.pop() should be 3, and is', stack.pop())
    print('stack should now be |-1-2-->, and is', stack)
    print('stack.length() should be 2, and is', stack.length())
    stack.pop()
    stack.pop()
    print('popped two more items; stack.length() should be 0, and is', stack.length())
    print('stack.top() should be None, and is', stack.top())
    print('stack.pop() should be None, and is', stack.top())
    print('stack should be |-->, and is', stack)



def reverse(stack):
    """ Turn a stack upside down.

    Assumes stack is genuinely a stack.

    Args:
        stack - a stack

    Returns a new stack, with items in the opposite order. This version destoys
    the old stack.
    """

    result = Stack()
    while (stack.length() > 0):
        result.push(stack.pop())

    return result


def test_reverse_stack():
    """ Test the the reverse function does genuinely reverse a stack. """

    emptystack = Stack()
    print('stack =', emptystack)
    print('reversed stack =', reverse(emptystack))

    stack = Stack()
    inputstring = 'abcdefgh'
    for x in inputstring:
        stack.push(x)
    print('stack =', stack)
    print('reversed stack =', reverse(stack))
    

def infix_to_postfix(string):
    """ Convert an infix string to postfix, using a stack.

    Elements must be separated by spaces.

    Args:
        string - a character string, with elements separated by spaces, which
                 represents an infix expression.

    Return a string representation of the equivalent postfix expression.
    """
    tokenlist = string.split()
    output = []
    stack = Stack()
    for token in tokenlist:
        if token == '(':
            stack.push(token)
        elif token == ')':
            toptoken = stack.pop()
            while toptoken != '(':
                output.append(toptoken)
                toptoken = stack.pop()
        elif token == '*' or token == '/':
            toptoken = stack.top()
            while toptoken in ['*','/']:
                output.append(stack.pop())
                toptoken = stack.top()
            stack.push(token)
        elif token == '+' or token == '-':
            toptoken = stack.top()
            while toptoken in ['*','/','+','-']:
                output.append(stack.pop())
                toptoken = stack.top()
            stack.push(token)
        else:
            output.append(token)
    while stack.length() > 0:
        output.append(stack.pop())
    space= ' '
    newstr = space.join(output)
    return newstr

def evaluate_infix(string):
    """ Evaluate an infix expression, using two stacks.

    Args:
        string - a string representation of an infix expression, with
                 characters separated by spaces

    Return an evaluation of the expression.
    """
    return postfix(infix_to_postfix(string))

def match(str1, str2):
    """ Determine whether two single-char strings are matching brackets. """
    if (    (str2 == '[' and str1 == ']')
         or (str2 == '{' and str1 == '}')
         or (str2 == '(' and str1 == ')')):
        return True
    return False

def balanced_string(string):
    """ Determine whether the brackets in a string are balanced.

    Args:
        string - a character string, including some brackets.

    Return True if the brackets in the string are properly matched.
    """
    stack = Stack()
    pos = 0
    while pos < len(string):
        if string[pos] in '[{(':
            stack.push(string[pos])
        elif string[pos] in ']})':
            pair = stack.pop()
            if not match(string[pos], pair):
                return False
        pos = pos+1
    #return stack.length()
    if stack.length() == 0:
        return True
    else:
        return False

import random
import time

def colour_tetris_1D(rounds):
    """ Play single stack colour tetris.

    Args:
        rounds - the (int) number of rounds to be played.
    """
    charstr = 'RGB'
    blocklist = []
    stack = Stack()
    count = 0
    for i in range(rounds):
        blocklist.append(charstr[random.randint(0,2)])
    #print('blocklist =', blocklist)
    prefix = '        '
    i = 1
    for block in blocklist:
        output = str(i) + ': Accept ' + block + '?'
        clocktime0 = time.time()
        ans = input(output)
        clocktime1 = time.time()
        elapsed = clocktime1 - clocktime0
        success = '       '
        if elapsed > 2:
            print('TOO LATE (', elapsed, ' sec), block accepted')
            ans = 'y'
        if ans == 'y' or ans == 'Y':
            if stack.top() == block:
                stack.pop()
                count = count + 1
                success =  block + '-' + block + ' * '
            else:
                stack.push(block)
        print(success + 'Score = ' + str(count) + '; Stack: ' + str(stack))
        i = i+1
    print(stack.length(), 'still in stack')
    print('Score:', count - stack.length())

def colour_tetris(stacks, colours, rounds, th, secs):
    """ Play multi-stack colour tetris.

    Args:
        stacks - (int) number of stacks
        colours - (int) number of colours
        rounds - (int) number of blocks to be generated
        th  - (int) threshold height for a stack (if any stack exceeds this
              height, the game is over)
        secs - (int) number of seconds available for each move.
    """
    stacklist = []
    for i in range(stacks):
        stacklist.append(Stack())
    charstr = 'RGBOYIV'

    #generate the list of blocks
    blocklist = []
    for i in range(rounds):
        blocklist.append(charstr[random.randint(0,colours-1)])
    i = 0
    matches = 0
    threshold = True

    #reveal each block in turn, until exhausted or threshold breached
    while i < len(blocklist) and threshold:
        block = blocklist[i]
        i = i+1
        #display the block and get the user response
        output = str(i) + ': ' + block + '?'
        clocktime0 = time.time()
        ans = input(output)
        clocktime1 = time.time()
        elapsed = clocktime1 - clocktime0
        #now propcess the user response
        if elapsed > secs:
            print('TOO LATE (', elapsed, ' sec), block add to stack 1')
            ans = '1'
        if ans in['1','2','3','4']:
            value = int(ans)-1
        else:
            value = 0
        #now try to match the block with the top of the user's chosen stack
        if stacklist[value].top() == block:   #successful match
            stacklist[value].pop()
            print(' ******************************** ')
            matches = matches + 1
        else:                                 #failed match, so grow the stack
            stacklist[value].push(block)
        if stacklist[value].length() >= th:
            threshold = False
        else:
            j = 0
            while j < len(stacklist):
                print((j+1), ':', stacklist[j])
                j = j+1
    if threshold:
        print('Congratulations! You beat the system, and made', matches, 'matches.')
    else:
        print('You lasted for', i, 'rounds, and made', matches, 'matches.')
        
                
                
                
        
        
        
    
    
        
