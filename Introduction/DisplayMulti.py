def DisplayMulti(*VarArgs):
    for Arg in VarArgs:
        if Arg.upper() == 'CONT':
            continue
            print('Continue Argument: ' + Arg)
        elif Arg.upper() == 'BREAK':
            break
            print('Break Argument: '+ Arg)
        print('Good Argument '+ Arg)
DisplayMulti("a", "b", "cont","c")
