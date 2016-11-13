from itertools import chain, zip_longest

def roundrobin(*iterables):
    sentinel = object()
    return (x for x in chain(*zip_longest(fillvalue=sentinel, *iterables)) if x is not sentinel)

print(list(roundrobin('ABC', 'D', 'EF','GHIJ')))


# copy from
# http://code.activestate.com/recipes/578768-and-yet-another-round-robin-generator/