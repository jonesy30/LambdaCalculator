grammar LambdaCalculus;

term 
    : variable
    | '%' variable '.' function* 
    | LBRACKET term RBRACKET
    ;

function
    : operation
    | NUMBER
    | term
    ;

variable
    : VARIABLE
    ;

operation
    : ADD
    | SUBTRACT
    | MULTIPLY
    | DIVIDE
    | POWER
    ;

VARIABLE : [a-z]+ ;
NUMBER : [0-9]+ ;
ADD : '+' ;
SUBTRACT : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/' ;
POWER : '^' ;
LBRACKET : '(' ;
RBRACKET : ')' ;

WS : [ \t\r\n]+ -> skip ;