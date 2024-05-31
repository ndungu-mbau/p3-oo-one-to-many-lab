class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

    def add_owner(self, owner):
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not a valid pet")
        pet.add_owner(self)

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
