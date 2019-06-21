grammar LambdaCalculus;

term 
    : VARIABLE
    | abstraction
    | application
    ;

abstraction
    : '%' VARIABLE '.' function*
    | LBRACKET abstraction RBRACKET
    ;

application
    : LBRACKET term term RBRACKET
    ;

function
    : expression operation expression
    | expression
    | term
    ;

expression
    : NUMBER
    | VARIABLE
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