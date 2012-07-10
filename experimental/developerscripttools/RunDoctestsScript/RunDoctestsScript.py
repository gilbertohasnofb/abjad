from abjad import *
from experimental import *
from abjad.tools import iotools
from experimental.developerscripttools.DirectoryScript import DirectoryScript
import doctest
import os


class RunDoctestsScript(DirectoryScript):

    ### PUBLIC READ-ONLY PROPERTIES ###

    @property
    def alias(self):
        return 'doctest'

    @property
    def long_description(self):
        return None

    @property
    def scripting_group(self):
        return None

    @property
    def short_description(self):
        return 'Run doctests on all modules in current path.'

    @property
    def version(self):
        return 1.0

    ### PUBLIC PROPERTIES ###

    def process_args(self, args):
        iotools.clear_terminal()
        total_modules = 0
        for dir_path, dir_names, file_names in os.walk('.'):
            for file_name in file_names:
                if file_name.endswith('.py') and \
                    not file_name.startswith('test_') and \
                    not file_name == '__init__.py':
                    total_modules += 1
                    full_file_name = os.path.abspath(os.path.join(dir_path, file_name))
                    doctest.testfile(full_file_name, module_relative = False, globs = globals(),
                       optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
        print 'Total modules: %s' % total_modules

    def setup_argument_parser(self, parser):
        pass
