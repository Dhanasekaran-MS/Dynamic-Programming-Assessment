# def evaluate(tokens):
#     stack = []
#     for i in tokens:
#         # print(stack)
#         if i in '+-/*':
#             b = stack.pop()
#             a = stack.pop()
#             # print(a)
#             # print(b)
#             if i=='+':
#                 res = a+b
#             elif i=='-':
#                 res = a-b
#             elif i=='*':
#                 res = a*b  
#             elif i=='/':
#                 res = int(a/b)
#             stack.append(res)
#         else:
#             stack.append(int(i))
#     return stack[0]

def eval(tokens) :
    stack = []
    operators={
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a/b),
    }
    for i in tokens:
        if i in operators:
            b = stack.pop()
            a = stack.pop()
            res = operators[i](a,b)
            stack.append(res)
        else:
            stack.append(int(i))
    return stack[0]     

tokens = ['5', '10', '+', '20', '*', '5', '/'] 

print(eval(tokens))