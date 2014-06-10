# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_go_to_segments_01():
    r'''Goes from score materials to score segments.
    '''

    input_ = 'red~example~score m g q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - segments',
        ]
    assert score_manager._transcript.titles == titles


def test_MaterialPackageWrangler_go_to_segments_02():
    r'''Goes from material library to segment library.
    '''

    input_ = 'm g q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - materials',
        'Abjad IDE - segments',
        ]
    assert score_manager._transcript.titles == titles