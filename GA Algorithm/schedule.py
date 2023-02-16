import numpy as np


class Schedule:
    """Class Schedule.
    """
    def __init__(self, flightId, classId, destinationId):
        """Init
        Arguments:
            flightId: int, unique flight id.
            classId: int, unique class id.
            destinationId: int, unique destination id.
        """
        self.flightId = flightId
        self.classId = classId
        self.destinationId = destinationId

        self.roomId = 0
        self.weekDay = 0
        self.slot = 0

    def random_init(self, roomRange):
        """random init.

        Arguments:
            roomSize: int, number of classrooms.
        """
        self.roomId = np.random.randint(1, roomRange + 1, 1)[0]
        self.weekDay = np.random.randint(1, 8, 1)[0]
        self.slot = np.random.randint(1, 8, 1)[0]


def schedule_cost(population, elite):
    """calculate conflict of class schedules.

    Arguments:
        population: List, population of class schedules.
        elite: int, number of best result.

    Returns:
        index of best result.
        best conflict score.
    """
    conflicts = []
    n = len(population[0])

    for p in population:
        conflict = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # check flight in same time and same room 
                if p[i].roomId == p[j].roomId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check flight for one class in same time
                if p[i].classId == p[j].classId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check flight for one destination in same time
                # if p[i].destinationId == p[j].destinationId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                #     conflict += 1
                # check same flight for one class in same day
                if p[i].classId == p[j].classId and p[i].flightId == p[j].flightId and p[i].weekDay == p[j].weekDay:
                    conflict += 1

        conflicts.append(conflict)

    index = np.array(conflicts).argsort()

    return index[: elite], conflicts[index[0]]
