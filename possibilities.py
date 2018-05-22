from random import random
from Possibility import Possibility
import config
from init_intervals import init_intervals

pitches_prob = [config.c, config.cis, config.d, config.dis, config.e, config.f, config.fis, config.g, config.gis,
                config.a, config.ais, config.b]

intervals = init_intervals()

def init_possibilities(note, up, low, intervals):

    possibilities = []

    for interval in intervals:
        new_note_distance = note.distance + interval.semitones
        if up >= new_note_distance >= low:
            possibilities.append(Possibility(interval.interval, interval.semitones, interval.probability + pitches_prob[new_note_distance % 12]))
        new_note_distance = note.distance - interval.semitones
        if up >= new_note_distance >= low:
            possibilities.append(Possibility(-interval.interval, -interval.semitones, interval.probability + pitches_prob[new_note_distance % 12]))

    possibilities.sort(key=lambda x: x.probability, reverse=True)
    distribute_probability(possibilities)
    return possibilities


def distribute_probability(possibilities):
    sum, prev = 0, 0
    for el in possibilities:
        sum += el.probability
    for el in possibilities:
        el.probability = (el.probability / sum) + prev
        prev = el.probability


def pick_interval(possibilities):
    ind = random()
    for el in possibilities:
        if ind <= el.probability:
            return el.interval, el.semitones
