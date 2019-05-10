# Generated from fol.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .folParser import folParser
else:
    from folParser import folParser

# This class defines a complete listener for a parse tree produced by folParser.
class folListener(ParseTreeListener):

    # Enter a parse tree produced by folParser#sequent.
    def enterSequent(self, ctx:folParser.SequentContext):
        pass

    # Exit a parse tree produced by folParser#sequent.
    def exitSequent(self, ctx:folParser.SequentContext):
        pass


    # Enter a parse tree produced by folParser#premisse.
    def enterPremisse(self, ctx:folParser.PremisseContext):
        pass

    # Exit a parse tree produced by folParser#premisse.
    def exitPremisse(self, ctx:folParser.PremisseContext):
        pass


    # Enter a parse tree produced by folParser#wff.
    def enterWff(self, ctx:folParser.WffContext):
        pass

    # Exit a parse tree produced by folParser#wff.
    def exitWff(self, ctx:folParser.WffContext):
        pass


    # Enter a parse tree produced by folParser#formula.
    def enterFormula(self, ctx:folParser.FormulaContext):
        pass

    # Exit a parse tree produced by folParser#formula.
    def exitFormula(self, ctx:folParser.FormulaContext):
        pass


