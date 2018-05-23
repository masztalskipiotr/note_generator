from possibilities import pick_interval
from Note import Note, count_distance
from config import tempo, bar_count, highest_note, lowest_note, rest_probability
from random import random, randint
from possibilities import init_possibilities
from rhythmic_values import init_rythmic_values
from init_header import init_header
from count_interval import count_interval

header = init_header()
rhythmic_values = init_rythmic_values()


def generate(filename, intervals):

    up = count_distance(highest_note)
    low = count_distance(lowest_note)

    with open(filename, 'w') as file:
        file.write(header)
        file.write(" { \\time %d/4 " % tempo)
        full_time = bar_count / (4 / tempo)
        note = Note()
        while full_time > 0:
            ind = randint(0, len(rhythmic_values) - 1)
            note.time_stamp, time_str = rhythmic_values[ind]
            while 1 / note.time_stamp > full_time:
                ind += 1
                note.time_stamp, time_str = rhythmic_values[ind]
            if random() <= rest_probability:
                file.write("r" + time_str + " ")
                full_time -= 1 / note.time_stamp
                continue
            file.write(note.pitch + note.octave + time_str + " ")
            full_time -= 1 / note.time_stamp
            possibilities = init_possibilities(note, up, low, intervals)
            interval, semitones = pick_interval(possibilities)
            note = count_interval(note, interval, semitones)
        file.write(' \\bar "||" } }')