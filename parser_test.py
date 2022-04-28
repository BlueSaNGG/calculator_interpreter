import unittest

from numpy import number
from tokens import Token, TokenType
from parser_ import Parser
from node import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 51.2)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_individual_operations(self):
        #add
        tokens = [
            Token(TokenType.NUMBER, 5),
            Token(TokenType.PLUS, None),
            Token(TokenType.NUMBER, 7),
            ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(5), NumberNode(7)))

        #subtract
        tokens = [
            Token(TokenType.NUMBER, 7),
            Token(TokenType.MINUS, None),
            Token(TokenType.NUMBER, 5),
            ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(7), NumberNode(5)))

        #multiply
        tokens = [
            Token(TokenType.NUMBER, 4),
            Token(TokenType.MULTIPLY, None),
            Token(TokenType.NUMBER, 5),
            ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(4), NumberNode(5)))

        #divide
        tokens = [
            Token(TokenType.NUMBER, 5),
            Token(TokenType.DIVIDE, None),
            Token(TokenType.NUMBER, 8),
            ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(5), NumberNode(8)))

        #expr
    def test_full_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS, None),
            Token(TokenType.LPAREN, None),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.DIVIDE, None),
            Token(TokenType.NUMBER, 36),
            Token(TokenType.MINUS, None),
            Token(TokenType.NUMBER, 48),
            Token(TokenType.RPAREN, None),
            Token(TokenType.MULTIPLY, None),
            Token(TokenType.NUMBER, 51),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, 
            AddNode(
                NumberNode(27),
                MultiplyNode(
                    SubtractNode(
                        DivideNode(
                            NumberNode(43),
                            NumberNode(36)
                        ),
                        NumberNode(48)
                    ),
                    NumberNode(51)
                )
            )
        )