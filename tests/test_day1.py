import pytest
import day_01_2

DATA = [
    ("five2six85npdqxgrshdjs4", 54),
    ("jbbnine2ttrktc2hxpxfdxgf", 92),
    ("fngvqsgmjfmfslrmone2vtpsstpkhr2jmmxk", 12),
    ("f683glvfsdvnsghvrzcdmxnx81", 61),
    ("lqblzgj322kqfsjrbxgcgsct", 32),
    ("threeldfnrbstbxqdpxpkbztbp84eight", 38),
    ("sevensevenmthprqg9six", 76),
    ("qldknljthdjthreeklttd6six", 36),
    ("7eightcdqxcftbgbfbnvqfive", 75),
    ("gxjzhvkbcjhscdxhjdqxnhsevenxrdrjbcl5fvlvlxjjvb", 75),
    ("9sixqnine9jk9six", 96),
    ("zjtdbzr6njdgflrmpshxn", 66),
    ("rktpknvmjknb7threefourhdxhcdtgtkvone", 71),
    ("276lzxhone3two2", 22),
    ("82fivelppqzjq", 85),
    ("lchslxtwohslsztgps5pdssctclhdkqtwo", 22),
    ("2five8three9dnine8", 28),
    ("68jpnqldjgfnpcmvbxnszhz2252", 62),
    ("q32", 32),
    ("2sixtwo87", 27),
    ("rgxrddnnbv7rkt", 77),
    ("8ffmvpcsvfoureightqpnzzjksgchnine9jlgjqb", 89),
    ("two9tfvjqsgqsixnine", 29),
    ("bzn4two", 42),
    ("sqlfeighteight6hjddxzcone2", 82),
    ("3fivekmfnqlctddfivelcthnine", 39),
    ("twodn8", 28),
    ("one5six913lbrcc", 13),
    ("foureightmppchbgz8lqbzqbjztwo7cksqxns", 47),
    ("zvhzgfpkhkone93nine", 19),
    ("mboneighteightonefive1ninenineninetwonine", 19),
    ("1one", 11),
    ("1two", 12),
    ("1three", 13),
    ("1four", 14),
    ("1five", 15),
    ("1six", 16),
    ("1seven", 17),
    ("1eight", 18),
    ("1nine", 19),
    ("one1", 11),
    ("two1", 21),
    ("three1", 31),
    ("four1", 41),
    ("five1", 51),
    ("six1", 61),
    ("seven1", 71),
    ("eight1", 81),
    ("nine1", 91),
    ("oneight", 18),
    ("nineight", 98),
]


@pytest.mark.parametrize("line,expected", DATA)
def test_read_digits_from_line(line: str, expected: int):
    assert day_01_2.read_digits_from_line(line) == expected
    assert day_01_2.read_digits_from_line("abc" + line) == expected
    assert day_01_2.read_digits_from_line("abc" + line + "abc") == expected
    assert day_01_2.read_digits_from_line(line + "abc") == expected
