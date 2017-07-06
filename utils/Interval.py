class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def createInterval(arr):
    intervals = []
    for (s, e) in arr:
        intervals += Interval(s, e),
    return intervals


def printInterval(arr):
    if not arr:
        print("[]")
        return
    for interval in arr:
        print("[{},{}] ".format(interval.start, interval.end))
    return
