import unittest
import ddt




@ddt.ddt
class IntegerArithmeticTestCase(unittest.TestCase):

    @ddt.file_data('d1.json')
    @ddt.unpack

    def testAdd(self,first,second,value):
        self.assertEqual((first + second),value)



    if __name__ == '__main__':
        unittest.main(verbosity=2)