from Interval import Interval


def init_intervals():

    intervals = []

    intervals.append(Interval('unison',0,0))
    intervals.append(Interval('dim_second',1,0))
    intervals.append(Interval('aug_unison',0,1))
    intervals.append(Interval('min_second',1,1))

    intervals.append(Interval('maj_second',1,2))
    intervals.append(Interval('dim_third',2,2))
    intervals.append(Interval('aug_second',1,3))
    intervals.append(Interval('min_third',2,3))

    intervals.append(Interval('maj_third',2,4))
    intervals.append(Interval('dim_fourth',3,4))
    intervals.append(Interval('aug_third',2,5))
    intervals.append(Interval('fourth',3,5))

    intervals.append(Interval('aug_fourth',3,6))
    intervals.append(Interval('dim_fifth',4,6))

    intervals.append(Interval('fifth',4,7))
    intervals.append(Interval('dim_sixth',5,7))
    intervals.append(Interval('aug_fifth',4,8))
    intervals.append(Interval('min_sixth',5,8))

    intervals.append(Interval('maj_sixth',5,9))
    intervals.append(Interval('dim_seventh',6,9))
    intervals.append(Interval('aug_sixth',5,10))
    intervals.append(Interval('min_seventh',6,10))

    intervals.append(Interval('maj_seventh',6,11))
    intervals.append(Interval('dim_octave',7,11))
    intervals.append(Interval('aug_seventh',6,12))
    intervals.append(Interval('octave',7,12))

    return intervals
