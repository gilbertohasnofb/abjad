from abjad import *
import py.test


def test_lily_voice_resolution_01( ):
   '''Anonymous voice with a sequence of leaves,
   in the middle of which there is a parallel,
   which in turn contains two anonymous voices.
   How does LilyPond resolve voices?
   '''

   t = Voice(leaftools.make_repeated_notes(4))
   t.insert(2, Container(Voice(leaftools.make_repeated_notes(2)) * 2))
   t[2].parallel = True
   pitchtools.diatonicize(t)
   t.note_head.color = 'red'

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
   }'''

   '''LilyPond identifies three separate voices.
   LilyPond colors the outer four notes (c'8 d'8 b'8 c''8) red.
   LilyPond colors the inner four notes black.
   LilyPond issues clashing note column warnings for the inner notes. 
   How should Abjad resolve voices?
   '''


def test_lily_voice_resolution_02( ):
   '''Named voice with  with a sequence of leaves,
   in the middle of which there is a parallel,
   which in turn contains one like-named and one differently named voice.
   How does LilyPond resolve voices?
   '''

   t = Voice(leaftools.make_repeated_notes(4))
   t.name = 'foo'
   t.insert(2, Container(Voice(leaftools.make_repeated_notes(2)) * 2))
   t[2].parallel = True
   t[2][0].name = 'foo'
   pitchtools.diatonicize(t)
   t.note_head.color = 'red'

   r'''
   \context Voice = "foo" \with {
           \override NoteHead #'color = #red
   } {
           c'8
           d'8
           <<
                   \context Voice = "foo" {
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

   '''LilyPond colors six notes red and two notes black.
   LilyPond identifies two voices.
   ''' 


def test_lily_voice_resolution_03( ):
   '''Two like-named voices in two differently named staves.'''

   t = Container(Staff([Voice(macros.scale(2))]) * 2)
   t[0].name = 'staff1'
   t[1].name = 'staff2'
   t[0][0].name = 'voicefoo'
   t[1][0].name = 'voicefoo'
   pitchtools.diatonicize(t)
   py.test.raises(AssertionError, 'Beam(t.leaves)')

   '''LilyPond gives unterminated beam warnings.
   LilyPond gives grob direction programming errors.
   We conclude that LilyPond identifies two separate voices.
   Good example for Abjad voice resolution.
   '''


def test_lily_voice_resolution_04( ):
   '''Container containing a run of leaves.
   Two like-structured parallels in the middle of the run.
   '''

   t = Container(leaftools.make_repeated_notes(2))
   t[1:1] = Container(Voice(leaftools.make_repeated_notes(2)) * 2) * 2
   t[1].parallel = True
   t[1][0].name = 'alto'
   t[1][1].name = 'soprano'
   t[2][0].name = 'alto'
   t[2][1].name = 'soprano'
   pitchtools.diatonicize(t)

   t[1][1][0].directives.before.append(r"\override NoteHead #'color = #red")
   t[2][1][-1].directives.after.append(r"\revert NoteHead #'color")

   r'''
   {
           c'8
           <<
                   \context Voice = "alto" {
                           d'8
                           e'8
                   }
                   \context Voice = "soprano" {
                           \override NoteHead #'color = #red
                           f'8
                           g'8
                   }
           >>
           <<
                   \context Voice = "alto" {
                           a'8
                           b'8
                   }
                   \context Voice = "soprano" {
                           c''8
                           d''8
                           \revert NoteHead #'color
                   }
           >>
           e''8
   }
   '''

   '''LilyPond handles this example perfectly.
   LilyPond colors the four note_heads of the soprano voice red.
   LilyPond colors all other note_heads black.
   '''
