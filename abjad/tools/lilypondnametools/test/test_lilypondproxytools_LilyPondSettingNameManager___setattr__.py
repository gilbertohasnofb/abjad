# -*- coding: utf-8 -*-
from abjad import *


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___01():
    r'''Define LilyPond autoBeaming context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).auto_beaming = True

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            autoBeaming = ##t
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___02():
    r'''Remove LilyPond autoBeaming context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).auto_beaming = True
    del(setting(staff).auto_beaming)

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___03():
    r'''Define LilyPond currentBarNumber context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff[0]).score.current_bar_number = 12

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff {
            \set Score.currentBarNumber = #12
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___04():
    r'''Define LilyPond currentBarNumber context setting.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    setting(staff[0]).score.current_bar_number = 12

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff {
            {
                \set Score.currentBarNumber = #12
                \time 2/8
                c'8
                d'8
            }
            {
                e'8
                f'8
            }
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___05():
    r'''Define LilyPond fontSize context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).font_size = -3

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            fontSize = #-3
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___06():
    r'''Define LilyPond instrumentName context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).instrument_name = 'Violini I'

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            instrumentName = #"Violini I"
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___07():
    r'''Define LilyPond instrumentName context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).instrument_name = markuptools.Markup(r'\circle { V }')

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            instrumentName = \markup {
                \circle
                    {
                        V
                    }
                }
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___08():
    r'''Define LilyPond proportionalNotationDuration context setting.
    '''

    score = Score([Staff("c'8 d'8 e'8 f'8")])
    moment = schemetools.SchemeMoment(Fraction(1, 56))
    setting(score).proportional_notation_duration = moment

    assert format(score) == stringtools.normalize(
        r'''
        \new Score \with {
            proportionalNotationDuration = #(ly:make-moment 1 56)
        } <<
            \new Staff {
                c'8
                d'8
                e'8
                f'8
            }
        >>
        '''
        )

    assert inspect(score).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___09():
    r'''Define LilyPond shortInstrumentName context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).short_instrument_name = 'Vni. I'

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            shortInstrumentName = #"Vni. I"
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___10():
    r'''Define LilyPond shortInstrumentName context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).short_instrument_name = markuptools.Markup(
        r'\circle { V }')

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            shortInstrumentName = \markup {
                \circle
                    {
                        V
                    }
                }
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___11():
    r'''Define LilyPond suggestAccidentals context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff).suggest_accidentals = True

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            suggestAccidentals = ##t
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___12():
    r'''Define LilyPond suggestAccidentals context setting.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    setting(staff[1]).suggest_accidentals = True

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff {
            c'8
            \set suggestAccidentals = ##t
            d'8
            e'8
            f'8
        }
        '''
        )

    assert inspect(staff).is_well_formed()


def test_lilypondproxytools_LilyPondSettingNameManager___setattr___13():
    r'''Define LilyPond tupletFullLength context setting.
    '''

    staff = Staff([])
    setting(staff).tuplet_full_length = True

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            tupletFullLength = ##t
        } {
        }
        '''
        )

    assert not len(staff)

    setting(staff).tuplet_full_length = False

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff \with {
            tupletFullLength = ##f
        } {
        }
        '''
        )

    assert not len(staff)

    del(setting(staff).tuplet_full_length)

    assert format(staff) == stringtools.normalize(
        r'''
        \new Staff {
        }
        '''
        )

    assert not len(staff)