import unittest

from torch import divide
from node import *
from interpreter import Interpreter
from value import Number

class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(51.2))
        self.assertEqual(value, Number(51.2))

    def test_individual_operations(self):
        value = Interpreter().visit(AddNode(NumberNode(99), NumberNode(100)))
        self.assertEqual(value, Number(199))

        value = Interpreter().visit(SubtractNode(NumberNode(199), NumberNode(99)))
        self.assertEqual(value, Number(100))

        value = Interpreter().visit(MultiplyNode(NumberNode(3), NumberNode(33)))
        self.assertEqual(value, Number(99))

        value = Interpreter().visit(DivideNode(NumberNode(99), NumberNode(3)))
        self.assertAlmostEqual(value.value, 33, 5)

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(77), NumberNode(0)))

    def test_full_expression(self):
        tree = AddNode(
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
        result = Interpreter().visit(tree)
        self.assertAlmostEqual(result.value, -2360.08, 2)