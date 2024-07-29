footprint_set = set()

def initialize_set(initial_items=None):
    global footprint_set
    if initial_items is not None:
        footprint_set.update(initial_items)
def add_to_set(item):
    global footprint_set
    footprint_set.add(item)

def remove_from_set(item):
    global footprint_set
    footprint_set.discard(item)

def get_footprint_set():
    global footprint_set
    return footprint_set

def any_footprint_in_string(s):
    global footprint_set
    return any(item in s for item in footprint_set)
