import abjad


def test_LilyPondParser__leaves__Skip_01():

    target = abjad.Skip((3, 8))
    parser = abjad.parser.LilyPondParser()
    result = parser("{ %s }" % format(target))
    assert format(target) == format(result[0]) and target is not result[0]
