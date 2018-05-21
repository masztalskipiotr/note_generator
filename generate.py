from Note import Note
from config import tempo, rest_prob, bar_count, notes
from random import randint, random
from rhythmic_values import init_rythmic_values
from init_header import init_header
from count_interval import count_interval

header = init_header()
rhythmic_values = init_rythmic_values()

def generate(filename, random_mode, interval, going_down):
    if random_mode:
        random(filename)
    else:
        interval_mode(filename, interval, going_down)

def random(filename):
    with open(filename, 'w') as file:
        file.write(header)
        file.write(" { \\time %d/4 " % tempo)
        full_time = bar_count / (4 / tempo)
        while full_time > 0:
            note = Note()
            rest_rand = random()
            if rest_rand <= rest_prob:
                note.pitch = 'r'
            else:
                note.degree = randint(0, len(notes) - 1)
                note.pitch = notes[note.degree][0]

            ind = randint(0, len(rhythmic_values) - 1)
            note.time_stamp, time_str = rhythmic_values[ind]

            while 1 / note.time_stamp > full_time:
                ind += 1
                note.time_stamp, time_str = rhythmic_values[ind]

            full_time -= 1 / note.time_stamp
            file.write(note.pitch + time_str + " ")


def interval_mode(filename, interval, going_down):
    with open(filename, 'w') as file:
        file.write(header)
        file.write(" { \\time %d/4 " % tempo)
        full_time = bar_count / (4 / tempo)
        note = Note()
        file.write(note.pitch + note.octave + " ")
        full_time -= (1 / note.time_stamp)
        while full_time > 0:
            if going_down:
                note = count_interval(note, -interval.interval, -interval.semitones)
            else:
                note = count_interval(note, interval.interval, interval.semitones)
            ind = randint(0, len(rhythmic_values) - 1)
            note.time_stamp, time_str = rhythmic_values[ind]

            while 1 / note.time_stamp > full_time:
                ind += 1
                note.time_stamp, time_str = rhythmic_values[ind]

            full_time -= 1 / note.time_stamp
            file.write(note.pitch + note.octave + time_str + " ")

        file.write(' \\bar "||" }')