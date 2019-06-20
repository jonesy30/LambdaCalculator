grammar LambdaCalculus;
lambda : '/' VARIABLE '.' VARIABLE ;
VARIABLE : [a-z]+ ;
WS : [ \t\r\n]+ -> skip ;