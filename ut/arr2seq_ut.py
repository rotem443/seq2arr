import unittest
import numpy as np
from src.arr2seq.arr2seq import array_to_sequence

class array_to_sequence_ut(unittest.TestCase):
    
    def test_seq_in_3_len_out_1(self):

        current_arr = np.arange(5)
        next_arr = np.arange(5,10)
        seq_in_len = 3
        seq_out_len = 1

        result_x, result_y = array_to_sequence.convert(current_arr, next_arr, seq_in_len, seq_out_len)
        
        expected_result_x = np.array([[0,1,2],[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
        expected_result_y = np.array([[3],[4],[5],[6],[7]])

        self.assertTrue((result_x == expected_result_x).all())
        self.assertTrue((result_y == expected_result_y).all())

    def test_seq_in_1_len_out_1(self):

        current_arr = np.arange(5)
        next_arr = np.arange(5,10)
        seq_in_len = 1
        seq_out_len = 1

        result_x, result_y = array_to_sequence.convert(current_arr, next_arr, seq_in_len, seq_out_len)
        
        expected_result_x = np.array([[0],[1],[2],[3],[4]])
        expected_result_y = np.array([[1],[2],[3],[4],[5]])

        self.assertTrue((result_x == expected_result_x).all())
        self.assertTrue((result_y == expected_result_y).all())
        
    def test_seq_in_1_len_out_3(self):

        current_arr = np.arange(5)
        next_arr = np.arange(5,10)
        seq_in_len = 1
        seq_out_len = 3

        result_x, result_y = array_to_sequence.convert(current_arr, next_arr, seq_in_len, seq_out_len)
        
        expected_result_x = np.array([[0],[1],[2],[3],[4]])
        expected_result_y = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]])

        self.assertTrue((result_x == expected_result_x).all())
        self.assertTrue((result_y == expected_result_y).all())

    def test_seq_in_almost_border_exceede(self):

        current_arr = np.arange(5)
        next_arr = np.arange(5,10)
        seq_in_len = 5
        seq_out_len = 1

        result_x, result_y = array_to_sequence.convert(current_arr, next_arr, seq_in_len, seq_out_len)
        
        expected_result_x = np.array([[0,1,2,3,4],[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]])
        expected_result_y = np.array([[5],[6],[7],[8],[9]])

        self.assertTrue((result_x == expected_result_x).all())
        self.assertTrue((result_y == expected_result_y).all())

    def test_seq_in_border_exceede(self):

        current_arr = np.arange(5)
        next_arr = np.arange(5,10)
        seq_in_len = 6
        seq_out_len = 1

        result_x, result_y = array_to_sequence.convert(current_arr, next_arr, seq_in_len, seq_out_len)
        
        expected_result_x = np.array([[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]])
        expected_result_y = np.array([[6],[7],[8],[9]])

        self.assertTrue((result_x == expected_result_x).all())
        self.assertTrue((result_y == expected_result_y).all())


if __name__ == "__main__":
    unittest.main()