# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_go_to_all_materials_01():
    r'''From score distribution files to all materials.
    '''

    input_ = 'red~example~score d M q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - distribution files',
        'Abjad IDE - materials',
        ]
    assert ide._transcript.titles == titles


def test_DistributionFileWrangler_go_to_all_materials_02():
    r'''From all distribution files to all materials.
    '''

    input_ = 'D M q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - distribution files',
        'Abjad IDE - materials',
        ]
    assert ide._transcript.titles == titles