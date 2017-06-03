class Parent():
    def __init__(self, last_name, eye_color):
        #print('Parent constructor called.')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)

# Inheritance
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        #print('Child constructor called.')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    # overriding methods
    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)
        # casting int to str
        print("Number of toys: " + str(self.number_of_toys))
        
billy_cyrus = Parent('Cyrus', 'blue')
miley_cyrus = Child('Cyrus','blue',5)
billy_cyrus.show_info()
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()
