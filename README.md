# Flex-Repository

Repository for making a compiler with ply 
If you want to have a look at the language the compiler can work with you can have a look at the file '' 
If working on a new future/issue, please create your own branch and make a pull request after finishing it. Before merging the new PR please test wether the fix you made, broke soething else. Therefore the file 'tests_working.txt' can be used. The command for running the test is:
> python compiler.py tests_working.txt.

### Usage
A python interpreter is needed, it must be Python Version 3.6 or greater.
After installing all the required programs, simply clone the project.    
After cloning the repository, simply start the compiler with `python compiler.py`.    
To compile a file, start the compiler as following: `python compiler.py <filename>`    

### Structure
`compiler.py` serves as the Main-File for this compiler, and should be as short as possible.    
The lexical and syntax analysis will be imported from their respecting folders.    
`lexical/` includes the lexical analysis.    
`syntax/` includes the syntax analysis, but the syntax rules for the syntax trees itself should go into `syntax/rules` and the imported in `syntax/syntax.py`    
`tokens/` is the only directory, which defines all the tokens used in this compiler    

### Documentation

All the documentation for this compiler can be foun in the directory `documentation`
If you want to have a look at the current status and the future plans, just visit the file `current_implementation.xlsx`.
