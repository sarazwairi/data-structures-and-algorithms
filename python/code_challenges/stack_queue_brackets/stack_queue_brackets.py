open_bracket=["[","{","("]
close_bracket=["]","}",")"]

def  validate_brackets(str):
    stack=[]
    for i in str:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            y=close_bracket.index(i)
            if (len(stack)>0) and (open_bracket(y)==stack[len(stack)-1]):
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False

