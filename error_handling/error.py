def wrong_assignment_error(line):
    print("Wrong dataType for assignment")
    print("Syntax error on line " + str(line) + "\n")
    raise SyntaxError


def wrong_reassignment_error(line):
    print("Wrong dataType for reassignment")
    print("Syntax error on line " + str(line) + "\n")
    raise SyntaxError
