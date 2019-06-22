grammar LambdaCalculus;

term 
    : variable
    | abstraction
    | application
    ;

abstraction
    : LBRACKET abstraction RBRACKET
    | '%' variable '.' function
    ;

application
    : LBRACKET term term RBRACKET
    | application term
    | application expression
    | abstraction expression
    ;

function
    : expression operation expression
    | expression
    | term
    ;

expression
    : number
    | variable
    ;

variable
    : VARIABLE
    ;

number
    : NUMBER
    ;

operation
    : ADD
    | SUBTRACT
    | MULTIPLY
    | DIVIDE
    | POWER
    ;

VARIABLE : [a-zA-Z]+ ;
NUMBER : [0-9]+ ;
ADD : '+' ;
SUBTRACT : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/' ;
POWER : '^' ;
LBRACKET : '(' ;
RBRACKET : ')' ;

WS : [ \t\r\n]+ -> skip ;