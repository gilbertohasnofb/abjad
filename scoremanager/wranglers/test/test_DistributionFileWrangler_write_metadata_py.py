# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.core.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_write_metadata_py_01():

    metadata_py_path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'distribution',
        '__metadata__.py',
        )

    with systemtools.FilesystemState(keep=[metadata_py_path]):
        input_ = 'red~example~score d mdw y q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents

    assert 'Will rewrite ...' in contents
    assert metadata_py_path in contents