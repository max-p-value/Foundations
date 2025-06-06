class ProteinTurnover:
    def __init__(self, transcription_rate, translation_rate, degradation_rate, mRNA_degradation_rate, dt=1.0):
        self.mRNA = 0.0
        self.protein = 0.0
        self.transcription_rate = transcription_rate
        self.translation_rate = translation_rate
        self.degradation_rate = degradation_rate
        self.mRNA_degradation_rate = mRNA_degradation_rate
        self.dt = dt
        self.time = 0.0
        self.history = []

    def step(self):
        self.mRNA += self.transcription_rate * self.dt
        self.mRNA -= self.mRNA_degradation_rate * self.mRNA * self.dt
        self.protein += self.translation_rate * self.mRNA * self.dt
        self.protein -= self.degradation_rate * self.protein * self.dt
        self.time += self.dt
        self.history.append((self.time, self.mRNA, self.protein))

    def run(self, steps):
        for _ in range(steps):
            self.step()