grammar LambdaCalculus;

/* Parser Rules */
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
    : '%' variable
    ;

function
    : value operation term
    | function operation term
    | abstraction operation term
    | LBRACKET function RBRACKET
    ;

value
    : number
    | boolean_value
    | variable
    | LBRACKET value RBRACKET
    ;

variable
    : VARIABLE
    | VARIABLE':'function_type
    ;

number
    : NUMBER
    | NUMBER':'function_type
    ;

boolean_value
    : BOOL
    | BOOL':'function_type
    ;

function_type
    : ground_type
    | function_type '->' function_type
    ;

ground_type
    : 'Bool'
    | 'bool'
    | 'BOOL'
    | 'Int'
    | 'int'
    | 'INT'
    | 'None'
    | 'none'
    | 'NONE'
    ;

operation
    : ADD
    | SUBTRACT
    | MULTIPLY
    | DIVIDE
    | POWER
    | AND
    | OR
    | GT
    | LT
    | EQ
    ;

/* Lexer rules */
NUMBER : [0-9]+ ;
BOOL : 'TRUE'|'true'|'True'|'FALSE'|'false'|'False' ;
VARIABLE : [a-zA-Z] ;
ADD : '+' ;
SUBTRACT : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/' ;
POWER : '^' ;
LBRACKET : '(' ;
RBRACKET : ')' ;
AND : '&' ;
OR : '|' ;
GT : '>' ;
LT : '<' ;
EQ : '==' ;

WS : [ \t\r\n]+ -> skip ;