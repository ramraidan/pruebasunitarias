# -*- coding: utf-8 -*-
import unittest

class TestCalculadora(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()

	def test_suma_de_2_mas_2(self):
		resultado = self.calc.suma(2,2)

		self.assertEqual(4,resultado)

	def test_suma_de_3_mas_3(self):

		resultado = self.calc.suma(3,3)
		self.assertEqual(6,resultado)

	def test_suma_de_5_mas_5(self):
	   	resultado = self.calc.suma(5,5)
		self.assertEqual(10,resultado)

class Calculadora():

	def suma(self,num1,num2):
		return num1+num2
		

if __name__ == '__main__':
	unittest.main()
