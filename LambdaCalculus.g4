grammar LambdaCalculus;

term 
    : variable
    | abstraction
    | application
    ;

abstraction_term
    : '%' variable
    ;

value_term
    : abstraction number
    ;

abstraction
    : LBRACKET abstraction RBRACKET
    | abstraction_term '.' function
    ;

application
    : value_term
    | abstraction application
    | application term
    | application expression
    | LBRACKET term+ RBRACKET
    ;

function
    : expression operation expression
    | expression operation term
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