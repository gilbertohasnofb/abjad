import abjad
from abjad import rhythmtree


def test_RhythmTreeContainer_children_01():

    leaf_a = rhythmtree.RhythmTreeLeaf(preprolated_duration=3)
    leaf_b = rhythmtree.RhythmTreeLeaf(preprolated_duration=3)
    leaf_c = rhythmtree.RhythmTreeLeaf(preprolated_duration=2)
    subcontainer = rhythmtree.RhythmTreeContainer(
        preprolated_duration=2, children=[leaf_b, leaf_c])
    leaf_d = rhythmtree.RhythmTreeLeaf(preprolated_duration=1)

    container = rhythmtree.RhythmTreeContainer(
        preprolated_duration=1, children=[leaf_a, subcontainer, leaf_d])

    assert container.children == (leaf_a, subcontainer, leaf_d)
