%{
int rowCount = 0;
%}

%%
//Keywords
int         {return INTEGER;}
string      {return STRING;}
bool        {return BOOLEAN;}

//Controll-Keywords
if          {return IF;}
for         {return FOR;}
while       {return WHILE;}
true        {return TRUE;}
false       {return FALSE;}
\|\|        {return OR;}
&&          {return AND;}

//Operators
\+|-|\*     {return CALC_OPERATION;}
=           {return ASSIGNMENT;}
!           {return INVERSE;}
<           {return RIGHT_GREATER;}
>           {return LEFT_GREATER;}

//Other stuff
[A-Za-z]*   {return CHARS;}
[0-9]*      {return NUMBER;}
;|\n|\r\n           {rowCount++;return LINE_END;}


//Braces
\(          {return ROUND_START;}
\)          {return ROUND_END;}
\{          {return CURLY_START;}
\}          {return CURLY_END;}


.           {printf("Invalid Character");
             return INVALID;}
%%

int yywrap(){}
int main(int argc, char *argv[]){
    if( argc != 2){
        printf("No or to many arguments supplied.\n");
        printf("Please use the program like this:\n");
        printf("./a.out <Filename>");
        return 0;
    }
    FILE *fp;
    fp = fopen(argv[1],"r");
    yyin = fp;
    yylex(); 
    return 0;
}
