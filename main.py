import sys
from antlr4 import *
from dist.CalculatorLexer import CalculatorLexer
from dist.CalculatorParser import CalculatorParser
from dist.CalculatorVisitor import CalculatorVisitor


def get_username():
    return "Jaider"

  
class MyVisitor(CalculatorVisitor):
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()} {get_username()}")


if __name__ == "__main__":
    while 1:
        data =  InputStream(input("calculator> "))
        # lexer
        lexer = CalculatorLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = CalculatorParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)