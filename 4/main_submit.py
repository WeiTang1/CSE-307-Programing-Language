#Thang Bui
#108848430

import sys
import tpg
import math

# create a dictionary to store the values of variables
variables = {}
# evaluateions list will keep track of the statements that need to be evaluate
class SemanticError(Exception):
    """
    This is the class of the exception that is raised when a semantic error
    occurs.
    """
    
# These are the nodes of our abstract syntax tree.
class Node(object):
    """
    A base class for nodes. Might come in handy in the future.
    """

    def evaluate(self):
        """
        Called on children of Node to evaluate that child.
        """
        raise Exception("Not implemented.")

class Value(Node):
    def __init__(self, value):
        try:
            self.value = int(value)
        except (ValueError):
            try:
                self.value = float(value)
            except (ValueError):
                s = str(value)
                # get rid of the ""
                self.value = s[1:len(s)-1]
    def evaluate(self):
        return self.value

class List(Node):
        def __init__(self,value):
            self.value = []

        def evaluate(self):
            return self.value


class Multiply(Node):
    """
    A node representing multiplication.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left * right

class Multiply_Divide(Node):
    """
    A node representing multiplication and division.
    """

    def __init__(self, left, op, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) and not isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) and not isinstance(right, float):
            raise SemanticError()
        if self.op == '/' and right == 0:
            raise SemanticError()
        if self.op == '*':
            return left * right
        else:
            return left/right

class Comparison(Node):
    """
    A node representing a comparison.
    """

    def __init__(self, left, op, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) and not isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) and not isinstance(right, float):
            raise SemanticError()
        if self.op == '<':
            if left < right:
                return 1
            else:
                return 0
        elif self.op == '<=':
            if left <= right:
                return 1
            else:
                return 0
        elif self.op == '==':
            if left == right:
                return 1
            else:
                return 0
        elif self.op == '<>':
            if left != right:
                return 1
            else:
                return 0
        elif self.op == '>':
            if left > right:
                return 1
            else:
                return 0
        elif self.op == '>=':
            if left >= right:
                return 1
            else:
                return 0

class Module(Node):
    """
    A node representing modulation.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) and not isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) and not isinstance(right, float):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left % right

class Power(Node):
    """
    A node representing power.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) and not isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) and not isinstance(right, float):
            raise SemanticError()
        return math.pow(left, right)

class FloorDivide(Node):
    """
    A node representing floor division.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) and not isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) and not isinstance(right, float):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left // right

class Add_Sub(Node):
    """
    A node representing addition and abstraction.
    """

    def __init__(self, left, op, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.op == '-':
            if not isinstance(left, int) and not isinstance(left, float):
                raise SemanticError()
            if not isinstance(right, int) and not isinstance(right, float):
                raise SemanticError()
            return left - right
        else:
            if isinstance(left, str) and not isinstance(right, str):
                raise SemanticError()
            if isinstance(left, list) and not isinstance(right, list):
                raise SemanticError()
            if isinstance(left, int) and not isinstance(right, int) and not isinstance(right, float):
                raise SemanticError()
            return left + right

class Boolean_Not(Node):
    """
    A node representing Boolean Not.
    """

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        value = self.value.evaluate()
        if not isinstance(value, int):
            raise SemanticError()
        if value == 0:
            return 1
        else:
            return 0


class Boolean_And(Node):
    """
    A node representing boolean and
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if left == 0 or right == 0:
            return 0
        else:
            return 1

class Boolean_Or(Node):
    """
    A node representing boolean or
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if left != 0 or right != 0:
            return 1
        else:
            return 0

class Index(Node):
    """
    A node representing indexing of a list
    """
    def __init__(self, l, index):
        self.l = l
        self.index = index

    def evaluate(self):
        l = self.l.evaluate()
        index = self.index.evaluate()
        if not isinstance(l, list) and not isinstance(l, str):
            raise SemanticError()
        if not isinstance(index, int):
            raise SemanticError()
        if index > len(l) - 1:
            raise SemanticError()
        return l[index]

class In(Node):
    """
    A node representing indexing of a list
    """
    def __init__(self, element, l):
        self.l = l
        self.element = element

    def evaluate(self):
        l = self.l.evaluate()
        element = self.element.evaluate()
        if not isinstance(l, list):
            raise SemanticError()
        if element in l:
            return 1
        else:
            return 0

class Variable(Node):
    global variables
    def __init__(self, var):
        # l-value
        self.name = str(var)
    def evaluate(self):
        return self.name

class Assignment(Node):
    """
    A node representing assignment operation
    """
    def __init__(self, left, right):
        global variables
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if isinstance(left, tuple):
            # if left is a tuple, it must be array location because the LocationArray evaluate function return a tuple
            try:
                if left[0] in variables:
                    variables[left[0]][left[1]] = right
            except (IndexError):
                raise SemanticError()
        else:
            variables[left] = right


class GetValue(Node):
    """
    A node representing getting right value
    """

    def __init__(self, var):
        # The nodes representing the left and right sides of this
        # operation.
        self.var = var.name

    def evaluate(self):
        global variables
        try:
            # r-value
            value = variables[self.var]
            return value
        except (KeyError):
            raise SemanticError

class LocationArray(Node):
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def evaluate(self):
        # the evaluate function will return the tuple of the name of the variable
        # and the index of the array
        return (self.left.evaluate(),self.right.evaluate())

class Print(Node):
    def __init__(self,exp):
        self.exp = exp

    def evaluate(self):
        # Print the representation of the result.
        print(self.exp.evaluate())

class IF(Node):
    def __init__(self,exp,block):
        self.exp = exp
        self.block = block
    def evaluate(self):
        # Print the representation of the result.
        if self.exp.evaluate() == 1:
            self.block.evaluate()

class IF_ELSE(Node):
    def __init__(self,exp,block1, block2):
        self.exp = exp
        self.if_block = block1
        self.else_block = block2
    def evaluate(self):
        # Print the representation of the result.
        if self.exp.evaluate() == 1:
            self.if_block.evaluate()
        else:
            self.else_block.evaluate()

class BlockStatements(Node):
    def __init__(self):
        self.blocks = []

    def addStatement(self, stmt):
        self.blocks.append(stmt)

    def evaluate(self):
        for statement in self.blocks:
            statement.evaluate()

class WHILE(Node):
    def __init__(self,exp,block):
        self.exp = exp
        self.block = block

    def evaluate(self):
        # Print the representation of the result.
        while self.exp.evaluate() == 1:
            self.block.evaluate()

# This is the TPG Parser that is responsible for turning our language into
# an abstract syntax tree.
class Parser(tpg.Parser):
    """
    token value "((\d+\.\d*)|(\d*\.\d+))|(\d+)|(\\"([^\\"])*\\")" Value
    token var "[A-Za-z][A-Za-z0-9_]*" Variable
    token assign "=" Value
    separator space "\s+";

    START/a -> block/a;

    block/a ->"\{" statements/a "\}" | "gcd";

    statements/a -> $ a = BlockStatements() $ (statement/b $ a.addStatement(b)$)*;

    statement/a -> assignment/a | expression/a | print/a | if_else_statement/a | if_statement/a | while_statement/a;

    print/a -> "print" "\(" expression/a "\);"                                           $ a = Print(a) $;

    while_statement/a -> "while" "\(" expression/a "\)" block/b                          $ a = WHILE(a,b)$;

    if_else_statement/a -> "if" "\(" expression/a "\)" block/b  "else" block/c                              $ a = IF_ELSE(a, b, c) $;

    if_statement/a -> "if" "\(" expression/a "\)" block/b                                $ a = IF(a, b) $;

    assignment/a -> location_var/l assign  expression/a ";"                              $ a = Assignment(l,a) $;

    location_var/a -> l_array/a | var/a;

    l_array/a -> var/a ("\[" expression/b "\]"                                       $ a = LocationArray(a,b) $)*;

    expression/a -> boolOR/a;

    boolOR/a -> boolAND/a ( "or"/op boolAND/b                                        $ a = Boolean_Or(a,b) $ )*;

    boolAND/a -> boolNOT/a ( "\&\&"/op boolNOT/b                                      $ a = Boolean_And(a,b) $ )*;

    boolNOT/a -> comparison/a | "not"/op expression/b                                $ a = Boolean_Not(b) $;

    comparison/a -> isin/a ( ("<="/op | "<>"/op | ">="/op | "\=\="/op  | ">"/op | "<"/op ) isin/b     $ a = Comparison(a,op,b) $ )*;

    isin/a -> addsub/a ( "isin"/op addsub/b                                          $ a = In(a,b) $ )*;

    addsub/a -> floordiv/a ( ("\+"/op | "\-"/op) floordiv/b                          $ a = Add_Sub(a,op,b) $ )*;

    floordiv/a -> power/a ("//"/op power/b                                           $ a = FloorDivide(a,b) $ )*;

    power/a -> mod/a ("\*\*"/op mod/b                                                $ a = Power(a,b) $ )*;

    mod/a -> muldiv/a ("\%"/op muldiv/b                                              $ a = Module(a,b) $ )*;

    muldiv/a -> index/a ( ("\*"/op | "/"/op) index/b                                 $ a = Multiply_Divide(a,op,b) $ )*;

    index/a -> parens/a ("\[" expression/b "\]"                                      $ a = Index(a,b) $ )*;

    parens/a -> "\(" expression/a "\)" | literal/a;

    array/a -> "\["     $ a = List([]) $
            expression/b    $ a.value.append(b.evaluate()) $
        ( "," expression/b  $ a.value.append(b.evaluate()) $ )*
        "\]"
        | "\[" "\]" $ a = List([]) $;

    literal/a -> value/a | array/a | var/a $a = GetValue(a)$;
    """
# Make an instance of the parser. This acts like a function.
parse = Parser()

# This is the driver code, that reads in lines, deals with errors, and
# prints the output if no error occurs.

# Open the file containing the input.
try:
    f = open(sys.argv[1], "r")
except(IndexError, IOError):
    f = open("input1.txt", "r")

file = f.read().strip()
try:
    eval = parse(file)
    eval.evaluate()
# If an exception is thrown, print the appropriate error.
except tpg.Error:
    print("SYNTAX ERROR")

        
except SemanticError:
    print("SEMANTIC ERROR")

f.close()
