import csv
import pprint

pp = pprint.PrettyPrinter(indent=4, compact=True)
pprint = pp.pprint


def main():
    pprint(freeUniqEnglish('google')[0:10])
    pprint(freeUniqEnglish('apple')[0:10])


def freeUniqEnglish(setName):
    dSet = readSet(setName + ".csv")
    return removeDupes(removeNonEnglish(removePaid(dSet, setName), setName),
                       setName)


def removeNonEnglish(data, store):
    nloc = 1 if store == 'apple' else (0 if store == 'google' else None)
    return [app for app in data if isEnglish(app[nloc])]


def removePaid(data, store):
    ploc = 4 if store == 'apple' else (7 if store == 'google' else None)
    return [app for app in data if float(app[ploc].replace("$", '')) == 0]


def isEnglish(text):
    return sum(ord(c) > 127 for c in text) <= 3


def removeDupes(data, store):
    if store == 'apple':
        return data

    data = sorted(data, key=lambda x: int(x[3]), reverse=True)
    uniq = []

    # very slow, not sure how to fix
    for app in data:
        if not app[0] in [ae[0] for ae in uniq]:
            uniq.append(app)
    return uniq


def readSet(fname):
    with open(fname, 'r') as f:
        f.readline()
        data = [
            l for l in csv.reader(f.readlines(),
                                  quotechar='"',
                                  delimiter=',',
                                  quoting=csv.QUOTE_ALL,
                                  skipinitialspace=True)
        ]
        if fname == 'google.csv':
            del data[10472]
        return data


if __name__ == "__main__":
    main()