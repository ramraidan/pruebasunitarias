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

	def test_resta_de_9_menos_3(self):
		resultado = self.calc.resta(9,3)
		self.assertEqual(6,resultado)

	def test_resta_de_50_menos_25(self):
		resultado = self.calc.resta(50,25)
		self.assertEqual(25,resultado)

	def test_resta_de_10_menos_10(self):
		resultado = self.calc.resta(10,10)
		self.assertEqual(0,resultado)

class Calculadora():

	def suma(self,num1,num2):
		return num1+num2
		
	def resta(self,num1,num2):
	    return num1-num2

if __name__ == '__main__':
	unittest.main()
