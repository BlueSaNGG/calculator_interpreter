from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("输入：")
        if text == "88":
            break
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree:
            continue
        interpreter = Interpreter()
        result = interpreter.visit(tree)
        print(result)
    except Exception as e:
        print(e)