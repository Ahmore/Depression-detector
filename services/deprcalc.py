def depression(value):
    print(value)
    if value < 10.0:
        return 4
    if value < 16.0:
        return 3
    if value < 22.0:
        return 2
    return 1


def normalize(value, total):
    res = value / total
    if res > 0.5:
        return 3.0
    return res * 6.0


def depression_calculator(emotions):
    if emotions['neutral'] > 0.4:
        emotions['neutral'] /= 10.0

    total = sum([v for k, v in emotions.items()])

    s = 3 * normalize(emotions["sadness"], total)
    fn = 4 * normalize(emotions["fear"] + emotions['neutral'], total)
    f_su = normalize(emotions["fear"] + emotions["surprise"], total)
    c = 2 * normalize(emotions["contempt"], total)
    acs = 3 * normalize(
        emotions["anger"] + emotions["contempt"] + emotions["sadness"], total)
    afc = 2 * normalize(
        emotions["anger"] + emotions["fear"] + emotions["contempt"]
        , total)
    fs = normalize(emotions["fear"] + emotions["sadness"], total)
    sc = normalize(emotions["sadness"] + emotions["contempt"], total)
    sfc = normalize(

        emotions["sadness"] + emotions["fear"] + emotions["contempt"], total)

    coeffs = [s, fn, f_su, c, acs, afc, fs, sc, sfc]

    return depression(sum(coeffs))
