# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_OctaveTranspositionMappingInventoryEditor_run_01():
    r'''Empty inventories.
    '''

    editor = scoremanager.editors.OctaveTranspositionMappingInventoryEditor()
    editor._run(pending_user_input='done')
    assert editor.target == pitchtools.OctaveTranspositionMappingInventory()

    editor = scoremanager.editors.OctaveTranspositionMappingInventoryEditor()
    editor._run(pending_user_input='q')
    assert editor.target == pitchtools.OctaveTranspositionMappingInventory()

    editor = scoremanager.editors.OctaveTranspositionMappingInventoryEditor()
    editor._run(pending_user_input='b')
    assert editor.target == pitchtools.OctaveTranspositionMappingInventory()

    editor = scoremanager.editors.OctaveTranspositionMappingInventoryEditor()
    editor._run(pending_user_input='home')
    assert editor.target == pitchtools.OctaveTranspositionMappingInventory()


# TODO: remove test
#def test_OctaveTranspositionMappingInventoryEditor_run_02():
#    r'''Empty named inventory.
#    '''
#
#    editor = scoremanager.editors.OctaveTranspositionMappingInventoryEditor()
#    editor._run(pending_user_input='id foo done')
#    assert editor.target == \
#        pitchtools.OctaveTranspositionMappingInventory(custom_identifier='foo')
