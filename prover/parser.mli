type token =
  | LPAR
  | RPAR
  | NOT
  | IMP
  | EQU
  | DISJ
  | CONJ
  | FALSE
  | VAR of (string)
  | EOL
  | ASSUME
  | THEREFORE

val formula_alone :
  (Lexing.lexbuf  -> token) -> Lexing.lexbuf -> Interface.formula
val line :
  (Lexing.lexbuf  -> token) -> Lexing.lexbuf -> Interface.line
