class Compartment:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
        self.molecules = {}  # e.g., {'proteinA': 250.0}

    def add(self, molecule, amount):
        self.molecules[molecule] = self.molecules.get(molecule, 0) + amount

    def degrade(self, molecule, amount):
        self.molecules[molecule] = max(self.molecules.get(molecule, 0) - amount, 0)

    def concentration(self, molecule):
        return self.molecules.get(molecule, 0) / self.volume
