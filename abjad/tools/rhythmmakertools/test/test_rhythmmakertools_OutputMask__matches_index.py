# -*- encoding: utf -*-
from abjad import *


def test_rhythmmakertools_OutputMask__matches_index_01():

    mask = rhythmmakertools.OutputMask(
        indices=[0, 1],
        period=None,
        )

    length = 9
    assert mask._matches_index(0, length)
    assert mask._matches_index(1, length)
    assert not mask._matches_index(2, length)
    assert not mask._matches_index(3, length)
    assert not mask._matches_index(4, length)
    assert not mask._matches_index(5, length)
    assert not mask._matches_index(6, length)
    assert not mask._matches_index(7, length)


def test_rhythmmakertools_OutputMask__matches_index_02():

    mask = rhythmmakertools.OutputMask(
        indices=[0, 1],
        period=4,
        )

    length = 9
    assert mask._matches_index(0, length)
    assert mask._matches_index(1, length)
    assert not mask._matches_index(2, length)
    assert not mask._matches_index(3, length)
    assert mask._matches_index(4, length)
    assert mask._matches_index(5, length)
    assert not mask._matches_index(6, length)
    assert not mask._matches_index(7, length)


def test_rhythmmakertools_OutputMask__matches_index_03():

    mask = rhythmmakertools.OutputMask(
        indices=[0, 1, 2, 3, 4, 5, 6, 7],
        period=None,
        )

    length = 9
    assert mask._matches_index(0, length)
    assert mask._matches_index(1, length)
    assert mask._matches_index(2, length)
    assert mask._matches_index(3, length)
    assert mask._matches_index(4, length)
    assert mask._matches_index(5, length)
    assert mask._matches_index(6, length)
    assert mask._matches_index(7, length)


def test_rhythmmakertools_OutputMask__matches_index_04():

    mask = rhythmmakertools.OutputMask(
        indices=[0, 1, 2, 3, 4, 5, 6, 7],
        period=None,
        )

    length = 2
    assert mask._matches_index(0, length)
    assert mask._matches_index(1, length)
    assert not mask._matches_index(2, length)
    assert not mask._matches_index(3, length)
    assert not mask._matches_index(4, length)
    assert not mask._matches_index(5, length)
    assert not mask._matches_index(6, length)
    assert not mask._matches_index(7, length)


def test_rhythmmakertools_OutputMask__matches_index_05():

    mask = rhythmmakertools.OutputMask(
        indices=[-2, -1],
        period=None,
        )

    length = 4
    assert not mask._matches_index(0, length)
    assert not mask._matches_index(1, length)
    assert mask._matches_index(2, length)
    assert mask._matches_index(3, length)
    assert not mask._matches_index(4, length)
    assert not mask._matches_index(5, length)
    assert not mask._matches_index(6, length)
    assert not mask._matches_index(7, length)


def test_rhythmmakertools_OutputMask__matches_index_06():

    mask = rhythmmakertools.OutputMask(
        indices=[-2, -1],
        period=4,
        )

    length = 4
    assert not mask._matches_index(0, length)
    assert not mask._matches_index(1, length)
    assert mask._matches_index(2, length)
    assert mask._matches_index(3, length)
    assert not mask._matches_index(4, length)
    assert not mask._matches_index(5, length)
    assert mask._matches_index(6, length)
    assert mask._matches_index(7, length)