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

open Parsing;;
let _ = parse_error;;
# 1 "parser.mly"
open Interface
# 20 "parser.ml"
let yytransl_const = [|
  257 (* LPAR *);
  258 (* RPAR *);
  259 (* NOT *);
  260 (* IMP *);
  261 (* EQU *);
  262 (* DISJ *);
  263 (* CONJ *);
  264 (* FALSE *);
  266 (* EOL *);
  267 (* ASSUME *);
  268 (* THEREFORE *);
    0|]

let yytransl_block = [|
  265 (* VAR *);
    0|]

let yylhs = "\255\255\
\003\000\003\000\003\000\003\000\003\000\003\000\003\000\003\000\
\001\000\002\000\002\000\002\000\000\000\000\000"

let yylen = "\002\000\
\001\000\001\000\003\000\002\000\003\000\003\000\003\000\003\000\
\002\000\003\000\003\000\002\000\002\000\002\000"

let yydefred = "\000\000\
\000\000\000\000\000\000\000\000\000\000\001\000\002\000\013\000\
\000\000\000\000\000\000\014\000\000\000\000\000\004\000\000\000\
\000\000\000\000\000\000\009\000\000\000\000\000\012\000\003\000\
\000\000\000\000\000\000\008\000\010\000\011\000"

let yydgoto = "\003\000\
\008\000\012\000\009\000"

let yysindex = "\004\000\
\027\255\010\255\000\000\027\255\027\255\000\000\000\000\000\000\
\034\255\027\255\027\255\000\000\041\255\062\255\000\000\027\255\
\027\255\027\255\027\255\000\000\048\255\055\255\000\000\000\000\
\066\255\066\255\250\254\000\000\000\000\000\000"

let yyrindex = "\000\000\
\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
\002\255\032\255\021\255\000\000\000\000\000\000"

let yygindex = "\000\000\
\000\000\000\000\254\255"

let yytablesize = 73
let yytable = "\013\000\
\019\000\014\000\015\000\005\000\001\000\002\000\005\000\021\000\
\022\000\000\000\004\000\005\000\005\000\025\000\026\000\027\000\
\028\000\006\000\007\000\000\000\010\000\011\000\007\000\000\000\
\007\000\007\000\007\000\004\000\000\000\005\000\007\000\000\000\
\000\000\006\000\006\000\007\000\006\000\016\000\017\000\018\000\
\019\000\006\000\000\000\020\000\016\000\017\000\018\000\019\000\
\000\000\000\000\023\000\016\000\017\000\018\000\019\000\000\000\
\000\000\029\000\016\000\017\000\018\000\019\000\000\000\024\000\
\030\000\016\000\017\000\018\000\019\000\016\000\000\000\018\000\
\019\000"

let yycheck = "\002\000\
\007\001\004\000\005\000\002\001\001\000\002\000\005\001\010\000\
\011\000\255\255\001\001\010\001\003\001\016\000\017\000\018\000\
\019\000\008\001\009\001\255\255\011\001\012\001\002\001\255\255\
\004\001\005\001\006\001\001\001\255\255\003\001\010\001\255\255\
\255\255\002\001\008\001\009\001\005\001\004\001\005\001\006\001\
\007\001\010\001\255\255\010\001\004\001\005\001\006\001\007\001\
\255\255\255\255\010\001\004\001\005\001\006\001\007\001\255\255\
\255\255\010\001\004\001\005\001\006\001\007\001\255\255\002\001\
\010\001\004\001\005\001\006\001\007\001\004\001\255\255\006\001\
\007\001"

let yynames_const = "\
  LPAR\000\
  RPAR\000\
  NOT\000\
  IMP\000\
  EQU\000\
  DISJ\000\
  CONJ\000\
  FALSE\000\
  EOL\000\
  ASSUME\000\
  THEREFORE\000\
  "

let yynames_block = "\
  VAR\000\
  "

let yyact = [|
  (fun _ -> failwith "parser")
; (fun __caml_parser_env ->
    Obj.repr(
# 29 "parser.mly"
                                 (False)
# 120 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 0 : string) in
    Obj.repr(
# 30 "parser.mly"
           (Var _1)
# 127 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _2 = (Parsing.peek_val __caml_parser_env 1 : Interface.formula) in
    Obj.repr(
# 31 "parser.mly"
                      (_2)
# 134 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _2 = (Parsing.peek_val __caml_parser_env 0 : Interface.formula) in
    Obj.repr(
# 32 "parser.mly"
                 (Neg _2)
# 141 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 2 : Interface.formula) in
    let _3 = (Parsing.peek_val __caml_parser_env 0 : Interface.formula) in
    Obj.repr(
# 33 "parser.mly"
                        (Imp (_1,_3))
# 149 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 2 : Interface.formula) in
    let _3 = (Parsing.peek_val __caml_parser_env 0 : Interface.formula) in
    Obj.repr(
# 34 "parser.mly"
                                 (Equiv (_1,_3))
# 157 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 2 : Interface.formula) in
    let _3 = (Parsing.peek_val __caml_parser_env 0 : Interface.formula) in
    Obj.repr(
# 35 "parser.mly"
                                 (Disj (_1,_3))
# 165 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 2 : Interface.formula) in
    let _3 = (Parsing.peek_val __caml_parser_env 0 : Interface.formula) in
    Obj.repr(
# 36 "parser.mly"
                                 (Conj (_1,_3))
# 173 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 1 : Interface.formula) in
    Obj.repr(
# 40 "parser.mly"
                                        (_1)
# 180 "parser.ml"
               : Interface.formula))
; (fun __caml_parser_env ->
    let _2 = (Parsing.peek_val __caml_parser_env 1 : Interface.formula) in
    Obj.repr(
# 46 "parser.mly"
                               (Assume _2)
# 187 "parser.ml"
               : Interface.line))
; (fun __caml_parser_env ->
    let _2 = (Parsing.peek_val __caml_parser_env 1 : Interface.formula) in
    Obj.repr(
# 47 "parser.mly"
                                (Therefore _2)
# 194 "parser.ml"
               : Interface.line))
; (fun __caml_parser_env ->
    let _1 = (Parsing.peek_val __caml_parser_env 1 : Interface.formula) in
    Obj.repr(
# 48 "parser.mly"
                               (Usable _1)
# 201 "parser.ml"
               : Interface.line))
(* Entry formula_alone *)
; (fun __caml_parser_env -> raise (Parsing.YYexit (Parsing.peek_val __caml_parser_env 0)))
(* Entry line *)
; (fun __caml_parser_env -> raise (Parsing.YYexit (Parsing.peek_val __caml_parser_env 0)))
|]
let yytables =
  { Parsing.actions=yyact;
    Parsing.transl_const=yytransl_const;
    Parsing.transl_block=yytransl_block;
    Parsing.lhs=yylhs;
    Parsing.len=yylen;
    Parsing.defred=yydefred;
    Parsing.dgoto=yydgoto;
    Parsing.sindex=yysindex;
    Parsing.rindex=yyrindex;
    Parsing.gindex=yygindex;
    Parsing.tablesize=yytablesize;
    Parsing.table=yytable;
    Parsing.check=yycheck;
    Parsing.error_function=parse_error;
    Parsing.names_const=yynames_const;
    Parsing.names_block=yynames_block }
let formula_alone (lexfun : Lexing.lexbuf -> token) (lexbuf : Lexing.lexbuf) =
   (Parsing.yyparse yytables 1 lexfun lexbuf : Interface.formula)
let line (lexfun : Lexing.lexbuf -> token) (lexbuf : Lexing.lexbuf) =
   (Parsing.yyparse yytables 2 lexfun lexbuf : Interface.line)
