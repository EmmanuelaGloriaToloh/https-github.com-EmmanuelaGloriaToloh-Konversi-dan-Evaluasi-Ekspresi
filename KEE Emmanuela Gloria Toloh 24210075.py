def toPostfix(expr: str):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    tokens = tokenize(expr)

    for token in tokens:
        if token.isdigit() or isFloat(token):
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Unbalanced parenthesis")
            stack.pop()  # Pop the '('
    while stack:
        if stack[-1] in '()':
            raise ValueError("Unbalanced parenthesis")
        output.append(stack.pop())
    return output

def evalPostfix(tokens):
    stack = []
    for token in tokens:
        if token.isdigit() or isFloat(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

def tokenize(expr):
    tokens = []
    number = ''
    for char in expr:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                tokens.append(number)
                number = ''
            if char in '+-*/()':
                tokens.append(char)
    if number:
        tokens.append(number)
    return tokens

def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Loop input dari pengguna
while True:
    infix_expr = input("Masukkan ekspresi matematika (atau ketik 'exit' untuk keluar): ")
    
    if infix_expr.lower() == 'exit':
        print("Program selesai.")
        break

    try:
        postfix_tokens = toPostfix(infix_expr)
        print("Postfix:", postfix_tokens)
        result = evalPostfix(postfix_tokens)

        # Tampilkan bilangan bulat jika hasilnya bulat
        if result == int(result):
            print("Evaluasi:", int(result))
        else:
            print("Evaluasi:", result)
    except Exception as e:
        print("Terjadi kesalahan:", e)