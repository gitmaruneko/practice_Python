from unittest import TestCase
from src.s00.Math import Math


class TestSolver(TestCase):

    def test_negative_discr(self):
        s = Math()
        self.assertRaises(Exception,s.solver,2,1,2)