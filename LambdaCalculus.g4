grammar LambdaCalculus;

term 
    : abstraction
    | function
    | value
    | application
    ;

application
    : application term 
    | abstraction term
    | value term
    | function term
    | LBRACKET application RBRACKET
    ;

abstraction
    : abstraction_term '.' term
    | LBRACKET abstraction RBRACKET
    ;

abstraction_term
    : '%' lambda_variable
    ;

function
    : value operation term
    | function operation term
    | abstraction operation term
    | LBRACKET function RBRACKET
    ;

value
    : number
    | variable
    | LBRACKET value RBRACKET
    ;

variable
    : VARIABLE
    | VARIABLE':''Bool'
    | VARIABLE':''bool'
    | VARIABLE':''BOOL'
    | VARIABLE':''Int'
    | VARIABLE':''int'
    | VARIABLE':''INT'
    ;

lambda_variable
    : VARIABLE
    | VARIABLE':''Bool'
    | VARIABLE':''bool'
    | VARIABLE':''BOOL'
    | VARIABLE':''Int'
    | VARIABLE':''int'
    | VARIABLE':''INT'
    ;

number
    : NUMBER
    | NUMBER':''Bool'
    | NUMBER':''bool'
    | NUMBER':''BOOL'
    | NUMBER':''Int'
    | NUMBER':''int'
    | NUMBER':''INT'
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