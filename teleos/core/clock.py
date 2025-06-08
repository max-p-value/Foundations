class Clock:
    def __init__(self, modules, dt=1.0):
        self.modules = modules
        self.dt = dt
        self.time = 0.0
        self.history = []

    def step(self):
        for module in self.modules:
            module.step(self.dt, self.time)
        self.time += self.dt

    def run(self, steps):
        for _ in range(steps):
            self.step()