grammar LambdaCalculus;

term 
    : function
    | abstraction
    | application
    | value
    | parenthesis
    ;

parenthesis
    : LBRACKET term RBRACKET
    ;

abstraction
    : abstraction_term '.' term
    ;

abstraction_term
    : '%' lambda_variable
    ;

application
    : parenthesis term
    ;

function
    : value term
    | value operation term
    | operation term ',' term
    ;

value
    : number
    | variable
    ;

variable
    : VARIABLE
    ;

lambda_variable
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

VARIABLE : [a-zA-Z] ;
NUMBER : [0-9]+ ;
ADD : '+' ;
SUBTRACT : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/' ;
POWER : '^' ;
LBRACKET : '(' ;
RBRACKET : ')' ;

WS : [ \t\r\n]+ -> skip ;