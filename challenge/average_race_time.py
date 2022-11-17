# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    race_time_Rhines = []

    def get_time(line):
        return re.findall(r'\d{2}:\S+', line)[0]

    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            race_time_Rhines.append(get_time(line))
    return race_time_Rhines


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()  # saber el numero de tiempos registrados
    for time in racetimes:
        try:
            m, s, M = re.findall(r'[:.]', time)
            total += datetime.timedelta(minutes=int(m),
                                        seconds=int(s),
                                        milliseconds=int(M))
        except ValueError:
            m, s = re.split(r'[:]', time)
            total += datetime.timedelta(minutes=int(m),
                                        seconds=int(s))

    return total
