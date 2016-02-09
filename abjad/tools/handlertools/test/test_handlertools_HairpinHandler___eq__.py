# -*- coding: utf-8 -*-
from abjad import *


def test_handlertools_HairpinHandler___eq___01():

    handler_1 = handlertools.HairpinHandler(
        hairpin_tokens=['p < f'],
        minimum_duration=Duration(1, 8),
        )

    handler_2 = handlertools.HairpinHandler(
        hairpin_tokens=['p < f'],
        minimum_duration=Duration(1, 8),
        )

    handler_3 = handlertools.HairpinHandler(
        hairpin_tokens=['pp < p'],
        minimum_duration=Duration(1, 8),
        )

    assert handler_1 == handler_1
    assert handler_1 == handler_2
    assert not handler_1 == handler_3
    assert handler_2 == handler_1
    assert handler_2 == handler_2
    assert not handler_2 == handler_3
    assert not handler_3 == handler_1
    assert not handler_3 == handler_2
    assert handler_3 == handler_3