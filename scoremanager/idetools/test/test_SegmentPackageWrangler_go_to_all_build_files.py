# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageWrangler_go_to_all_build_files_01():
    r'''From score segments to all build files.
    '''

    input_ = 'red~example~score g U q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments',
        'Abjad IDE - build files',
        ]
    assert ide._transcript.titles == titles


def test_SegmentPackageWrangler_go_to_all_build_files_02():
    r'''From all segments to all build files.
    '''

    input_ = 'G U q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - segments',
        'Abjad IDE - build files',
        ]
    assert ide._transcript.titles == titles