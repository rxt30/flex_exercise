from error_handling.error import variable_not_initiated_error

savedVariables = {}

def getVariable(name, line):
    if name in savedVariables:
        return savedVariables.get(name)
    else:
        variable_not_initiated_error(line)
