# Generated from fol.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write(">\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\7\n.\n\n\f\n\16\n\61\13\n\3\n\5\n\64\n")
        buf.write("\n\3\13\3\13\3\f\6\f9\n\f\r\f\16\f:\3\f\3\f\2\2\r\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\f\3\2\5")
        buf.write("\4\2HHVV\5\2\62;aac|\5\2\13\f\17\17\"\"\2?\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\27\3")
        buf.write("\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t \3\2\2")
        buf.write("\2\13\"\3\2\2\2\r$\3\2\2\2\17&\3\2\2\2\21(\3\2\2\2\23")
        buf.write("\63\3\2\2\2\25\65\3\2\2\2\278\3\2\2\2\31\32\7*\2\2\32")
        buf.write("\4\3\2\2\2\33\34\7+\2\2\34\6\3\2\2\2\35\36\7/\2\2\36\37")
        buf.write("\7@\2\2\37\b\3\2\2\2 !\7(\2\2!\n\3\2\2\2\"#\7-\2\2#\f")
        buf.write("\3\2\2\2$%\7/\2\2%\16\3\2\2\2&\'\7.\2\2\'\20\3\2\2\2(")
        buf.write(")\7?\2\2)*\7@\2\2*\22\3\2\2\2+/\4c|\2,.\5\25\13\2-,\3")
        buf.write("\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\64\3\2\2\2")
        buf.write("\61/\3\2\2\2\62\64\t\2\2\2\63+\3\2\2\2\63\62\3\2\2\2\64")
        buf.write("\24\3\2\2\2\65\66\t\3\2\2\66\26\3\2\2\2\679\t\4\2\28\67")
        buf.write("\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\f")
        buf.write("\2\2=\30\3\2\2\2\6\2/\63:\3\b\2\2")
        return buf.getvalue()


class folLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    IMPL = 3
    AND = 4
    OR = 5
    NOT = 6
    COMMA = 7
    ENTL = 8
    PREPOSITION = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'->'", "'&'", "'+'", "'-'", "','", "'=>'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "IMPL", "AND", "OR", "NOT", "COMMA", "ENTL", 
            "PREPOSITION", "WS" ]

    ruleNames = [ "LPAREN", "RPAREN", "IMPL", "AND", "OR", "NOT", "COMMA", 
                  "ENTL", "PREPOSITION", "CHARACTER", "WS" ]

    grammarFileName = "fol.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


