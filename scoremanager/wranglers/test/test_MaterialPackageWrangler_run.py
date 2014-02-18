# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_MaterialPackageWrangler_run_01():
    r'''Quit, back, home, score & junk all work.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='mlm q')
    assert score_manager.session.io_transcript.signature == (4,)

    score_manager._run(pending_user_input='mlm b q')
    assert score_manager.session.io_transcript.signature == (6, (0, 4))

    score_manager._run(pending_user_input='mlm h q')
    assert score_manager.session.io_transcript.signature == (6, (0, 4))

    score_manager._run(pending_user_input='mlm s q')
    assert score_manager.session.io_transcript.signature == (6, (2, 4))

    score_manager._run(pending_user_input='mlm asdf q')
    assert score_manager.session.io_transcript.signature == (6, (2, 4))


def test_MaterialPackageWrangler_run_02():
    r'''Breadcrumbs work.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='mlm q')
    title_line = 'Score manager - material library'
    assert score_manager.session.io_transcript[-2][1][0] == title_line


def test_MaterialPackageWrangler_run_03():
    r'''Menu displays at least one test material.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='mlm q')
    menu_lines = score_manager.session.io_transcript[-2][1]
    assert any(x.endswith('red sargasso measures') for x in menu_lines)
