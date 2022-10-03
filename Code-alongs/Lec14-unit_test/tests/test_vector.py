from __future__ import annotations
import sys, os
import unittest


print(__file__)

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))

# we define a path that is up one step
# in this path we have vector.py and plotter.py and manual_testing.ipynb
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)
print(path_to_vector_module)

from vector import Vector


class TestVector(unittest.TestCase):
    #setUP körs automatiskt och ger attributes that we can use later on (1 och 2)
    def setUp(self):
        self.x, self.y = 1, 2

    def create_2D_vector(self) -> Vector: #automatically generate 2D vectors for testing
        """Testing numbers property"""
        return Vector (self.x, self.y)

    def test_create_2D_vector(self):
        # v = Vector(1,2) not needed since have create_2D_vector
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))

    def test_create_3D_vector(self):
        v = Vector(1,2,3)
        self.assertEqual(v.numbers, (1,2,3))

    def test_create_empty_vector(self): #vill ha felmeddelandet
        #testing if len(nimbers) <= 0 
        with self.assertRaises(ValueError): # with istället för try/except
            v = Vector()

    def test_equal_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1, v2)
    
    def test_not_equal_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(-1,-2)
        self.assertNotEqual(v1, v2)

    def test_add_2_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector (1,3)
        self.assertEqual(v1+v2, Vector(self.x+1, self.y+3))
    
    def test_getitem(self):
        v1 = self.create_2D_vector()

        # tideous so loop as below instead
        #self.assertEqual(v1[0], 1)
        #self.assertEqual(v1[1], 2)

        # i = 0, number = 1
        # i = 1, number = 2
        for i, number in enumerate((1,2)):
            self.assertEqual(v1[i], number)
        
    # TODO: many more tests can be performed


class TestVector2(unittest.TestCase):
    def test_create_2D_vector(self):
        v = Vector(1,2)
        self.assertEqual(v.numbers, (1,2))
    
    
    


# nedanstående rader kör testet
if __name__ == "__main__":
    unittest.main()
