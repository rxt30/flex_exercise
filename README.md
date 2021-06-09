# Flex-Repository

Repository for making a compiler with ply.  
A more detailed guide can be found in the file `Documentation-Compiler.pdf`
If working on a new future/issue, please create your own branch and make a pull request after finishing it. Before merging the new PR please test wether the fix you made, broke soething else. Therefore the file 'tests/test_working.txt' can be used. The command for running the test is:    
```python compiler.py -f tests/test_working.txt```.

## Usage
A prebuild binary can be found on the [release page](https://github.com/rxt30/flex_exercise/releases).
### Run on Linux
Start the compiler with the following command:
```./compiler_linux [OPTIONS]```
### Run on Windows
To run the compiler windows, open up a command line of your choice and start the compiler with the following command:
```compiler_windows.exe [OPTIONS]```
### Run from Source Code
If you intend to run the compiler directly from the source code instead of using a prebuild binary, you must install [Python 3.6 or greater and pip](https://www.python.org/downloads/release/python-395/).    
After installing python and pip, install ply with the following command:
```pip3 install ply```     
After cloning the repository, simply start the compiler with the following command:
```python compiler.py [OPTIONS]```
### Options
|Option|Description|
|---|---|
| -h | Show the help menu with all options |
| -f [FILENAME] | Compile a file |
| -v | Verbose, print the decoded syntax for every code section |
| -t | Output the syntax tree corresponding to the code onto the command line |
| -i | Output the syntax tree correspoding to the code as an image in the browser |

## Structure
`compiler.py` serves as the Main-File for this compiler, and should be as short as possible.    
The lexical and syntax analysis will be imported from their respecting folders.    
`lexical/` includes the lexical analysis.    
`syntax/` includes the syntax analysis, but the syntax rules for the syntax trees itself should go into `syntax/rules` and the imported in `syntax/syntax.py`    
`tokens/` is the only directory, which defines all the tokens used in this compiler    
