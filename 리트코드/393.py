class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        num_of_byte = 0
        for num in data:
            print(bin(num), num_of_byte)
            if num_of_byte == 0:
                if num >> 3 == 0b11110:
                    num_of_byte = 3
                elif num >> 4 == 0b1110:
                    num_of_byte = 2
                elif num >> 5 == 0b110:
                    num_of_byte = 1
                elif num >> 7 == 0b0:
                    num_of_byte = 0
                else:
                    return False

            else:
                num_of_byte -= 1
                if num >> 6 != 0b10:
                    return False

        if num_of_byte == 0:
            return True
        else:
            return False


print(Solution.validUtf8(None, [197, 130, 1]))