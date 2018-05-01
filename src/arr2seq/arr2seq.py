import numpy as np

class array_to_sequence:
    
    @staticmethod
    def convert(current_arr, next_arr, seq_in_len, seq_out_len):
        """Convert array's to sequence formating

        Parameters:
            current_arr (numpy_arr): The array u want to convert into sequence's
            next_arr (numpy_arr): The next chunk of the data 
            seq_in_len (int): Sequence in length
            seq_out_len (int): Sequence out length

        Returns:
            Array of sequence's
        """

        result_x = []
        result_y = []

        concatenate_arr = np.concatenate((current_arr, next_arr))
        concatenate_arr_len = len(concatenate_arr)

        for seq_in_start_index, _ in enumerate(current_arr):

            seq_in_end_index = seq_in_start_index + seq_in_len
            seq_out_end_index = seq_in_end_index + seq_out_len

            if seq_out_end_index > concatenate_arr_len: # Stop condition to prevent exceeding boundaries 
                break

            result_x.append(concatenate_arr[seq_in_start_index : seq_in_end_index])
            result_y.append(concatenate_arr[seq_in_end_index: seq_out_end_index])

        return  result_x,result_y