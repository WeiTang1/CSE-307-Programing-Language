# Wei Tang
#CSE 307 Assignment 5

import sys
import tpg
import copy

variable_hash = {}
function_hash = {}
stack = {}
stack = variable_hash
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

class IntLiteral(Node):
    """
    A node representing integer literals.
    """

    def __init__(self, value):
        self.value = int(value)

    def evaluate(self):
        return self.value


class StrLiteral(Node):
        def __init__(self, value):
            temp = str(value)
            self.value = temp[1:len(temp)-1]

        def evaluate(self):
            return self.value

class ListLiteral(Node):
        def __init__(self,value):
            self.value = []

        def evaluate(self):
            return self.value


class Floatliteral(Node):
        def __init__(self, value):
            self.value = float(value)
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
        if ((not isinstance(left, int)) and ( not isinstance(left,float))) :
            raise SemanticError()
        if ((not isinstance(right, int)) and ( not isinstance(right,float))):
            raise SemanticError()
        return left * right

class Divide(Node):
    """
    A node representing division.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((not isinstance(left, int)) and ( not isinstance(left,float))) :
            raise SemanticError()
        if ((not isinstance(right, int)) and ( not isinstance(right,float))):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left / right

class Module(Node):
    """
    A node representing division.
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
        if right == 0:
            raise SemanticError()
        return left % right

class Add(Node):
    """
    A node representing division.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):

        left = self.left.evaluate()
        right = self.right.evaluate()

        if (isinstance(left,str) & isinstance(right,str)):
            return left+right
        if (isinstance(left,int) & isinstance(right,int)):
            return left+right
        if (isinstance(left,float) & isinstance(right,float)):
            return left+right
        if (isinstance(left,float) & isinstance(right,int)):
            return left+right
        if (isinstance(left,int) & isinstance(right,float)):
            return left+right
        if (isinstance(left,list) & isinstance(right,list)):
            return left+right
        else:
            raise SemanticError()

class Minus(Node):
    """
    A node representing division.
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
        return left - right

class Power(Node):
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

        return left ** right

class Floordiv(Node):
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
        return left // right

class And(Node):
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
        if (right and left) != 0:
            return 1
        else:
            return 0

class Or(Node):
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
        if (right or left) != 0:
            return 1
        else:
            return 0

class Not(Node):
    """
    A node representing multiplication.
    """

    def __init__(self, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.right = right

    def evaluate(self):
        right = self.right.evaluate()
        if not isinstance(right, int):
            raise SemanticError()
        if right == 0:
            return 1
        else:
            return 0

class LessThan(Node):
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
        if ( left < right):
            return 1
        else:
            return 0

class LessEqual(Node):
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
        if ( left <= right):
            return 1
        else:
            return 0

class Equal(Node):
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
        if ( left == right):
            return 1
        else:
            return 0

class Bigger(Node):
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
        if ( left > right):
            return 1
        else:
            return 0

class BiggerEqual(Node):
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
        if ( left >= right):
            return 1
        else:
            return 0
class Index(Node):
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
        if (isinstance(left,list) & isinstance(right,int)):
            if right > len(left):
                raise SemanticError()
            else:
                return left[right]
        elif (isinstance(left,str) & isinstance(right,int)):
            if right > len(left)-1:
                raise SemanticError()
            else:
                return left[right:right+1]
        else:
            raise SemanticError()

class NotEqual(Node):
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
        if ( left != right):
            return 1
        else:
            return 0

class Xin(Node):
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
        if (isinstance(right,list) | isinstance(right,str)):
            if left in right :
                return 1
            else:
                return 0
        else:
            raise SemanticError()

class Variable(Node):
        def __init__(self, value):
            self.value = str(value)
        def evaluate(self):
            return self.value

class functionName(Node):
    def __init__(self, value):
        self.value = str(value)
    def evaluate(self):
        return self.value

class assignment(Node):
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
        if isinstance(left,tuple):
            # could do more here for multiple indexing
            if left[0] not in variable_hash:
                raise SemanticError()
            else:
                if left[1] > len(variable_hash[left[0]]):
                    raise SemanticError()
                else:
                    variable_hash[left[0]][left[1]] = right
        else:
            variable_hash[left] = right

class getRvalue(Node):

    def __init__(self, left):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left

    def evaluate(self):
        left = self.left.evaluate()
        if left in variable_hash:
            return variable_hash[left]
        else:
            raise SemanticError()

# return the string name in variable
class variableLocation(Node):
    def __init__(self,left):
        self.left  = left

    def evaluate(self):
        left = self.left.evaluate()
        return left

class arrayLocation(Node):
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def evaluate(self):
        return (self.left.evaluate(),self.right.evaluate())

class myPrint(Node):
    def __init__(self,left):
        self.left = left

    def evaluate(self):
        print (self.left.evaluate())



class if_cond(Node):
    def __init__(self,left,right):
        self.left = left;
        self.right = right;
    def evaluate(self):
        if self.left.evaluate() == 1:
            return self.right.evaluate();

class if_else(Node):
    def __init__(self,if_cond,block):
        self.if_cond = if_cond
        self.block=block
    def evaluate(self):
        expression = self.if_cond.left
        if expression.evaluate() != 1:
            return self.block.evaluate()
        else:
            return self.if_cond.evaluate()

class while_block(Node):
    def __init__(self,expression,block):
        self.expr = expression
        self.block = block
    def evaluate(self):
        while self.expr.evaluate() ==1:
            self.block.evaluate()

class Block(Node):
    def __init__(self):
        self.statements = []
    def appendStatement(self,statement):
        self.statements.append(statement)

    def evaluate(self):
        for statement in self.statements:
            if (isinstance(statement,returnstate)):
                ret = statement.evaluate()
                print("ret:",ret)
                return (ret,1)
            else:
                statement.evaluate()


class functionblock(Node):
    def __init__(self,name):
        self.name=name
        self.parameternames = []
    def addparameter(self,variable):
        self.parameternames.append(variable)
    def addblock(self,statement):
        self.block = statement
    def evaluate(self):
        function_hash[self.name.evaluate()] = self


class functioncall(Node):
    def __init__(self,name):
        self.name = name.evaluate()
        self.values=[]
    def addvalues(self,value):
        self.values.append(value)
    def evaluate(self):
        global variable_hash
        temp = variable_hash
        functionblock = function_hash[self.name]
        parametervalues = self.values
        parameternames = functionblock.parameternames
        frame={}
        # construct frame
        for i in range(0,len(parameternames)):
            frame[parameternames[i].evaluate()]=parametervalues[i].evaluate()
        # print("frame: ",frame)
        variable_hash = frame
        for c in functionblock.block.statements:
            if (isinstance(c,returnstate)):
                re = c.evaluate()
                variable_hash=temp
                # print ("re",re)
                return re
            else:
                re = c.evaluate()
                if (isinstance(re,tuple)):
                    variable_hash=temp
                    # print ("tuple",re[0])
                    return re[0]

class returnstate(Node):
    def __init__(self,expression):
        self.expression = expression

    def evaluate(self):
        return self.expression.evaluate()

class Parser(tpg.Parser):
        """
        token float '\d+\.\d*|\d*\.\d+' Floatliteral;
        token int "\d+" IntLiteral;
        token str "\\"([^\\"])*\\"" StrLiteral;
        token functionname "[A-Za-z][A-Za-z0-9_]*\(" functionName;
        token left_variable "[A-Za-z][A-Za-z0-9_]*" Variable;
        token lparent "\(" StrLiteral;
        token rparent "\)" StrLiteral;
        token lbrack "\{" StrLiteral;
        token rbrack "\}" StrLiteral;
        token semi ";" StrLiteral;
        token equal "=" StrLiteral;
        separator space "\s+";

        START/a -> $a=Block()$ (block/b  $a.appendStatement(b)$)*;

        block/a ->"\{" body_statements/a "\}" | functionBlock/a;

        functionBlock/a ->  functionname/n $a=functionblock(n)$ left_variable/v $a.addparameter(v)$(',' left_variable/v $a.addparameter(v)$)* '\)' "\{" body_statements/b "\}"$a.addblock(b)$;

        body_statements/a -> $ a = Block()$ (statement/s $a.appendStatement(s)$)*;

        statement/a -> assignment/a | expression/a  | print/a | if_else/a | if_cond/a | while_state/a | returnstate/a;

        returnstate/a -> "return" expression/e $a=returnstate(e)$ semi;

        print/a -> "print" "\(" expression/a "\)" semi $ a=myPrint(a) $;

        if_cond/a -> "if" "\(" expression/c "\)" block/b $a=if_cond(c,b)$;

        if_else/a -> if_cond/a "else" block/b $a = if_else(a,b)$ ;

        while_state/a -> "while" "\(" expression/e "\)" block/b $ a=while_block(e,b)$;

        assignment/a -> left_value/v equal expression/a semi    $ a = assignment(v,a) $;

        left_value/a -> array_location/a | variable_location/a $ a = a $;

        variable_location/a -> left_variable/a $ a = variableLocation(a) $;

        array_location/a -> left_variable/a ("\[" expression/b "\]" $ a = arrayLocation(a,b) $)*;

        expression/a -> boolOR/a;

        boolOR/a -> boolAND/a ( "or" boolAND/b                 $ a = Or(a,b) $ )* ;

        boolAND/a -> boolNOT/a ( "\&\&" boolNOT/b               $ a = And(a,b) $ )* ;

        boolNOT/a -> comparison/a | "not"/op expression/b      $ a = Not(b) $ ;

        comparison/a -> xin/a ((
          "<=" xin/b $ a = LessEqual(a,b) $
        | "<>" xin/b $ a = NotEqual(a,b)    $
        | ">=" xin/b $ a = BiggerEqual(a,b) $
        | "==" xin/b $ a = Equal(a,b)       $
        | ">" xin/b  $ a = Bigger(a,b)    $
        | "<" xin/b $ a = LessThan(a,b) $
        ))* ;

        xin/a -> addsub/a ( "in" addsub/b                                   $ a = Xin(a,b) $ )* ;

        addsub/a -> floordiv/a ( ("\+" floordiv/b $ a = Add(a,b)$
        | "\-" floordiv/b $a = Minus(a,b)$))* ;

        floordiv/a -> power/a ( "//" power/b                              $ a = Floordiv(a,b) $ )* ;

        power/a -> module/a ( "\*\*" module/b                             $ a = Power(a,b) $ )* ;

        module/a -> muldiv/a ( "\%" muldiv/b                               $ a = Module(a,b) $ )* ;

        muldiv/a -> index/a ( ("\*" index/b                               $ a = Multiply(a,b) $
        | "/" index/b                                 $ a = Divide(a,b) $) )* ;

        index/a -> parens/a ( "\[" expression/b "\]"                      $ a = Index(a,b) $ )* ;

        parens/a -> "\(" expression/a "\)" | literal/a;

        literal/a ->  float/a | int/a | str/a | array/a | left_variable/a $ a = getRvalue(a) $| function_call/a ;

        function_call/a -> functionname/n $a=functioncall(n)$ expression/l $a.addvalues(l)$ ("," expression/l $a.addvalues(l)$)* "\)";

        array/a -> "\["     $ a = ListLiteral([]) $
            expression/b    $ a.value.append(b.evaluate()) $
        ( "," expression/b  $ a.value.append(b.evaluate()) $ )*
        "\]"
        | "\[" "\]" $ a = ListLiteral() $;


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


line = f.read().strip()
try:
    # Try to parse the expression.
    node = parse(line)
    node.evaluate()
    print ("\n\nvariable_hash",variable_hash)
    print ("function_hash",function_hash)
        # Try to get a result.
        # Print the representation of the result.
        # print(repr(result))
    # If an exception is thrown, print the appropriate error.
except tpg.Error:
    print("SYNTAX ERROR")
        # Uncomment the next line to re-raise the syntax error,
        # displaying where it occurs. Comment it for submission.
except SemanticError:
    print("SEMANTIC ERROR")



# For each line in f
# for l in f:
#     try:
#         # Try to parse the expression.
#         node = parse(l)

#         # Try to get a result.
#         result = node.evaluate()

#         # Print the representation of the result.
#         #

#     # If an exception is thrown, print the appropriate error.
#     except tpg.Error:
#         print("SYNTAX ERROR")
#         # Uncomment the next line to re-raise the syntax error,
#         # displaying where it occurs. Comment it for submission.
#     except SemanticError:
#         print("SEMANTIC ERROR")

f.close()

