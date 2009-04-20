from abjad import *
import py.test


def test_split_container_unfractured_01( ):
   '''Hew triplet.'''

   t = Voice(FixedDurationTuplet((2, 8), construct.run(3)) * 2)
   pitchtools.diatonicize(t)
   p = Beam(t[:])

   r'''\new Voice {
           \times 2/3 {
                   c'8
                   d'8
                   e'8
           }
           \times 2/3 {
                   f'8
                   g'8
                   a'8
           }
   }'''

   split.container_unfractured(t[1], 1)

   r'''\new Voice {
           \times 2/3 {
                   c'8 [
                   d'8
                   e'8
           }
           \times 2/3 {
                   f'8
           }
           \times 2/3 {
                   g'8
                   a'8 ]
           }
   }'''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\\times 2/3 {\n\t\tc'8 [\n\t\td'8\n\t\te'8\n\t}\n\t\\times 2/3 {\n\t\tf'8\n\t}\n\t\\times 2/3 {\n\t\tg'8\n\t\ta'8 ]\n\t}\n}"


def test_split_container_unfractured_02( ):
   '''Hew binary measure.'''

   t = Voice(RigidMeasure((3, 8), construct.run(3)) * 2)
   pitchtools.diatonicize(t)
   p = Beam(t[:])

   r'''\new Voice {
                   \time 3/8
                   c'8 [
                   d'8
                   e'8
                   \time 3/8
                   f'8
                   g'8
                   a'8 ]
   }'''

   split.container_unfractured(t[1], 1)

   r'''\new Voice {
                   \time 3/8
                   c'8 [
                   d'8
                   e'8
                   \time 1/8
                   f'8
                   \time 2/8
                   g'8
                   a'8 ]
   }'''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\t\\time 3/8\n\t\tc'8 [\n\t\td'8\n\t\te'8\n\t\t\\time 1/8\n\t\tf'8\n\t\t\\time 2/8\n\t\tg'8\n\t\ta'8 ]\n}"


def test_split_container_unfractured_03( ):
   '''Hew nonbinary measure.'''

   t = Voice(RigidMeasure((3, 9), construct.run(3)) * 2)
   pitchtools.diatonicize(t)
   p = Beam(t[:])

   r'''\new Voice {
                   \time 3/9
                   \scaleDurations #'(8 . 9) {
                           c'8 [
                           d'8
                           e'8
                   }
                   \time 3/9
                   \scaleDurations #'(8 . 9) {
                           f'8
                           g'8
                           a'8 ]
                   }
   }'''

   split.container_unfractured(t[1], 1)

   r'''\new Voice {
                   \time 3/9
                   \scaleDurations #'(8 . 9) {
                           c'8 [
                           d'8
                           e'8
                   }
                   \time 1/9
                   \scaleDurations #'(8 . 9) {
                           f'8
                   }
                   \time 2/9
                   \scaleDurations #'(8 . 9) {
                           g'8
                           a'8 ]
                   }
   }'''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\t\\time 3/9\n\t\t\\scaleDurations #'(8 . 9) {\n\t\t\tc'8 [\n\t\t\td'8\n\t\t\te'8\n\t\t}\n\t\t\\time 1/9\n\t\t\\scaleDurations #'(8 . 9) {\n\t\t\tf'8\n\t\t}\n\t\t\\time 2/9\n\t\t\\scaleDurations #'(8 . 9) {\n\t\t\tg'8\n\t\t\ta'8 ]\n\t\t}\n}"


def test_split_container_unfractured_04( ):
   '''A single container can be split in two by the middle;
      no parent.'''

   t = Voice(construct.scale(4))
   t1, t2 = split.container_unfractured(t, 2)

   r'''\new Voice {
      c'8
      d'8
   }
   \new Voice {
      e'8
      f'8
   }'''

   assert check.wf(t1)
   assert check.wf(t2)
   assert t1.format == "\\new Voice {\n\tc'8\n\td'8\n}"
   assert t2.format == "\\new Voice {\n\te'8\n\tf'8\n}"
   

def test_split_container_unfractured_05( ):
   '''A single container 'split' at index 0 gives
      an empty lefthand part and a complete righthand part.
      Original container empties contents.'''

   t = Staff([Voice(construct.scale(4))])
   v = t[0]
   Beam(v)
   left, right = split.container_unfractured(v, 0)

   r'''\new Staff {
           \new Voice {
                   c'8 [
                   d'8
                   e'8
                   f'8 ]
           }
   }'''

   assert check.wf(t)
   assert left.format == '\\new Voice {\n}'
   assert right.format == "\\new Voice {\n\tc'8 [\n\td'8\n\te'8\n\tf'8 ]\n}"
   assert t.format == "\\new Staff {\n\t\\new Voice {\n\t\tc'8 [\n\t\td'8\n\t\te'8\n\t\tf'8 ]\n\t}\n}"


def test_split_container_unfractured_06( ):
   '''Split container at index > len(container).
      Lefthand part instantiates with all contents.
      Righthand part instantiates empty.
      Original container empties contents.'''

   t = Staff([Voice(construct.scale(4))])
   v = t[0]
   left, right = split.container_unfractured(v, 10)

   assert check.wf(t)
   assert left.format == "\\new Voice {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"
   assert right.format == '\\new Voice {\n}'
   assert v.format == '\\new Voice {\n}'
   assert t.format == "\\new Staff {\n\t\\new Voice {\n\t\tc'8\n\t\td'8\n\t\te'8\n\t\tf'8\n\t}\n}"


def test_split_container_unfractured_07( ):
   '''Voice can be split but automatic reinsertion to parent
      raises ContiguityError.'''

   t = Staff([Voice(construct.scale(4))])
   v = t[0]
   #assert py.test.raises(ContiguityError, 'split.container_unfractured(v, -2)')

   left, right = split.container_unfractured(v, -2)
   assert check.wf(t)
   assert left.format == "\\new Voice {\n\tc'8\n\td'8\n}"
   assert right.format == "\\new Voice {\n\te'8\n\tf'8\n}"
   assert v.format == '\\new Voice {\n}'
   assert t.format == "\\new Staff {\n\t\\new Voice {\n\t\tc'8\n\t\td'8\n\t}\n\t\\new Voice {\n\t\te'8\n\t\tf'8\n\t}\n}"


def test_split_container_unfractured_08( ):
   '''Spanners attached to hewn container reattach
      to all resulting hewn parts.'''

   t = Staff([Container(construct.scale(4))])
   v = t[0]
   Beam(v)
   left, right = split.container_unfractured(v, 2)

   r'''\new Staff {
      {
         c'8 [
         d'8
      }
      {
         e'8
         f'8 ]
      }
   }'''

   assert check.wf(t)
   assert left.format == "{\n\tc'8 [\n\td'8\n}"
   assert right.format == "{\n\te'8\n\tf'8 ]\n}"
   assert v.format == '{\n}'
   assert t.format == "\\new Staff {\n\t{\n\t\tc'8 [\n\t\td'8\n\t}\n\t{\n\t\te'8\n\t\tf'8 ]\n\t}\n}"


   
def test_split_container_unfractured_09( ):
   '''Hewing a container with parent results in parented 
      sibling containers.'''

   t = Staff([Voice([FixedMultiplierTuplet((4, 5), construct.run(5))])])
   v = t[0]
   tuplet = v[0]
   Beam(tuplet)
   left, right = split.container_unfractured(tuplet, 2)

   r'''\new Staff {
           \new Voice {
                   \times 4/5 {
                           c'8 [
                           c'8
                   }
                   \times 4/5 {
                           c'8
                           c'8
                           c'8 ]
                   }
           }
   }'''

   assert check.wf(t)
   assert left.format == "\\times 4/5 {\n\tc'8 [\n\tc'8\n}"
   assert right.format == "\\times 4/5 {\n\tc'8\n\tc'8\n\tc'8 ]\n}"
   assert tuplet.format == '\\times 4/5 {\n}'
   assert v.format == "\\new Voice {\n\t\\times 4/5 {\n\t\tc'8 [\n\t\tc'8\n\t}\n\t\\times 4/5 {\n\t\tc'8\n\t\tc'8\n\t\tc'8 ]\n\t}\n}"
   assert t.format == "\\new Staff {\n\t\\new Voice {\n\t\t\\times 4/5 {\n\t\t\tc'8 [\n\t\t\tc'8\n\t\t}\n\t\t\\times 4/5 {\n\t\t\tc'8\n\t\t\tc'8\n\t\t\tc'8 ]\n\t\t}\n\t}\n}"
