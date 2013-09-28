# -*- encoding: utf-8 -*-
import os
from abjad.tools import iotools
from abjad.tools import stringtools
from experimental.tools.scoremanagertools.managers.FileManager \
    import FileManager


class ModuleManager(FileManager):

    ### INITIALIZER ###

    def __init__(self, filesystem_path=None, session=None):
        assert filesystem_path is None or \
            os.path.sep in filesystem_path, repr(filesystem_path)
        FileManager.__init__(
            self,
            filesystem_path=filesystem_path,
            session=session,
            )
        packagesystem_path = \
            self.configuration.filesystem_path_to_packagesystem_path(
            filesystem_path,
            )
        self._packagesystem_path = packagesystem_path

    ### PRIVATE METHODS ###

    def _get_space_delimited_lowercase_name(self):
        if self.filesystem_path:
            base_name = os.path.basename(self.filesystem_path)
            name = base_name.strip('.py')
            name = stringtools.string_to_space_delimited_lowercase(name)
            return name

    def _space_delimited_lowercase_name_to_asset_name(
        self, space_delimited_lowercase_name):
        asset_name = FileManager._space_delimited_lowercase_name_to_asset_name(
            self, space_delimited_lowercase_name)
        asset_name += '.py'
        return asset_name

    ### PUBLIC METHODS ###

    def execute_file_lines(self, return_attribute_name=None):
        if os.path.isfile(self.filesystem_path):
            file_pointer = open(self.filesystem_path, 'r')
            file_contents_string = file_pointer.read()
            file_pointer.close()
            try:
                exec(file_contents_string)
            except Exception:
                return
            if isinstance(return_attribute_name, str):
                if return_attribute_name in locals():
                    return locals()[return_attribute_name]
            elif isinstance(return_attribute_name, (list, tuple)):
                result = []
                for name in return_attribute_name:
                    if name in locals():
                        result.append(locals()[name])
                    else:
                        result.append(None)
                result = tuple(result)
                return result

    def interpret_in_external_process(self):
        command = 'python {}'.format(self.filesystem_path)
        result = iotools.spawn_subprocess(command)
        if result != 0:
            self.session.io_manager.display('')
            self.session.io_manager.proceed()

    def run_abjad(self, prompt=True):
        command = 'abjad {}'.format(self.filesystem_path)
        iotools.spawn_subprocess(command)
        message = 'file executed.'
        self.session.io_manager.proceed(message, is_interactive=prompt)

    def run_python(self, prompt=True):
        command = 'python {}'.format(self.filesystem_path)
        iotools.spawn_subprocess(command)
        message = 'file executed.'
        self.session.io_manager.proceed(message, is_interactive=prompt)
