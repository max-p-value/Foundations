class SignalingPathway:
    def __init__(self, ligand_onset=20.0):
        self.ligand_bound = False
        self.ligand_onset = ligand_onset
        self.receptor_active = False

    def step(self, dt, time):
        if time >= self.ligand_onset:
            self.ligand_bound = True
            self.receptor_active = True
        else:
            self.receptor_active = False