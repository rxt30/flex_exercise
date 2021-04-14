%{
int count = 0;
%}

%%
[A-Z]   {printf("%s capital letter\n", yytext);
         count++;}
.       {printf("%s not a capital letter\n", yytext);
         count++;} 
\n      {return 0;}
%%

int yywrap(){}
int main(int argc, char *argv[]){
    if( argc != 2){
        printf("No or to many arguments supplied.\n");
        printf("Please use the program like this:\n");
        printf("./a.out <Filename>");
        return 0;
    }
    printf("%s",argv[1]);
    FILE *fp;
    fp = fopen(argv[1],"r");
    yyin = fp;
    yylex(); 
    return 0;
}
