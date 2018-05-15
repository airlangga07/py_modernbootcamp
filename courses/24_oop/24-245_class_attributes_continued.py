class Pet:
    # class attributes
    allowed = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError("You can't have a {} pet!".format(species))
        self.name = name
        self.species = species
    
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError("You can't have a {} pet!".format(species))
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
tiger = Pet("Tony", "tiger")