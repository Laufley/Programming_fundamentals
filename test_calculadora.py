import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase) :
    def test_sumar_numeros_positivos(self) :
        resultado = sumar(5, 10)
        self.assertEqual(resultado, 15)

    def test_caso_con_bug(self) :
        resultado = sumar(2,2)
        self.assertAlmostEqual(resultado, 4) # this one should fail

if __name__ == "__main__":
    unittest.main()