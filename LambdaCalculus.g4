grammar LambdaCalculus;

term 
    : value
    | function
    |abstraction
    | application
    ;

value
    : number
    | variable
    ;

function
    : value operation term
    | operation term ',' term
    | LBRACKET function RBRACKET
    ;

abstraction
    : abstraction_term '.' term
    | LBRACKET abstraction RBRACKET
    ;

abstraction_term
    : '%' lambda_variable
    ;

application
    : application term 
    | abstraction term
    | function term
    | value term
    | LBRACKET application RBRACKET
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