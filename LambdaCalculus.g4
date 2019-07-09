grammar LambdaCalculus;

term 
    : LBRACKET term RBRACKET
    | expression
    | application
    | abstraction
    ;

abstraction
    : LBRACKET abstraction RBRACKET
    | abstraction_term '.' function
    | abstraction_term '.' term
    ;

abstraction_term
    : '%' lambda_variable+
    ;

application
    : LBRACKET term RBRACKET term
    | abstraction expression
    | abstraction application
    | application abstraction
    | application term+
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