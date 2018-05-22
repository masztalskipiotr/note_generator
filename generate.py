from possibilities import pick_interval
from Note import Note, count_distance
from config import tempo, bar_count, highest_note, lowest_note
import random
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
        file.write(note.pitch + note.octave + str(note.time_stamp) + " ")
        full_time -= (1 / note.time_stamp)

        while full_time > 0:
            possibilities = init_possibilities(note, up, low, intervals)
            interval, semitones = pick_interval(possibilities)
            note = count_interval(note, interval, semitones)
            ind = random.randint(0, len(rhythmic_values) - 1)
            note.time_stamp, time_str = rhythmic_values[ind]

            while 1 / note.time_stamp > full_time:
                ind += 1
                note.time_stamp, time_str = rhythmic_values[ind]

            full_time -= 1 / note.time_stamp
            file.write(note.pitch + note.octave + time_str + " ")

        file.write(' \\bar "||" }')