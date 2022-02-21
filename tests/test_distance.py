from mlproject.distance import haversine

def test_distance():
    # var = haversine(23,2,24,22)
    # print(type(haversine(23,2,24,22)))
    assert type(haversine(23,2,24,22)) == type(2.4)
    # assert type(var) == "<class 'float'>"
