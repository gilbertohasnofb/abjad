# -*- encoding: utf-8 -*-
import inspect
import pytest
from abjad.tools import *


classes = documentationtools.list_all_abjad_classes()
@pytest.mark.parametrize('class_', classes)
def test_default_positional_values_01(class_):
    r'''All storage-formattable concrete classes initialize from empty input.
    '''

    if '_storage_format' in dir(class_) and not inspect.isabstract(class_):
        instance = class_()
