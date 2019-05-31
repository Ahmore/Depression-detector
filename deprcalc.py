def depression(value):
    if value <= 10:
        return 0
    if value <= 16:
        return 1
    if value <= 22:
        return 2
    return 3


def normalize(value, total):
    res = value / total
    return res * 3.0


def depression_calculator(emotions):
    if emotions['neutral'] > 0.4:
        emotions['neutral'] /= 10.0

    total = sum([v for k, v in emotions.items()])

    s = 3 * normalize(emotions["sadness"], total)
    f = 4 * normalize(emotions["fear"] + emotions['neutral'], total)
    f_su = normalize(emotions["fear"] + emotions["surprise"], total)
    c = 2 * normalize(emotions["contempt"], total)
    ac = 3 * normalize(emotions["anger"] + emotions["contempt"], total)
    afc = 2 * normalize(
        emotions["anger"] + emotions["fear"] + emotions["contempt"], total)
    fs = normalize(emotions["fear"] + emotions["sadness"], total)
    sc = normalize(emotions["sadness"] + emotions["contempt"], total)
    sfc = normalize(
        emotions["sadness"] + emotions["fear"] + emotions["contempt"], total)

    coeffs = [s, f, f_su, c, ac, afc, fs, sc, sfc]
    return depression(sum(coeffs))


# emotions = {
#     "anger": 0,
#     "contempt": 0,
#     "disgust": 0,
#     "fear": 0,
#     "happiness": 0,
#     "neutral": 0.334,
#     "sadness": 0.665,
#     "surprise": 0
# }
#
# print(depression_calculator(emotions))
