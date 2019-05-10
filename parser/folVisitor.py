# Generated from fol.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .folParser import folParser
else:
    from folParser import folParser

# This class defines a complete generic visitor for a parse tree produced by folParser.

class folVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by folParser#sequent.
    def visitSequent(self, ctx:folParser.SequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#premisse.
    def visitPremisse(self, ctx:folParser.PremisseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#wff.
    def visitWff(self, ctx:folParser.WffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#formula.
    def visitFormula(self, ctx:folParser.FormulaContext):
        return self.visitChildren(ctx)



del folParser