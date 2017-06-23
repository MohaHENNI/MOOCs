class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self,name,desired_species,considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    def get_score(self, adoption_center):
        count = 0.0
        for species in self.considered_species:      
            if species != self.desired_species: 
                count += float(adoption_center.get_number_of_species(species))
            
        return float(Adopter.get_score(self, adoption_center)) + 0.3*count


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name,desired_species)
        self.feared_species = feared_species
    def get_score(self, adoption_center):
        count = 0.0
        for species in self.feared_species:
            if species != self.desired_species:
                count += float(adoption_center.get_number_of_species(species))
        return float(Adopter.get_score(self, adoption_center)) - 0.3*count
