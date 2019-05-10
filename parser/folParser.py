# Generated from fol.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\5\3\21\n\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\63")
        buf.write("\n\5\3\5\2\2\6\2\4\6\b\2\2\2\66\2\n\3\2\2\2\4\20\3\2\2")
        buf.write("\2\6\31\3\2\2\2\b\62\3\2\2\2\n\13\5\4\3\2\13\f\7\n\2\2")
        buf.write("\f\r\5\b\5\2\r\16\7\2\2\3\16\3\3\2\2\2\17\21\5\b\5\2\20")
        buf.write("\17\3\2\2\2\20\21\3\2\2\2\21\26\3\2\2\2\22\23\7\t\2\2")
        buf.write("\23\25\5\b\5\2\24\22\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2")
        buf.write("\2\26\27\3\2\2\2\27\5\3\2\2\2\30\26\3\2\2\2\31\32\5\b")
        buf.write("\5\2\32\33\7\2\2\3\33\7\3\2\2\2\34\35\7\13\2\2\35\63\b")
        buf.write("\5\1\2\36\37\7\b\2\2\37\63\5\b\5\2 !\7\3\2\2!\"\5\b\5")
        buf.write("\2\"#\7\6\2\2#$\5\b\5\2$%\7\4\2\2%\63\3\2\2\2&\'\7\3\2")
        buf.write("\2\'(\5\b\5\2()\7\7\2\2)*\5\b\5\2*+\7\4\2\2+\63\3\2\2")
        buf.write("\2,-\7\3\2\2-.\5\b\5\2./\7\5\2\2/\60\5\b\5\2\60\61\7\4")
        buf.write("\2\2\61\63\3\2\2\2\62\34\3\2\2\2\62\36\3\2\2\2\62 \3\2")
        buf.write("\2\2\62&\3\2\2\2\62,\3\2\2\2\63\t\3\2\2\2\5\20\26\62")
        return buf.getvalue()


class folParser ( Parser ):

    grammarFileName = "fol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'->'", "'&'", "'+'", "'-'", 
                     "','", "'=>'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "IMPL", "AND", "OR", 
                      "NOT", "COMMA", "ENTL", "PREPOSITION", "WS" ]

    RULE_sequent = 0
    RULE_premisse = 1
    RULE_wff = 2
    RULE_formula = 3

    ruleNames =  [ "sequent", "premisse", "wff", "formula" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    IMPL=3
    AND=4
    OR=5
    NOT=6
    COMMA=7
    ENTL=8
    PREPOSITION=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SequentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def premisse(self):
            return self.getTypedRuleContext(folParser.PremisseContext,0)


        def ENTL(self):
            return self.getToken(folParser.ENTL, 0)

        def formula(self):
            return self.getTypedRuleContext(folParser.FormulaContext,0)


        def EOF(self):
            return self.getToken(folParser.EOF, 0)

        def getRuleIndex(self):
            return folParser.RULE_sequent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequent" ):
                listener.enterSequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequent" ):
                listener.exitSequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequent" ):
                return visitor.visitSequent(self)
            else:
                return visitor.visitChildren(self)




    def sequent(self):

        localctx = folParser.SequentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sequent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.premisse()
            self.state = 9
            self.match(folParser.ENTL)
            self.state = 10
            self.formula()
            self.state = 11
            self.match(folParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PremisseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(folParser.FormulaContext)
            else:
                return self.getTypedRuleContext(folParser.FormulaContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.COMMA)
            else:
                return self.getToken(folParser.COMMA, i)

        def getRuleIndex(self):
            return folParser.RULE_premisse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPremisse" ):
                listener.enterPremisse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPremisse" ):
                listener.exitPremisse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPremisse" ):
                return visitor.visitPremisse(self)
            else:
                return visitor.visitChildren(self)




    def premisse(self):

        localctx = folParser.PremisseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_premisse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << folParser.LPAREN) | (1 << folParser.NOT) | (1 << folParser.PREPOSITION))) != 0):
                self.state = 13
                self.formula()


            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.COMMA:
                self.state = 16
                self.match(folParser.COMMA)
                self.state = 17
                self.formula()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WffContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(folParser.FormulaContext,0)


        def EOF(self):
            return self.getToken(folParser.EOF, 0)

        def getRuleIndex(self):
            return folParser.RULE_wff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWff" ):
                listener.enterWff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWff" ):
                listener.exitWff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWff" ):
                return visitor.visitWff(self)
            else:
                return visitor.visitChildren(self)




    def wff(self):

        localctx = folParser.WffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_wff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.formula()
            self.state = 24
            self.match(folParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._PREPOSITION = None # Token

        def PREPOSITION(self):
            return self.getToken(folParser.PREPOSITION, 0)

        def NOT(self):
            return self.getToken(folParser.NOT, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(folParser.FormulaContext)
            else:
                return self.getTypedRuleContext(folParser.FormulaContext,i)


        def LPAREN(self):
            return self.getToken(folParser.LPAREN, 0)

        def AND(self):
            return self.getToken(folParser.AND, 0)

        def RPAREN(self):
            return self.getToken(folParser.RPAREN, 0)

        def OR(self):
            return self.getToken(folParser.OR, 0)

        def IMPL(self):
            return self.getToken(folParser.IMPL, 0)

        def getRuleIndex(self):
            return folParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)




    def formula(self):

        localctx = folParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formula)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                localctx._PREPOSITION = self.match(folParser.PREPOSITION)
                print("matched a PREPOSITION", localctx._PREPOSITION, (None if localctx._PREPOSITION is None else localctx._PREPOSITION.text)) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(folParser.NOT)
                self.state = 29
                self.formula()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(folParser.LPAREN)
                self.state = 31
                self.formula()
                self.state = 32
                self.match(folParser.AND)
                self.state = 33
                self.formula()
                self.state = 34
                self.match(folParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.match(folParser.LPAREN)
                self.state = 37
                self.formula()
                self.state = 38
                self.match(folParser.OR)
                self.state = 39
                self.formula()
                self.state = 40
                self.match(folParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(folParser.LPAREN)
                self.state = 43
                self.formula()
                self.state = 44
                self.match(folParser.IMPL)
                self.state = 45
                self.formula()
                self.state = 46
                self.match(folParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





