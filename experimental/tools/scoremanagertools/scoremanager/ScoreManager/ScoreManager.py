# -*- encoding: utf-8 -*-
import os
import subprocess
from experimental.tools.scoremanagertools.core.ScoreManagerObject import \
    ScoreManagerObject


class ScoreManager(ScoreManagerObject):
    '''Score manager.

    ::

        >>> score_manager = scoremanagertools.scoremanager.ScoreManager()
        >>> score_manager
        ScoreManager()

    Return score manager.
    '''

    ### INITIALIZER ###

    def __init__(self, session=None):
        from experimental.tools import scoremanagertools
        ScoreManagerObject.__init__(self, session=session)
        self._segment_package_wrangler = \
            scoremanagertools.wranglers.SegmentPackageWrangler(
            session=self._session)
        self._material_package_maker_wrangler = \
            scoremanagertools.wranglers.MaterialPackageMakerWrangler(
            session=self._session)
        self._material_package_wrangler = \
            scoremanagertools.wranglers.MaterialPackageWrangler(
            session=self._session)
        self._score_package_wrangler = \
            scoremanagertools.wranglers.ScorePackageWrangler(
            session=self._session)
        self._stylesheet_file_wrangler = \
            scoremanagertools.wranglers.StylesheetFileWrangler(
            session=self._session)

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return 'score manager'

    @property
    def _score_status_string(self):
        return '{} scores'.format(self._session.scores_to_show)

    ### PRIVATE METHODS ###

    def _get_next_score_package_name(self):
        score_package_names = self.score_package_wrangler.list_asset_names()
        if self._session.underscore_delimited_current_score_name is None:
            return score_package_names[0]
        index = score_package_names.index(
            self._session.underscore_delimited_current_score_name)
        next_index = (index + 1) % len(score_package_names)
        return score_package_names[next_index]

    def _get_prev_score_package_name(self):
        score_package_names = self.score_package_wrangler.list_asset_names()
        if self._session.underscore_delimited_current_score_name is None:
            return score_package_names[-1]
        index = score_package_names.index(
            self._session.underscore_delimited_current_score_name)
        prev_index = (index - 1) % len(score_package_names)
        return score_package_names[prev_index]

    def _handle_main_menu_result(self, result):
        if result in self.user_input_to_action:
            self.user_input_to_action[result](self)
        else:
            wrangler = self.score_package_wrangler
            if result in wrangler.list_visible_asset_packagesystem_paths():
                self.interactively_edit_score(result)

    def _handle_svn_menu_result(self, result):
        '''Return true to exit the svn menu.
        '''
        this_result = False
        if result == 'add':
            self.score_package_wrangler.svn_add_assets()
        elif result == 'ci':
            self.score_package_wrangler.svn_ci_assets()
        elif result == 'st':
            self.score_package_wrangler.svn_st_assets()
        elif result == 'up':
            self.score_package_wrangler.svn_up_assets()
            return True
        return this_result

    def _make_main_menu(self):
        menu = self._make_score_selection_menu()
        menu_section = menu.make_section(
            return_value_attribute='key',
            is_keyed=True,
            is_modern=True,
            )
        menu_section.append(('materials', 'm'))
        menu_section.append(('stylesheets', 'y'))
        menu_section.append(('new score', 'new'))
        hidden_section = menu.make_section(
            return_value_attribute='key',
            is_keyed=True,
            is_hidden=True,
            is_modern=True,
            )
        hidden_section.append(('show active scores only', 'active'))
        hidden_section.append(('show all scores', 'all'))
        hidden_section.append(('fix all score package structures', 'fix'))
        hidden_section.append(('show mothballed scores only', 'mb'))
        hidden_section.append(('profile packages', 'profile'))
        hidden_section.append(('run py.test on all scores', 'py.test'))
        hidden_section.append(('work with repository', 'svn'))
        hidden_section.append(('write cache', 'wc'))
        return menu

    def _make_score_selection_menu(self):
        if self._session.is_first_run:
            if hasattr(self, 'start_menu_tokens'):
                menu_tokens = self.start_menu_tokens
            else:
                self.write_cache()
                menu_tokens = self.score_package_wrangler._make_menu_tokens()
            self._session.is_first_run = False
        else:
            menu_tokens = self.score_package_wrangler._make_menu_tokens()
        menu, menu_section = self._io.make_menu(
            where=self._where,
            menu_tokens=menu_tokens,
            return_value_attribute='key',
            is_numbered=True,
            is_modern=True,
            )
        return menu

    def _make_svn_menu(self):
        menu, menu_section = self._io.make_menu(
            where=self._where,
            return_value_attribute='key',
            is_modern=True,
            )
        menu_section.append(('svn add scores', 'add'))
        menu_section.append(('svn commit scores', 'ci'))
        menu_section.append(('svn status scores', 'st'))
        menu_section.append(('svn update scores', 'up'))
        return menu

    def _run(self, 
        user_input=None, 
        clear=True, 
        cache=False, 
        is_test=False, 
        dump_transcript=False):
        type(self).__init__(self)
        self._io.assign_user_input(user_input=user_input)
        self._session.cache_breadcrumbs(cache=cache)
        self._session.push_breadcrumb(self._breadcrumb)
        if is_test:
            self._session.is_test = True
        self._session.dump_transcript = dump_transcript
        run_main_menu = True
        while True:
            self._session.push_breadcrumb(self._score_status_string)
            if run_main_menu:
                menu = self._make_main_menu()
                result = menu._run(clear=clear)
            else:
                run_main_menu = True
            if self._session.backtrack(source='home'):
                self._session.pop_breadcrumb()
                self._session.clean_up()
                break
            elif self._session.is_navigating_to_next_score:
                self._session.is_navigating_to_next_score = False
                self._session.is_backtracking_to_score_manager = False
                result = self._get_next_score_package_name()
            elif self._session.is_navigating_to_prev_score:
                self._session.is_navigating_to_prev_score = False
                self._session.is_backtracking_to_score_manager = False
                result = self._get_prev_score_package_name()
            elif not result:
                self._session.pop_breadcrumb()
                continue
            self._handle_main_menu_result(result)
            if self._session.backtrack(source='home'):
                self._session.pop_breadcrumb()
                self._session.clean_up()
                break
            elif self._session.is_navigating_to_sibling_score:
                run_main_menu = False
            self._session.pop_breadcrumb()
        self._session.pop_breadcrumb()
        self._session.restore_breadcrumbs(cache=cache)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def material_package_maker_wrangler(self):
        '''Score manager material package maker wrangler:

        ::

            >>> score_manager.material_package_maker_wrangler
            MaterialPackageMakerWrangler()

        Return material package maker wrangler.
        '''
        return self._material_package_maker_wrangler

    @property
    def material_package_wrangler(self):
        '''Score manager material package wrangler:

        ::

            >>> score_manager.material_package_wrangler
            MaterialPackageWrangler()

        Return material package wrangler.
        '''
        return self._material_package_wrangler

    @property
    def score_package_wrangler(self):
        '''Score manager score package wrangler:

        ::

            >>> score_manager.score_package_wrangler
            ScorePackageWrangler()

        Return score package wrangler.
        '''
        return self._score_package_wrangler

    @property
    def segment_package_wrangler(self):
        '''Score manager segment package wrangler:

        ::

            >>> score_manager.segment_package_wrangler
            SegmentPackageWrangler()

        Return segment package wrangler.
        '''
        return self._segment_package_wrangler

    @property
    def storage_format(self):
        '''Score manager storage format:

        ::

            >>> score_manager.storage_format
            'scoremanager.ScoreManager()'

        Return string.
        '''
        return super(ScoreManager, self).storage_format

    @property
    def stylesheet_file_wrangler(self):
        '''Score manager stylesheet file wrangler:

        ::

            >>> score_manager.stylesheet_file_wrangler
            StylesheetFileWrangler()

        Return stylesheet file wrangler.
        '''
        return self._stylesheet_file_wrangler

    ### PUBLIC METHODS ###

    def fix_visible_scores(self):
        self.score_package_wrangler.fix_visible_assets()

    def interactively_edit_score(self, score_package_path):
        proxy = self.score_package_wrangler._initialize_asset_proxy(
            score_package_path)
        proxy._session.underscore_delimited_current_score_name = \
            score_package_path
        proxy._run(cache=True)
        self._session.underscore_delimited_current_score_name = None

    def interactively_make_new_score(self):
        self.score_package_wrangler.interactively_make_asset(
            rollback=True)

    def manage_materials(self):
        self.material_package_wrangler._run(
            rollback=True, 
            head=self.configuration.built_in_material_packages_package_path)

    def manage_stylesheets(self):
        self.stylesheet_file_wrangler._run(
            rollback=True, 
            head=self.configuration.built_in_stylesheets_directory_path)

    def manage_svn(self, clear=True):
        while True:
            self._session.push_breadcrumb('repository commands')
            menu = self._make_svn_menu()
            result = menu._run(clear=clear)
            if self._session.is_backtracking_to_score:
                self._session.is_backtracking_to_score = False
                self._session.pop_breadcrumb()
                continue
            elif self._session.backtrack():
                break
            self._handle_svn_menu_result(result)
            if self._session.backtrack():
                break
            self._session.pop_breadcrumb()
        self._session.pop_breadcrumb()

    def profile_visible_scores(self):
        self.score_package_wrangler.profile_visible_assets()

    def run_py_test_on_all_user_scores(self, prompt=True):
        command = 'py.test {}'.format(
            self.configuration.user_score_packages_directory_path)
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        lines = [line.strip() for line in proc.stdout.readlines()]
        if lines:
            self._io.display(lines, capitalize_first_character=False)
        line = 'tests complete.'
        self._io.proceed(line, is_interactive=prompt)

    def show_active_scores(self):
        self._session.show_active_scores()

    def show_all_scores(self):
        self._session.show_all_scores()

    def show_mothballed_scores(self):
        self._session.show_mothballed_scores()

    def write_cache(self):
        cache_file_path = os.path.join(
                self.configuration.configuration_directory_path, 'cache.py')
        cache_file_pointer = file(cache_file_path, 'w')
        cache_file_pointer.write('start_menu_tokens = [\n')
        menu_tokens = self.score_package_wrangler._make_menu_tokens()
        for menu_token in menu_tokens:
            cache_file_pointer.write('{},\n'.format(menu_token))
        cache_file_pointer.write(']\n')
        cache_file_pointer.close()

    ### UI MANIFEST ###

    user_input_to_action = {
        'active':   show_active_scores,
        'all':      show_all_scores,
        'fix':      fix_visible_scores,
        'm':        manage_materials,
        'mb':       show_mothballed_scores,
        'new':      interactively_make_new_score,
        'profile':  profile_visible_scores,
        'py.test':  run_py_test_on_all_user_scores,
        'svn':      manage_svn,
        'y':        manage_stylesheets,
        'wc':       write_cache
        }
