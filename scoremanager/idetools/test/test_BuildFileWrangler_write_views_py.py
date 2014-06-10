# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_write_views_py_01():

    input_ = 'red~example~score u vw y q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'Will write ...' in contents
    assert 'Rewrote' in contents