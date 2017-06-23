class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (float(location[0]), float(location[1]))
    def get_number_of_species(self, animal):
        if animal in self.species_types.keys():
            return self.species_types[animal]
        else:
            return 0
    def get_location(self):
        return self.location[:]
        
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name[:]
    def adopt_pet(self, species):
        self.species_types[species] -= 1
        if self.species_types[species] == 0:
            del self.species_types[species]
