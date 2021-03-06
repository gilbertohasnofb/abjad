import pytest

import abjad

pytest_plugins = ["helpers_namespace"]


@pytest.fixture(autouse=True)
def add_libraries(doctest_namespace):
    doctest_namespace["abjad"] = abjad


@pytest.helpers.register
def list_all_abjad_classes(modules="abjad", ignored_classes=None):
    return abjad.list_all_classes(modules=modules, ignored_classes=ignored_classes)


@pytest.helpers.register
def list_all_abjad_functions(modules=None):
    return abjad.list_all_functions(modules="abjad")
