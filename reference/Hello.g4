grammar Hello;

hi : 'hello' ID ;

ID : [a-z]+ ;
WS : [ \t\r\n]+ -> skip ;