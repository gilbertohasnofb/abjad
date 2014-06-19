# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)
views_file = os.path.join(
    score_manager._configuration.wrangler_views_directory,
    '__SegmentPackageWrangler_views__.py',
    )


def test_SegmentPackageWrangler_remove_views_01():
    r'''Makes two views. Removes two views at one time.
    '''

    with systemtools.FilesystemState(keep=[views_file]):
        input_ = 'G vnew _test_100 rm all'
        input_ += ' add A~(Red~Example~Score) done' 
        input_ += ' g vnew _test_101 rm all'
        input_ += ' add segment~02~(Red~Example~Score) done'
        input_ += ' q' 
        score_manager._run(input_=input_)

        input_ = 'G va q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents
        assert '_test_100' in contents
        assert '_test_101' in contents

        input_ = 'G vrm _test_100-_test_101 q'
        score_manager._run(input_=input_)

        input_ = 'G va q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents
        assert '_test_100' not in contents
        assert '_test_101' not in contents


def test_SegmentPackageWrangler_remove_views_02():
    r'''Makes sure selector backtracking works.
    '''

    with systemtools.FilesystemState(keep=[views_file]):
        input_ = 'G vrm b q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents

    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - segments',
        'Abjad IDE - segments',
        'Abjad IDE - segments',
        ]
    assert score_manager._transcript.titles == titles
    assert 'Select view(s) to remove:' in contents