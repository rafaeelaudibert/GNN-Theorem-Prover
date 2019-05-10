/*
* FOL originally written for Antlr3 by Stephan Opfer
*
* Ported to Antlr4 by Tom Everett
*
* Stripped down to PL by Boris Repasky and Suraj Narayanan S
*
* Updated by Rafael Baldasso Audibert to reflect the needs for the
* "End-to-End theorem prover using Typed Graph Networks" paper by
* Rafael Baldasso Audibert, INF, UFRGS, Brazil
*
*/

grammar fol;

options { language=Python3; }

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/

sequent
    : premisse ENTL formula EOF
    ;

premisse
    : formula? (COMMA formula)*
    ;

wff
    : formula EOF
    ;

formula
    : PREPOSITION {print("matched a PREPOSITION", $PREPOSITION, $PREPOSITION.text) }
    | NOT formula
    | LPAREN formula AND formula RPAREN
    | LPAREN formula OR formula RPAREN
    | LPAREN formula IMPL formula RPAREN
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

IMPL
    : '->'
    ;

AND
    : '&'
    ;

OR
    : '+'
    ;

NOT
    : '-'
    ;

COMMA
    : ','
    ;

ENTL
    : '=>'
    ;

PREPOSITION
    : ('a'..'z') CHARACTER* | 'T' | 'F'
    ;

fragment CHARACTER
    : ('0'..'9' | 'a'..'z' | '_')
    ;

WS
    : (' ' | '\t' | '\r' | '\n')+ ->skip
    ;