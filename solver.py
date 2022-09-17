from numpy import array, matrix


class Solver:
    def __init__(self, driving_equations: [], step_time: float, start_time: float, end_time: float):
        self.driving_equations = driving_equations
        self.dt = step_time
        self.start = start_time
        self.end = end_time

    def simulate(self):
        time = self.create_time_span(self.start, self.end, self.dt)



    @staticmethod
    def create_time_span(t_start, t_end, step_size):
        time_span = []
        time = t_start
        while time <= t_end:
            time_span.append(time)
            time += step_size
        time_span.append(time)
        return time_span
