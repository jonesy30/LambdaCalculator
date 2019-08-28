grammar LambdaCalculus;

/* Parser Rules */
term 
    : abstraction
    | function
    | value
    | application
    ;

/* Formatted like this to avoid ANTLR's mutual-left-recursion issue between application and term */
application
    : application term 
    | abstraction term
    | value term
    | function term
    | LBRACKET application RBRACKET
    ;

/* Terms in the form %x.M */
abstraction
    : abstraction_term '.' term
    | LBRACKET abstraction RBRACKET
    ;

/* Used by abstraction in the form %x */
abstraction_term
    : '%' variable
    ;

/* Formatted like this to avoid ANTLR's mutual-left-recursion issue between application and function */
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

/* Each value can have an associated type given by the user through x:TYPE format */
variable
    : VARIABLE
    | VARIABLE':'function_type
    ;

/* Each value can have an associated type given by the user through x:TYPE format */
number
    : NUMBER
    | NUMBER':'function_type
    ;

/* Each value can have an associated type given by the user through x:TYPE format */
boolean_value
    : BOOL
    | BOOL':'function_type
    ;

/* A function type is just a type, called this because type is a keyword in python */
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

/* Ignore any whitespace */
WS : [ \t\r\n]+ -> skip ;