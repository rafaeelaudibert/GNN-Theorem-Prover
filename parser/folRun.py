import sys
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
from antlr4.tree.Trees import Trees
from pprint import pprint as pp
 
def main():
    input_stream = FileStream('/home/rafael/Documents/theorem_prover/parser/input.txt')
    lexer = folLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = folParser(stream)
    tree = parser.sequent()

    pp(Trees.toStringTree(tree, None, parser))
 
if __name__ == '__main__':
    main()