from part2 import split_range, InputRange, MapRange, Map, split

def test_split_input_after_map():
    map_range = MapRange(0, 10)
    input_range = InputRange('test', 20, 30)

    assert list(split(input_range, map_range)) == [input_range]

def test_split_input_before_map():
    map_range = MapRange(50, 60)
    input_range = InputRange('test', 20, 30)

    assert list(split(input_range, map_range)) == [input_range]

def test_split_input_inside_map():
    map_range = MapRange(0, 100)
    input_range = InputRange('test', 20, 30)

    assert list(split(input_range, map_range)) == [input_range]

def test_split_input_overlap_map_start():
    map_range = MapRange(10, 60)
    input_range = InputRange('test', 0, 20)

    expected_output = [
        InputRange('test', 0, 10),
        InputRange('test', 11, 20),
    ]

    assert list(split(input_range, map_range)) == expected_output

def test_split_input_overlap_map_end():
    map_range = MapRange(0, 20)
    input_range = InputRange('test', 10, 30)

    expected_output = [
        InputRange('test', 10, 20),
        InputRange('test', 21, 30),
    ]

    assert list(split(input_range, map_range)) == expected_output


def test_split_input_overlap():
    map_range = MapRange(10, 20)
    input_range = InputRange('test', 0, 30)

    expected_output = [
        InputRange('test', 0, 10),
        InputRange('test', 11, 20),
        InputRange('test', 21, 30),
    ]

    assert list(split(input_range, map_range)) == expected_output


def test_split_range():
    map = Map(
        'test',
        'test_destination',
        [
            MapRange(0, 0, 10),
            MapRange(0, 10, 20),
            MapRange(0, 30, 10),
            MapRange(0, 50, 20),
            MapRange(0, 70, 10),
        ]
    )

    input_range = InputRange('test', 20, 40)

    expected_output = [
        InputRange('test', 20, 10),
        InputRange('test', 30, 10),
        InputRange('test', 40, 10),
        InputRange('test', 50, 10),
    ]

    output = list(split_range(input_range, map))

    assert output == expected_output