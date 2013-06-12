from experimental import *


def test_Menu_menu_token_return_values_01():

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    section_1 = menu.make_section(is_modern=True)
    section_1.append('apple')
    section_1.append('banana')
    section_1.append('cherry')
    section_1.title = 'section'
    section_2 = menu.make_section(is_modern=True)
    section_2.append(('add something', 'add'))
    section_2.append(('delete something', 'rm'))
    section_2.append(('modify something', 'mod'))

    assert menu.menu_token_return_values[-6:] == \
        section_1.menu_token_return_values + \
        section_2.menu_token_return_values
