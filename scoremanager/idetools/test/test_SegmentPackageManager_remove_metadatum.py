# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)
metadata_py_path = os.path.join(
    score_manager._configuration.example_score_packages_directory,
    'red_example_score',
    'segments',
    'segment_01',
    '__metadata__.py',
    )


def test_SegmentPackageManager_remove_metadatum_01():

    with systemtools.FilesystemState(keep=[metadata_py_path]):
        # make sure no flavor metadatum found
        input_ = 'red~example~score g A mdg flavor q'
        score_manager._run(input_=input_)
        assert 'None' in score_manager._transcript.contents

        # add flavor metadatum
        input_ = 'red~example~score g A mda flavor cherry q'
        score_manager._run(input_=input_)

        # maker sure flavor metadatum now equal to 'cherry'
        input_ = 'red~example~score g A mdg flavor q'
        score_manager._run(input_=input_)
        assert "'cherry'" in score_manager._transcript.contents

        # remove flavor metadatum
        input_ = 'red~example~score g A mdrm flavor q'
        score_manager._run(input_=input_)

        # make sure no flavor metadatum found
        input_ = 'red~example~score g A mdg flavor q'
        score_manager._run(input_=input_)
        assert 'None' in score_manager._transcript.contents