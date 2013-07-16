from abjad import *
import py.test


def test_Parentage_parentage_signature_01():
    '''An anonymous staff and its contained unvoiced leaves share the
    same parentage signature.
    '''

    t = Staff("c'8 d'8 e'8 f'8")

    containment = t.select_parentage().parentage_signature
    for component in iterationtools.iterate_components_in_expr(t):
        assert component.select_parentage().parentage_signature == containment


def test_Parentage_parentage_signature_02():
    '''A named staff and its contained unvoiced leaves share the
    same parentage signature.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.name = 'foo'

    containment = t.select_parentage().parentage_signature
    for component in iterationtools.iterate_components_in_expr(t):
        assert component.select_parentage().parentage_signature == containment


def test_Parentage_parentage_signature_03():
    '''Leaves inside equally named sequential voices inside a Staff
    share the same parentage signature.
    '''

    t = Staff(Voice("c'8 d'8 e'8 f'8") * 2)
    t[0].name = 'foo'
    t[1].name = 'foo'

    containment = t[0][0].select_parentage().parentage_signature
    for leaf in t.select_leaves():
        assert leaf.select_parentage().parentage_signature == containment


def test_Parentage_parentage_signature_04():
    '''Return ContainmentSignature giving the root and
    first voice, staff and score in the parentage of component.
    '''

    t = Voice(notetools.make_repeated_notes(4))
    t.insert(2, Container(Voice(notetools.make_repeated_notes(2)) * 2))
    t[2].is_parallel = True
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    t.override.note_head.color = 'red'

    r'''
    \new Voice \with {
        \override NoteHead #'color = #red
    } {
        c'8
        d'8
        <<
            \new Voice {
                e'8
                f'8
            }
            \new Voice {
                g'8
                a'8
            }
        >>
        b'8
        c''8
    }
    '''

    signatures = [leaf.select_parentage().parentage_signature 
        for leaf in t.select_leaves()]

    assert signatures[0] == signatures[1]
    assert signatures[0] != signatures[2]
    assert signatures[0] != signatures[4]
    assert signatures[0] == signatures[6]

    assert signatures[2] == signatures[3]
    assert signatures[2] != signatures[4]


def test_Parentage_parentage_signature_05():
    '''Unicorporated leaves carry different parentage signatures.
    '''

    t1 = Note(0, (1, 8))
    t2 = Note(0, (1, 8))

    assert t1.select_parentage().parentage_signature != \
        t2.select_parentage().parentage_signature


def test_Parentage_parentage_signature_06():
    '''Leaves inside different Staves with the same name have the same
    parentage signature.
    '''

    t = Container(Staff(notetools.make_repeated_notes(2)) * 2)
    t[0].name = t[1].name = 'staff'

    r'''
    {
        \context Staff = "staff" {
            c'8
            c'8
        }
        \context Staff = "staff" {
            c'8
            c'8
        }
    }
    '''

    assert t.select_leaves()[0].select_parentage().parentage_signature == \
        t.select_leaves()[1].select_parentage().parentage_signature
    assert t.select_leaves()[0].select_parentage().parentage_signature == \
        t.select_leaves()[2].select_parentage().parentage_signature
    assert t.select_leaves()[2].select_parentage().parentage_signature == \
        t.select_leaves()[3].select_parentage().parentage_signature
    assert t.select_leaves()[2].select_parentage().parentage_signature == \
        t.select_leaves()[0].select_parentage().parentage_signature

    assert t.select_leaves()[0].select_parentage().parentage_signature == \
        t.select_leaves()[1].select_parentage().parentage_signature
