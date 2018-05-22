import unittest
from activities import eat, nap, is_funny

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """ Eat should have a positive message for healthy eating """
        self.assertEqual(eat('broccoli', is_healthy=True), "I'm eating broccoli, because my body is a temple")

    def test_eat_unhealthy(self):
        self.assertEqual(eat('pizza', is_healthy=False), "I'm eating pizza, because YOLO")
    
    def test_short_nap(self):
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")

    def test_long_nap(self):
        self.assertEqual(nap(3), "Ugh I overslept")
    
    def test_is_funny_tim(self):
        self.assertEqual(is_funny('tim'), False)
    
    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

if __name__ == '__main__':
    unittest.main()