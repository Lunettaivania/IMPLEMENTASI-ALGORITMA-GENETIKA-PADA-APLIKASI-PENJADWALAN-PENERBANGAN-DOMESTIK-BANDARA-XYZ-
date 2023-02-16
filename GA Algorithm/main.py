import prettytable 

from schedule import Schedule
from genetic import GeneticOptimize


def vis(schedule):
    """visualization Class Schedule.

    Arguments:
        schedule: List, Class Schedule
    """
    col_labels = ['week/slot', 'senin', 'selasa', 'rabu', 'kamis', 'jumat','sabtu','minggu']
    table_vals = [[i + 4, '', '', '', '', '','','',] for i in range(7)]

    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)

    for s in schedule:
        weekDay = s.weekDay
        slot = s.slot
        text = 'flight: {} \n class: {} \n room: {} \n des: {}'.format(s.flightId, s.classId, s.roomId, s.destinationId)
        table_vals[weekDay - 1][slot] = text

    for row in table_vals:
        table.add_row(row)

    print(table)


if __name__ == '__main__':
    schedules = []

    # add schedule
    schedules.append(Schedule(201, "vip", "bali"))
    schedules.append(Schedule(201, "vip", "bali"))
    schedules.append(Schedule(202, "vip", "jakarta"))
    schedules.append(Schedule(202, "vip", "jakarta"))
    schedules.append(Schedule(203, "vip", "pekanbaru"))
    schedules.append(Schedule(203, "vip", "pekanbaru"))
    schedules.append(Schedule(206, "vip", "balikpapan"))
    schedules.append(Schedule(206, "vip", "balikpapan"))

    schedules.append(Schedule(202, "bisnis", "jakarta"))
    schedules.append(Schedule(202, "bisnis", "jakarta"))
    schedules.append(Schedule(204, "bisnis", "pontianak"))
    schedules.append(Schedule(204, "bisnis", "pontianak"))
    schedules.append(Schedule(206, "bisnis", "balikpapan"))
    schedules.append(Schedule(206, "bisnis", "balikpapan"))

    schedules.append(Schedule(203, "eksekutif", "pekanbaru"))
    schedules.append(Schedule(203, "eksekutif", "pekanbaru"))
    schedules.append(Schedule(204, "eksekutif", "pontianak"))
    schedules.append(Schedule(204, "eksekutif", "pontianak"))
    schedules.append(Schedule(205, "eksekutif", "jogja"))
    schedules.append(Schedule(205, "eksekutif", "jogja"))
    schedules.append(Schedule(206, "eksekutif", "balikpapan"))
    schedules.append(Schedule(206, "eksekutif", "balikpapan"))

    # optimization
    ga = GeneticOptimize(popsize=50, elite=10, maxiter=500)
    res = ga.evolution(schedules, 3)

    # visualization
    vis_res = []
    for r in res:
        print("flight", r.flightId)
        print("class", r.classId)
        print("destination", r.destinationId)

        print("room", r.roomId)
        print("weekday", r.weekDay)
        print("slot", r.slot)

        print("===============\n")
        # if r.classId == "eksekutif":
        #     vis_res.append(r)
        vis_res.append(r)
    vis(vis_res)
