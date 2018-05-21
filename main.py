from init_intervals import init_intervals
from config import random_mode
from generate import generate

intervals = init_intervals()

filename = 'p1.ly'
going_down = True
generate(filename, random_mode, intervals[1], going_down)   # just minor third going down for test

