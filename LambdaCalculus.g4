grammar LambdaCalculus;
expression 
    : variable
    | '%' variable '.' function* 
    ;

function
    : operation
    | variable
    | NUMBER
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

WS : [ \t\r\n]+ -> skip ;