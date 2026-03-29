names=['Ann', 'Bob', 'Dan', 'Eve', 'Tracy', 'Kevin']
scores= [1.3, 0.8, 0.2 ,2.5, 3.7, 0.8]

ns_dict = dict(zip(names, scores))
print(len(ns_dict))
print(ns_dict)

for k, v in ns_dict.items():
    print(k, v)

for i, (k,v) in enumerate(ns_dict.items()):
    print(i, k, v)

def pair_by_value(dict_items, v):
    result = [(k, val) for k, val in dict_items if v == val]
    return result

def indices_of(dict_items, val):
    result = [i for i, (k,v) in enumerate(dict_items) if v == val]
    return result


def first_index_of(dict_items, val):
    result = min(indices_of(dict_items, val))
    return result


def last_index_of(dict_items, val):
    result = max(indices_of(dict_items, val))
    return result


def get_value(dict, k):
    result = dict[k]
    return result


ks = ns_dict.keys()
vs = ns_dict.values()

rv = pair_by_value(ns_dict.items(), 0.8)
print(rv)
val = get_value(ns_dict, "Tracy")
print(val)

ii = indices_of(ns_dict.items(), 0.8)
print(ii)

imin = first_index_of(ns_dict.items(), 0.8)
print(imin)

imax = last_index_of(ns_dict.items(), 0.8)
print(imax)
