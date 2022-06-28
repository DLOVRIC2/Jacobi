"""
1. How tall is a tree?

Let us define a very simple version of a portfolio recursively as follows:
A portfolio is an asset that can be either
* a real asset (e.g. share, bond), or
* a weighted collection of portfolios where the weights add to 1

We can think of this like a tree. For example, in the tree below,
* portfolio A, which is the 'root' of the tree, is a collection containing some allocation to portfolios B and C
* portfolio B is a collection containing some allocation to portfolios D and E
* portfolios C, D and E are real assets because they are terminal nodes, aka 'leaves'

        A
       / \
      /   \
     B     C
    / \
   /   \
  D     E

Sometimes we might want to know the the 'height' of a tree, which is the number of edges on the longest path from the
root node to a leaf. For example, the height of the tree above is 2, because the longest path from A to a leaf is either
the path A -> B -> D or A -> B -> E, both of which contain 2 edges.

We can store a representation a portfolio (ignoring weights) using a dictionary which maps every non-leaf node in the
full tree to a list of it's immediate descendant nodes. We also need a reference to the root node. For example,
portfolio A could be stored as

root_node = 'A'
tree = {'A': ['B', 'C'], 'B': ['D', 'E']}

Task:
Write the function get_height(root_node, tree) which does just that; returns the height of a tree that starts at
root_node. Hint: use recursion.

Challenge task:
Do it in one line!

------------------------------------------------------------------------------------------------------------------------

2. Maximize your NPV

You are the chief investment officer of a big company and your research team presents you with a list of possible
projects to invest in. For each project they have calculated the expected NPV, which is summarised in the list bellow.

[13, 14, 2, 3, 1, 5, 4, 18, 17, 19, 5, 6, 9, 1]
(Here, the value in the ith index corresponds to the expected NPV of the ith project.)

Each pair of consecutive projects are mutually exclusive (if you invest in the ith project you cannot invest (i+1)th or
(i-1)th project). The total number of projects you can invest in is unconstrained.

What is the maximum total expected NPV you would achieve by investing in the optimal permissible subset of projects?

------------------------------------------------------------------------------------------------------------------------

3. Roundabout arithmetic with functions

Fill out the template to write simple calculations using functions.

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division, e.g eight(divided_by(three)) should return 2, not 2.66666...

Examples:

seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
"""


##### 1. How tall is a tree? #####



def get_height(node, tree):
    #your code here
    pass


# You can use these for testing

# basic_tree_root = 'A'
# basic_tree = {'A': ['B', 'C'], 'B': ['D', 'E']}  # (answer: 2)
#
# bigger_tree_root = 0
# bigger_tree = {0: [1, 2, 3], 1: [4, 5], 3: [6], 5: [9, 10], 6: [7, 8], 8: [18, 19, 20], 10: [11, 12], 12: [13, 14],
#                14: [15, 16, 17], 19: [21]}  # (answer: 6)
#
#
# print(get_height(basic_tree_root, basic_tree))
# print(get_height(bigger_tree_root, bigger_tree))


##### 2. Maximize your NPV #####



def max_nvp(array):
    '''
    Calculates maximum total expected NPV based on input array.
    
    Array - Value of the ith index in the array corresponds to the expected NPV of the ith project
    
    Rules:
    
    - Each pair of consecutive values in the array are mutually exclusive
    - The total number of projects that can be invested in is unconstrained
    
    Logic:
    
    If an array [1,2,3,4,5] is passed, the code will start by setting included value (incl[0]) to the
    first number of the array and exluded to zero.
    
    incl = [1, 0, 0, 0, 0]
    exl = 0
    
    Running through a loop we will check if exluded value + the new value in the array is
    greater than the previous included value. (if 0+2 > 1)
    
    If so, this is now our new included value and excluded value becomes included value from the
    previous loop.
    
    incl = [1, 2, 0, 0, 0]
    exl = 1
    
    ...
    
    At the final step we will have:
    
    incl = [1, 2, 4, 6, 9]
    exl = 6
    
    So the maximum NPV that can be achieved is stored as the last value in the incl list
    
    Hence, maxNPV = incl[-1]
    '''
    #Creating a list of zeros that corresponds to the length of the input array
    incl = [0 for i in range(len(array))]
    
    #As negative values in the array would impact the algorithm, they are simply replaced with zero.
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = 0
        else:
            continue
    
    incl[0] = array[0]
    exl = 0
    
    #Not to raise any errors if an input array ends up being just 1 number.
    if len(array) == 1:
        maxNPV = incl[0]
        return maxNPV
    
    #Required reccurance to get the max() value.
    else:
        for i in range(1, len(array)):
            incl[i] = max(exl+array[i], incl[i-1])
            exl = incl[i-1]
            
        maxNPV = incl[-1]
        
        return maxNPV


##### 3. Roundabout arithmetic with functions #####


def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2) 
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x//2


