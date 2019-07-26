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
    | VARIABLE':'term_type
    ;

lambda_variable
    : VARIABLE
    | VARIABLE':'term_type
    ;

number
    : NUMBER
    | NUMBER':'term_type
    ;

term_type
    : ground_type
    | term_type '->' term_type
    ;

ground_type
    : 'Bool'
    | 'bool'
    | 'BOOL'
    | 'Int'
    | 'int'
    | 'INT'
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