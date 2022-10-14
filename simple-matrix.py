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
matr= Matrix(3)

matr.add_new_row(4)

matr.add_row_data(2,0)
matr.add_row_data(3,0)


matr.add_row_data(2,1)
matr.add_row_data(3,1)
matr.print()