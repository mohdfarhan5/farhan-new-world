#overiding
class Super:
    def employee_data(self):
        employee_data = dict()
        employee_data['name'] = 'Virat'
        employee_data['ctc'] = '20 lpa'
        print('Employee Details ', employee_data)

class Sub(Super):
    def employee_data(self):
        employee_data = dict()
        employee_data['name'] = 'Virat'
        employee_data['ctc'] = '20 lpa'
        employee_data['designation'] = 'SDE II'
        print('Employee Details ', employee_data)

s = Sub()
s.employee_data()


# overloading
class Main:
    def sum(self, x1= None, x2= None, x3= None):
        if x3 is None:
            print('Sum of two numbers: ', x1+x2)
        else:
            print('Sum of three numbers: ', x1+x2+x3)
m = Main()
m.sum(10, 20) # calling s
m.sum(10, 20, 30) # calling 