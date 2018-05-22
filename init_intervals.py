from Interval import Interval
import config


def init_intervals():

    intervals = []

    intervals.append(Interval('unison',0,0, config.unison))
    intervals.append(Interval('dim_second',1,0, config.dim_second))
    intervals.append(Interval('aug_unison',0,1, config.aug_unison))
    intervals.append(Interval('min_second',1,1, config.min_second))

    intervals.append(Interval('maj_second',1,2, config.maj_second))
    intervals.append(Interval('dim_third',2,2, config.dim_third))
    intervals.append(Interval('aug_second',1,3, config.aug_second))
    intervals.append(Interval('min_third',2,3, config.min_third))

    intervals.append(Interval('maj_third',2,4, config.maj_third))
    intervals.append(Interval('dim_fourth',3,4, config.dim_fourth))
    intervals.append(Interval('aug_third',2,5, config.aug_third))
    intervals.append(Interval('fourth',3,5, config.fourth))

    intervals.append(Interval('aug_fourth',3,6, config.aug_fourth))
    intervals.append(Interval('dim_fifth',4,6, config.dim_fifth))

    intervals.append(Interval('fifth',4,7, config.fifth))
    intervals.append(Interval('dim_sixth',5,7, config.dim_sixth))
    intervals.append(Interval('aug_fifth',4,8, config.aug_fifth))
    intervals.append(Interval('min_sixth',5,8, config.min_sixth))

    intervals.append(Interval('maj_sixth',5,9, config.maj_sixth))
    intervals.append(Interval('dim_seventh',6,9, config.dim_seventh))
    intervals.append(Interval('aug_sixth',5,10, config.aug_sixth))
    intervals.append(Interval('min_seventh',6,10, config.min_seventh))

    intervals.append(Interval('maj_seventh',6,11, config.maj_seventh))
    intervals.append(Interval('dim_octave',7,11, config.dim_octave))
    intervals.append(Interval('aug_seventh',6,12,config.aug_seventh))
    intervals.append(Interval('octave',7,12, config.octave))

    #intervals = sorted(intervals, key=lambda x: x.probability, reverse=True)
    #distribute_probability(intervals)

    return intervals
