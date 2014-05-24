# -*- encoding: utf-8 -*-
import abc
import os
import readline
import subprocess
import sys
import traceback
from abjad.tools import datastructuretools
from abjad.tools import stringtools
from abjad.tools import systemtools
from abjad.tools.systemtools.IOManager import IOManager


class IOManager(IOManager):
    r'''IO manager.

    ..  container:: example

        ::

            >>> score_manager = scoremanager.core.ScoreManager(is_test=True)
            >>> io_manager = score_manager._session.io_manager

    '''

    ### CLASS VARAIBLES ###

    __slots__ = (
        '_client',
        '_configuration',
        '_session',
        )

    ### INITIALIZER ###

    def __init__(self, client=None, session=None):
        from scoremanager import core
        self._client = client
        self._configuration = core.ScoreManagerConfiguration()
        self._session = session

    ### SPECIAL METHODS ###

    def __repr__(self):
        r'''Gets interpreter representation of IO manager.

        ..  container:: example

            ::

                >>> io_manager
                IOManager()

        Returns string.
        '''
        return '{}()'.format(type(self).__name__)

    ### PRIVATE METHODS ###

    def _confirm(
        self,
        prompt_string='ok?',
        include_chevron=False,
        ):
        getter = self._make_getter(
            include_chevron=include_chevron,
            include_newlines=False,
            )
        getter.append_yes_no_string(prompt_string)
        result = getter._run()
        if isinstance(result, str):
            if 'yes'.startswith(result.lower()):
                return True

    def _display(self, lines, capitalize=True):
        assert isinstance(lines, (str, list))
        if isinstance(lines, str):
            lines = [lines]
        if capitalize:
            lines = [
                stringtools.capitalize_start(line)
                for line in lines
                ]
        if lines:
            self._session.transcript._append_entry(lines)
        if not self._session.pending_input:
            for line in lines:
                print(line)

    @staticmethod
    def _get_greatest_version_number(version_directory):
        if not os.path.isdir(version_directory):
            return 0
        greatest_number = 0
        for entry in os.listdir(version_directory):
            base_name, extension = os.path.splitext(entry)
            number = 0
            try:
                number = int(base_name[-4:])
            except ValueError:
                pass
            if greatest_number < number:
                greatest_number = number
        return greatest_number

    @staticmethod
    def _get_one_line_menu_summary(expr):
        if isinstance(expr, (type, abc.ABCMeta)):
            return expr.__name__
        elif getattr(expr, '_one_line_menu_summary', None):
            return expr._one_line_menu_summary
        elif isinstance(expr, str):
            return expr
        else:
            return repr(expr)

    def _handle_input(
        self,
        prompt_string,
        default_value=None,
        include_chevron=True,
        include_newline=False,
        prompt_character='>',
        capitalize_prompt=True,
        ):
        r'''Handles user input.
        Appends user input to command history.
        Appends user input to IO transcript.
        Returns command selected by user.
        '''
        if default_value in (None, 'None'):
            default_value = ''
        readline.set_startup_hook(lambda: readline.insert_text(default_value))
        found_default_token = False
        try:
            if capitalize_prompt:
                prompt_string = stringtools.capitalize_start(
                    prompt_string)
            if include_chevron:
                prompt_string = prompt_string + prompt_character + ' '
            else:
                prompt_string = prompt_string + ' '
            if not self._session.pending_input:
                if sys.version_info[0] == 2:
                    input_ = raw_input(prompt_string)
                else:
                    input_ = input(prompt_string)
                if include_newline:
                    if not input_ == 'help':
                        print('')
            else:
                input_ = self._pop_from_pending_input()
                if input_ == '<return>':
                    found_default_token = True
            if not found_default_token:
                self._session.command_history.append(input_)
            if input_ == '.':
                last_semantic_command = self._session.last_semantic_command
                input_ = last_semantic_command
            if found_default_token:
                menu_chunk = [prompt_string.strip()]
                if include_newline:
                    if not input_ == 'help':
                        menu_chunk.append('')
                self._session.transcript._append_entry(menu_chunk)
                menu_chunk = ['> ']
                if include_newline:
                    if not input_ == 'help':
                        menu_chunk.append('')
                self._session.transcript._append_entry(menu_chunk)
            else:
                menu_chunk = []
                menu_chunk.append('{}{}'.format(prompt_string, input_))
                if include_newline:
                    if not input_ == 'help':
                        menu_chunk.append('')
                self._session.transcript._append_entry(menu_chunk)
            return input_
        finally:
            readline.set_startup_hook()

    def _make_autoeditor(
        self, 
        allow_item_edit=True,
        breadcrumb=None,
        target=None,
        ):
        from scoremanager import iotools
        prototype = (
            list,
            datastructuretools.TypedList,
            )
        if isinstance(target, prototype):
            class_ = iotools.ListAutoeditor
            return class_(
                allow_item_edit=allow_item_edit,
                breadcrumb=breadcrumb,
                session=self._session,
                target=target,
                )
        else:
            class_ = iotools.Autoeditor
            return class_(
                breadcrumb=breadcrumb,
                session=self._session,
                target=target,
                )

    def _make_getter(
        self,
        allow_none=False,
        include_chevron=True,
        include_newlines=False,
        ):
        from scoremanager import iotools
        getter = iotools.UserInputGetter(
            session=self._session,
            allow_none=allow_none,
            include_chevron=include_chevron,
            include_newlines=include_newlines,
            )
        return getter

    def _make_interaction(self, display=True, dry_run=False, task=True):
        from scoremanager import iotools
        return iotools.Interaction(
            controller=self.client, 
            display=display,
            dry_run=dry_run,
            task=task,
            )

    def _make_menu(
        self,
        breadcrumb_callback=None,
        name=None,
        ):
        from scoremanager import iotools
        return iotools.Menu(
            breadcrumb_callback=breadcrumb_callback,
            name=name,
            session=self._session,
            )

    def _make_package_manager(self, path):
        from scoremanager import managers
        return managers.PackageManager(
            path=path,
            session=self._session,
            )

    def _make_selector(
        self,
        breadcrumb=None,
        is_ranged=False,
        items=None,
        ):
        from scoremanager import iotools
        return iotools.Selector(
            breadcrumb=breadcrumb,
            is_ranged=is_ranged,
            items=items,
            session=self._session,
            )

    def _make_silent(self):
        from scoremanager import iotools
        return iotools.Interaction(
            confirm=False,
            controller=self.client,
            display=False,
            dry_run=False,
            task=False,
            )

    def _make_tab(self, n=1):
        return 4 * n * ' '

    def _pop_from_pending_input(self):
        self._session._last_command_was_composite = False
        if self._session.pending_input is None:
            return None
        elif self._session._pending_input == '':
            self._session._pending_input = None
            return None
        elif self._session.pending_input.startswith('{{'):
            index = self._session.pending_input.find('}}')
            input_ = self._session.pending_input[2:index]
            pending_input = self._session.pending_input[index+2:]
            pending_input = pending_input.strip()
            self._session._last_command_was_composite = True
        else:
            input_parts = self._session.pending_input.split(' ')
            first_parts, rest_parts = [], []
            for i, part in enumerate(input_parts):
                if not part.endswith((',', '-')):
                    break
            first_parts = input_parts[:i+1]
            rest_parts = input_parts[i+1:]
            input_ = ' '.join(first_parts)
            pending_input = ' '.join(rest_parts)
        input_ = input_.replace('~', ' ')
        self._session._pending_input = pending_input
        return input_

    def _display_not_yet_implemented(self):
        r'''Prints not-yet-implemented message.

        Returns none.
        '''
        with self._make_interaction():
            message = 'not yet implemented.'
            self._display(message)

    ### PUBLIC PROPERTIES ###

    @property
    def client(self):
        r'''Gets client of IO manager.

        Returns score manager object.
        '''
        return self._client

    @property
    def selector(self):
        r'''Gets dummy selector.

        Use for access to selector make methods.

        Returns selector.
        '''
        from scoremanager import iotools
        return iotools.Selector(session=self._session)

    ### PUBLIC METHODS ###

    def edit(self, path, line_number=None):
        r'''Edits file `path`.

        Opens at `line_number` when `line_number` is set.

        Opens at first line when `line_number` is not set.

        Returns none.
        '''
        if not os.path.isfile(path):
            return
        if line_number is None:
            command = 'vim + {}'.format(path)
        else:
            command = 'vim +{} {}'.format(line_number, path)
        self._session._attempted_to_open_file = True
        if self._session.is_test:
            return
        self.spawn_subprocess(command)

    def execute_file(self, path=None, attribute_names=None):
        r'''Executes file `path`.

        Returns `attribute_names` from file.
        '''
        assert path is not None
        assert isinstance(attribute_names, tuple)
        if not os.path.isfile(path):
            return
        with open(path, 'r') as file_pointer:
            file_contents_string = file_pointer.read()
        try:
            exec(file_contents_string)
        except:
            traceback.print_exc()
            return 'corrupt'
        result = []
        for name in attribute_names:
            if name in locals():
                result.append(locals()[name])
            else:
                result.append(None)
        result = tuple(result)
        return result

    def interpret_file(self, path, confirm=True, display=True):
        r'''Invokes Python or LilyPond on `path`.

        Returns integer success code.
        '''
        with self._make_interaction():
            _, extension = os.path.splitext(path)
            if extension == '.py':
                command = 'python {}'.format(path)
            elif extension == '.ly':
                command = 'lilypond {}'.format(path)
            else:
                message = 'can not interpret {}.'.format(path)
                raise Exception(message)
            directory = os.path.dirname(path)
            directory = systemtools.TemporaryDirectoryChange(directory)
            with directory:
                result = self.spawn_subprocess(command)
            if display:
                message = 'interpreted {}.'.format(path)
                self._display(message)
            return result

    def invoke_shell(self, statement=None):
        r'''Invokes shell on `statement`.

        Returns none.
        '''
        with self._make_interaction():
            lines = []
            prompt = True
            if statement is None:
                statement = self._handle_input(
                    '$',
                    include_chevron=False,
                    include_newline=False,
                    )
            statement = statement.strip()
            process = subprocess.Popen(
                statement,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                )
            try:
                lines = [str(x) for x in process.stdout.readlines()]
            except:
                lines.append('expression not executable.')
            lines = lines or []
            lines = [_.strip() for _ in lines]
            self._display(lines, capitalize=False)

    def open_file(self, path):
        r'''Opens file `path`.

        Also works when `path` is a list.

        Returns none.
        '''
        if not isinstance(path, list) and not os.path.isfile(path):
            return
        if (isinstance(path, list) and
            all(x.endswith('.pdf') for x in path)):
            paths = path
            paths = ' '.join(paths)
            command = 'open {}'.format(paths)
        elif isinstance(path, list):
            paths = path
            paths = ' '.join(paths)
            command = 'vim {}'.format(paths)
        elif path.endswith('.pdf'):
            command = 'open {}'.format(path)
        else:
            command = 'vim -R {}'.format(path)
        self._session._attempted_to_open_file = True
        if self._session.is_test:
            return
        self.spawn_subprocess(command)

    def run_command(self, command, capitalize=True):
        r'''Makes subprocess with `command` and then runs and displays
        output of subprocess.

        Returns none.
        '''
        process = self.make_subprocess(command)
        lines = [str(line).strip() for line in process.stdout.readlines()]
        if not lines:
            return
        self._display(
            lines,
            capitalize=capitalize,
            )

    def run_lilypond(self, path, confirm=True, display=True):
        r'''Runs LilyPond on file `path`.

        Returns none.
        '''
        with self._make_interaction():
            if self.find_executable('lily'):
                executable = 'lily'
            elif self.find_executable('lilypond'):
                executable = 'lilypond'
            else:
                message = 'cannot find LilyPond executable.'
                raise ValueError(message)
            command = '{} {}'.format(
                executable,
                path,
                )
            input_directory = os.path.dirname(path)
            with systemtools.TemporaryDirectoryChange(input_directory):
                self.spawn_subprocess(command)

    def write(self, path, string):
        r'''Writes `string` to `path`.

        Returns none.
        '''
        with open(path, 'w') as file_pointer:
            file_pointer.write(string)

    def write_stub(self, path):
        r'''Writes Unicode directive to otherwise empty file at `path`.

        Returns none.
        '''
        with open(path, 'w') as file_pointer:
            file_pointer.write(self._configuration.unicode_directive)