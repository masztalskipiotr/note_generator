from config import tempo

def init_rythmic_values():

    if tempo == 2:
        rythmic_values = [[2, '2'], [8/3, '4.'], [4, '4'],
                          [16/3, '8.'], [8, '8'], [16, '16']]
    elif tempo == 3:
        rythmic_values = [[4/3, '2.'], [2, '2'], [8/3, '4.'], [4, '4'],
                          [16/3, '8.'], [8, '8'], [16, '16']]
    elif tempo == 4:
        rythmic_values = [[1, '1'], [4/3, '2.'], [2, '2'], [8/3, '4.'], [4, '4'],
                          [16/3, '8.'], [8, '8'], [16, '16']]
    elif tempo == 5:
        rythmic_values = [[1, '1'], [4 / 3, '2.'], [2, '2'], [8 / 3, '4.'], [4, '4'],
                          [16 / 3, '8.'], [8, '8'], [16, '16']]

    return rythmic_values