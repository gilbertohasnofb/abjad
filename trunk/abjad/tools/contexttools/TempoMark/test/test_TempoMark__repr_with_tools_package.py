from abjad import *


def test_TempoMark__repr_with_tools_package_01():

    assert contexttools.TempoMark('Allegro', (1, 4), 84)._tools_package_qualified_repr == \
        "contexttools.TempoMark('Allegro', durationtools.Duration(1, 4), 84)"
