class PQueue:
    pass

Node = namedTuple('id', 'value') # we need to store distance in nodes

def djikstra():
    # how to represent graphs with distances on the
    # edges
    q = PQueue()
