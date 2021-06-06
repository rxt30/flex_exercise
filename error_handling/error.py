def wrong_assignment_error(line):
    print("Wrong dataType for assignment")
    print("Datatype error on line " + str(line) + "\n")

def wrong_reassignment_error(line):
    print("Wrong dataType for reassignment")
    print("Datatype error on line " + str(line) + "\n")

def denominator_error(line):
    print("The denominator can not be zero")
    print("Mathematical error on line " + str(line) + "\n")

def variable_not_initiated_error(line):
    print("Variable not initiated")
    print("Access error on line " + str(line) + "\n")

def syntax_error(line):
    print("Syntax error on line " + str(line) + "\n")

def missing_semicolon_error():
    print("Missing semicolon on the last line\n")