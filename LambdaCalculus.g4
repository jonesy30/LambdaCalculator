grammar LambdaCalculus;

term 
    : function
    | abstraction
    | application
    | value
    ;

abstraction
    : abstraction_term '.' term
    | LBRACKET abstraction RBRACKET
    ;

abstraction_term
    : '%' lambda_variable
    ;

application
    : function term
    | abstraction term
    | application term
    | value term
    | LBRACKET application RBRACKET
    ;

function
    : value operation term
    | operation term ',' term
    | LBRACKET function RBRACKET
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