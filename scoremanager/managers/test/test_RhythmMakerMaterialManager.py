# -*- encoding: utf-8 -*-
import os
import pytest
from abjad import *
import scoremanager
pytest.skip('unskip once it is possible to edit composite objects.')


def test_RhythmMakerMaterialManager_01():

    score_manager = scoremanager.core.ScoreManager()
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.abjad_material_packages_directory_path,
        'testrhythmmaker',
        )
    assert not os.path.exists(path)
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'output_material.py',
        ]
    talea = rhythmmakertools.Talea(
        counts=(-1, 2, -3, 4),
        denominator=16,
        )
    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=talea,
        extra_counts_per_division=(2, 3),
        split_divisions_by_counts=(6,),
        )
    input_ = 'lmm nmm rhythm testrhythmmaker default'
    input_ += ' testrhythmmaker omi talearhythmmaker'
    input_ += ' (-1, 2, -3, 4) 16 (2, 3) (6,) b default q'

    try:
        score_manager._run(pending_user_input=input_, is_test=True)
        manager = scoremanager.managers.RhythmMakerMaterialManager(
            path=path)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_material_module()
        assert output_material == maker
    finally:
        input_ = 'lmm testrhythmmaker rm remove q'
        score_manager._run(pending_user_input=input_, is_test=True)
        assert not os.path.exists(path)
