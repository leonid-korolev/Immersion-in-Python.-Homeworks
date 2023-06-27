class Matrix:

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def __str__(self):
       
        # result = ''
        # for row in self.matrix:
        #     for elem in row:
        #         result += ''.join(f'{elem}\t')
        #     result += ''.join('\n')
        # return result
    
        for row in self.matrix:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

        # return '\n'.join(map(str, self.matrix))
    
    
    def comparing(self, other):
        result = ""
        if self.matrix < other.matrix:
            result = "Вторая матрица больше первой"
        elif self.matrix > other.matrix:
            result = "Первая матрица больше второй"
        else:
            result = "Матрицы равны"
        return result

    def __add__(self, other):
        result = []
        nums = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sum = self.matrix[i][j] + other.matrix[i][j]
                nums.append(sum)
                if len(nums) == len(self.matrix):
                    result.append(nums)
                    nums = []
        return result


if __name__ == "__main__":
    matrix_1 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
    matrix_2 = Matrix([[3, 4, 5], [6, 7, 8], [1, 2, 9]])
    matrix_sum = matrix_1 + matrix_2
    print(Matrix(matrix_sum))
    
    matrix_3 = Matrix([[7, 8, 9], [1, 2, 3], [3, 4, 6]])
    matrix_4 = Matrix([[7, 8, 9], [1, 2, 3]])
    mc = matrix_4.comparing(matrix_3)
    
    print(mc)


