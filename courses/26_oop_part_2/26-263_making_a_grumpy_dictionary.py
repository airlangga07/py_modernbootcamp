class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self, key):
        print("YOU WANT {}? WELL IT AINT HERE!".format(self.key))
    
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE.")
        super().__setitem__(key, value)

data = GrumpyDict({ "name": "Yoko", "city": "New York" })
print(data)
data['name'] = 'Chris'
print(data)