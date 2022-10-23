

class Matrix:
    def __init__(self,data):
        self.data=[[data]]
    def add_new_row(self, data):
        self.data.append([data])
        return print(f'You have Successfully Created A New Row' )
    
    def add_row_data(self, data,row):
        self.data[row].append(data)
        return print(f'You have Successfully Added {data} to row {row} ')     
    def print(self):     
        for i in self.data:
            print(i)
class Two_Dimensional_Matrix(Matrix):
       def __init__(self, data):
           super().__init__(data)
       def add_row_data(self, data, row):
           if len(self.data[row]<2):
             return print(f'This row is filled')    


def add_matrix(a,b):
  matrix=Matrix('New Data Created')   

  for i in range(len(a.data)-1):
    matrix.add_new_row(None)
    for j in range(len(a.data[i])-1):
        ans= a.data[i][j]+b.data[i][j]
        matrix.add_row_data(ans,i)
  return print(matrix.data)

matr= Matrix(3)

matr.add_new_row(4)

matr.add_row_data(2,0)
matr.add_row_data(3,0)


matr.add_row_data(2,1)
matr.add_row_data(3,1)
matr.print()
mat= Matrix(3)

mat.add_new_row(4)

mat.add_row_data(2,0)
mat.add_row_data(3,0)


mat.add_row_data(2,1)
mat.add_row_data(3,1)
mat.print()

add_matrix(matr,mat)