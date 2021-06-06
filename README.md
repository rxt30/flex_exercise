# Flex-Repository

Repository for making a compiler with ply.  
A more detailed guide can be found in the file `Documentation-Compiler.pdf`
If working on a new future/issue, please create your own branch and make a pull request after finishing it. Before merging the new PR please test wether the fix you made, broke soething else. Therefore the file 'tests/test_working.txt' can be used. The command for running the test is:
> python compiler.py -f tests/test_working.txt.

### Usage
A python interpreter is needed, it must be Python Version 3.6 or greater. After installing all the required programs, simply clone the project.
After cloning the repository, simply start the compiler with 
> python compiler.py [OPTION] [Filename]
If you run the compiler you can give it different options to customize the output to your liking. Without any option only the code in the print instruction gets printed onto the command line. These are the following different modes:
- Option -h: Shows a help menu with all options.
- Option -f: Use a file as input
- Option -v: Print the decoded syntax for every code section
- Option -t: Output the syntax tree corresponding to the code onto the command line
- Option -i: Output the syntax tree corresponding to the code as an image in the browser


### Structure
`compiler.py` serves as the Main-File for this compiler, and should be as short as possible.    
The lexical and syntax analysis will be imported from their respecting folders.    
`lexical/` includes the lexical analysis.    
`syntax/` includes the syntax analysis, but the syntax rules for the syntax trees itself should go into `syntax/rules` and the imported in `syntax/syntax.py`    
`tokens/` is the only directory, which defines all the tokens used in this compiler    
