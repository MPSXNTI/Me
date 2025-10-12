import unittest
from vehiculos.auto import Auto
from vehiculos.bicicleta import Bicicleta

class VehiculosTest(unittest.TestCase):
    def test_encapsulamiento_y_movimiento(self):
        a = Auto("Toyota")
        b = Bicicleta("Trek")
        a.acelerar(10); a.acelerar(5)
        b.acelerar(7)
        self.assertEqual(a.velocidad, 15)
        self.assertEqual(b.velocidad, 7)
        self.assertIn("Auto Toyota", a.mover())
        self.assertIn("Bici Trek", b.mover())

    def test_frenar_no_negativo(self):
        a = Auto("Toyota")
        a.acelerar(10)
        a.frenar(15)  # no baja de 0
        self.assertEqual(a.velocidad, 0)

    def test_validacion_delta(self):
        a = Auto("Toyota")
        with self.assertRaises(ValueError):
            a.acelerar(-1)
        with self.assertRaises(ValueError):
            a.frenar(-2)

if __name__ == '__main__':
    unittest.main()
