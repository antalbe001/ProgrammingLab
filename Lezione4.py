#inizio con il pseudocodice

#oggetto CSVfile
#   -init(filename)
#   -name
#   -get_data()
#    return dati

class CSVfile:
    def __init__(self, name):

        self.name = name

    def get_data(self):

        values = []

        my_file = open(self.name, 'r')

        for line in my_file:
            elements = line.split(',')

            if elements[0] != 'Date':
                date  = elements[0]
                value = elements[1]

                values.append(float(value))

        return values

mio_file=CSVfile(name='shampoo_sales.csv')

print(mio_file.name)
print(mio_file.get_data())