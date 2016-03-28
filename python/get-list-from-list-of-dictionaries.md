Get a list from a list of dictionaries 

You have a list of dictionaries:

jeep_matrix = [
    {'a': 1, 'b': 0.30},
    {'a': 2, 'b': 2.32},
    {'a': 3, 'b': 0.42},
    {'a': 8, 'b': 1.39},
]

list_of_b = [tree['b'] for tree in jeep_matrix]
