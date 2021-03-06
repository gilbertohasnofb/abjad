import collections

from ..pitch.pitches import NamedPitch, Pitch
from ..pitch.sets import PitchSet
from ..storage import StorageFormatManager
from ..utilities.Expression import Expression
from ..utilities.OrderedDict import OrderedDict
from .Chord import Chord
from .Component import Component
from .Container import Container
from .Leaf import Leaf
from .MultimeasureRest import MultimeasureRest
from .Note import Note
from .Rest import Rest
from .Skip import Skip
from .inspectx import Inspection


class Iteration(object):
    r"""
    Iteration.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 e'4 d'4 f'4")
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                c'4
                e'4
                d'4
                f'4
            }

        >>> abjad.iterate(staff)
        Iteration(client=Staff("c'4 e'4 d'4 f'4"))

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = "Collaborators"

    __slots__ = ("_client",)

    ### INITIALIZER ###

    def __init__(self, client=None):
        assert not isinstance(client, str), repr(client)
        self._client = client

    ### SPECIAL METHODS ###

    def __repr__(self) -> str:
        """
        Delegates to storage format manager.
        """
        return StorageFormatManager(self).get_repr_format()

    ### PRIVATE METHODS ###

    @staticmethod
    def _coerce_exclude(exclude):
        if exclude is None:
            exclude = ()
        elif isinstance(exclude, str):
            exclude = (exclude,)
        else:
            exclude = tuple(exclude)
        assert isinstance(exclude, tuple), repr(exclude)
        return exclude

    @staticmethod
    def _iterate_components(
        client,
        prototype=None,
        *,
        exclude=None,
        do_not_iterate_grace_containers=None,
        grace=None,
        reverse=None,
    ):
        argument = client
        prototype = prototype or Component
        before_grace_container = None
        after_grace_container = None
        exclude = Iteration._coerce_exclude(exclude)
        assert isinstance(exclude, tuple), repr(exclude)
        if grace is not False and isinstance(argument, Leaf):
            inspection = Inspection(argument)
            before_grace_container = inspection.before_grace_container()
            after_grace_container = inspection.after_grace_container()
        if not reverse:
            if (
                not do_not_iterate_grace_containers
                and grace is not False
                and before_grace_container
            ):
                yield from Iteration._iterate_components(
                    before_grace_container,
                    prototype,
                    do_not_iterate_grace_containers=do_not_iterate_grace_containers,
                    grace=grace,
                    reverse=reverse,
                )
            if isinstance(argument, prototype):
                if (
                    grace is None
                    or (grace is True and Inspection(argument).grace())
                    or (grace is False and not Inspection(argument).grace())
                ):
                    if not Iteration._should_exclude(argument, exclude):
                        yield argument
            if (
                not do_not_iterate_grace_containers
                and grace is not False
                and after_grace_container
            ):
                yield from Iteration._iterate_components(
                    after_grace_container,
                    prototype,
                    exclude=exclude,
                    do_not_iterate_grace_containers=do_not_iterate_grace_containers,
                    grace=grace,
                    reverse=reverse,
                )
            if isinstance(argument, collections.abc.Iterable):
                for item in argument:
                    yield from Iteration._iterate_components(
                        item,
                        prototype,
                        exclude=exclude,
                        do_not_iterate_grace_containers=do_not_iterate_grace_containers,
                        grace=grace,
                        reverse=reverse,
                    )
        else:
            if (
                not do_not_iterate_grace_containers
                and grace is not False
                and after_grace_container
            ):
                yield from Iteration._iterate_components(
                    after_grace_container,
                    prototype,
                    exclude=exclude,
                    do_not_iterate_grace_containers=do_not_iterate_grace_containers,
                    grace=grace,
                    reverse=reverse,
                )
            if isinstance(argument, prototype):
                if (
                    grace is None
                    or (grace is True and Inspection(argument).grace())
                    or (grace is False and not Inspection(argument).grace())
                ):
                    if not Iteration._should_exclude(argument, exclude):
                        yield argument
            if (
                not do_not_iterate_grace_containers
                and grace is not False
                and before_grace_container
            ):
                yield from Iteration._iterate_components(
                    before_grace_container,
                    prototype,
                    exclude=exclude,
                    do_not_iterate_grace_containers=do_not_iterate_grace_containers,
                    grace=grace,
                    reverse=reverse,
                )
            if isinstance(argument, collections.abc.Iterable):
                for item in reversed(argument):
                    yield from Iteration._iterate_components(
                        item,
                        prototype,
                        exclude=exclude,
                        do_not_iterate_grace_containers=do_not_iterate_grace_containers,
                        grace=grace,
                        reverse=reverse,
                    )

    @staticmethod
    def _should_exclude(argument, exclude):
        assert isinstance(exclude, tuple)
        for string in exclude:
            if Inspection(argument).has_indicator(string):
                return True
        return False

    ### PUBLIC PROPERTIES ###

    @property
    def client(self):
        """
        Gets client.

        ..  container:: example

            >>> staff = abjad.Staff("c'4 d' e' f'")
            >>> abjad.iterate(staff[:2]).client
            Selection([Note("c'4"), Note("d'4")])

        Returns component or selection.
        """
        return self._client

    ### PUBLIC METHODS ###

    def components(self, prototype=None, *, exclude=None, grace=None, reverse=None):
        r"""
        Iterates components.

        ..  container:: example

            Grace iteration is controlled by a ternary flag.

            >>> music_voice = abjad.Voice("c'4 d' e' f'", name="Music_Voice")
            >>> container = abjad.BeforeGraceContainer("cs'16")
            >>> abjad.attach(container, music_voice[1])
            >>> container = abjad.on_beat_grace_container(
            ...     "g'16 gs' a' as'", music_voice[2:3]
            ... )
            >>> abjad.attach(abjad.Articulation(">"), container[0])
            >>> container = abjad.AfterGraceContainer("fs'16")
            >>> abjad.attach(container, music_voice[3])
            >>> staff = abjad.Staff([music_voice])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    \context Voice = "Music_Voice"
                    {
                        c'4
                        \grace {
                            cs'16
                        }
                        d'4
                        <<
                            \context Voice = "On_Beat_Grace_Container"
                            {
                                \set fontSize = #-3 %! abjad.on_beat_grace_container(1)
                                \slash %! abjad.on_beat_grace_container(2)
                                \voiceOne %! abjad.on_beat_grace_container(3)
                                <
                                    \tweak font-size #0
                                    \tweak transparent ##t
                                    e'
                                    g'
                                >16
                                - \accent
                                [
                                (
                                gs'16
                                a'16
                                as'16
                                )
                                ]
                            }
                            \context Voice = "Music_Voice"
                            {
                                \voiceTwo %! abjad.on_beat_grace_container(4)
                                e'4
                            }
                        >>
                        \oneVoice %! abjad.on_beat_grace_container(5)
                        \afterGrace
                        f'4
                        {
                            fs'16
                        }
                    }
                }

            Leave ``grace`` unset to iterate grace and nongrace components
            together:

            >>> for component in abjad.iterate(staff).components():
            ...     component
            <Staff{1}>
            <Voice-"Music_Voice"{4}>
            Note("c'4")
            BeforeGraceContainer("cs'16")
            Note("cs'16")
            Note("d'4")
            <<<2>>>
            OnBeatGraceContainer("<e' g'>16 gs'16 a'16 as'16")
            Chord("<e' g'>16")
            Note("gs'16")
            Note("a'16")
            Note("as'16")
            Voice("e'4", name='Music_Voice')
            Note("e'4")
            Note("f'4")
            AfterGraceContainer("fs'16")
            Note("fs'16")

            >>> for component in abjad.iterate(staff).components(reverse=True):
            ...     component
            <Staff{1}>
            <Voice-"Music_Voice"{4}>
            AfterGraceContainer("fs'16")
            Note("fs'16")
            Note("f'4")
            <<<2>>>
            Voice("e'4", name='Music_Voice')
            Note("e'4")
            OnBeatGraceContainer("<e' g'>16 gs'16 a'16 as'16")
            Note("as'16")
            Note("a'16")
            Note("gs'16")
            Chord("<e' g'>16")
            Note("d'4")
            BeforeGraceContainer("cs'16")
            Note("cs'16")
            Note("c'4")

            Set ``grace=True`` to iterate only grace components:

            >>> for component in abjad.iterate(staff).components(grace=True):
            ...     component
            BeforeGraceContainer("cs'16")
            Note("cs'16")
            OnBeatGraceContainer("<e' g'>16 gs'16 a'16 as'16")
            Chord("<e' g'>16")
            Note("gs'16")
            Note("a'16")
            Note("as'16")
            AfterGraceContainer("fs'16")
            Note("fs'16")

            >>> for component in abjad.iterate(staff).components(
            ...     grace=True, reverse=True
            ...     ):
            ...     component
            AfterGraceContainer("fs'16")
            Note("fs'16")
            OnBeatGraceContainer("<e' g'>16 gs'16 a'16 as'16")
            Note("as'16")
            Note("a'16")
            Note("gs'16")
            Chord("<e' g'>16")
            BeforeGraceContainer("cs'16")
            Note("cs'16")

            Set ``grace=False`` to iterate only nongrace components:

            >>> for component in abjad.iterate(staff).components(grace=False):
            ...     component
            <Staff{1}>
            <Voice-"Music_Voice"{4}>
            Note("c'4")
            Note("d'4")
            <<<2>>>
            Voice("e'4", name='Music_Voice')
            Note("e'4")
            Note("f'4")

            >>> for component in abjad.iterate(staff).components(
            ...     grace=False, reverse=True
            ...     ):
            ...     component
            <Staff{1}>
            <Voice-"Music_Voice"{4}>
            Note("f'4")
            <<<2>>>
            Voice("e'4", name='Music_Voice')
            Note("e'4")
            Note("d'4")
            Note("c'4")

        Returns generator.
        """
        if isinstance(self.client, Container):
            for component in self._iterate_components(
                self.client,
                prototype,
                exclude=exclude,
                do_not_iterate_grace_containers=False,
                grace=grace,
                reverse=reverse,
            ):
                yield component
        elif isinstance(self.client, collections.abc.Iterable):
            if not reverse:
                for item in self.client:
                    generator = Iteration(item).components(
                        prototype, exclude=exclude, grace=grace, reverse=reverse,
                    )
                    yield from generator
            else:
                for item in reversed(self.client):
                    generator = Iteration(item).components(
                        prototype, exclude=exclude, grace=grace, reverse=reverse,
                    )
                    yield from generator
        else:
            for component in self._iterate_components(
                self.client,
                prototype,
                exclude=exclude,
                do_not_iterate_grace_containers=True,
                grace=grace,
                reverse=reverse,
            ):
                yield component

    def leaves(
        self, prototype=None, *, exclude=None, grace=None, pitched=None, reverse=None,
    ):
        r"""
        Iterates leaves.

        ..  container:: example

            Set ``exclude=<annotation>`` to exclude leaves with annotation:

            >>> staff = abjad.Staff()
            >>> staff.extend("<c' bf'>8 <g' a'>8")
            >>> staff.extend("af'8 r8")
            >>> staff.extend("r8 gf'8")
            >>> abjad.attach(abjad.TimeSignature((2, 8)), staff[0])
            >>> abjad.attach("RED", staff[0])
            >>> abjad.attach("BLUE", staff[1])
            >>> abjad.attach("GREEN", staff[2])
            >>> abjad.attach("RED", staff[3])
            >>> abjad.attach("BLUE", staff[4])
            >>> abjad.attach("GREEN", staff[5])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    \time 2/8
                    <c' bf'>8
                    <g' a'>8
                    af'8
                    r8
                    r8
                    gf'8
                }

            >>> for leaf in abjad.iterate(staff).leaves(
            ...     exclude=['RED', 'BLUE'],
            ...     ):
            ...     leaf
            ...
            Note("af'8")
            Note("gf'8")

            Iteration excludes leaves ``'RED'`` or ``'BLUE'`` attached.

        ..  container:: example

            Grace iteration is controlled by a ternary flag.

            >>> music_voice = abjad.Voice("c'4 d' e' f'", name="Music_Voice")
            >>> container = abjad.BeforeGraceContainer("cs'16")
            >>> abjad.attach(container, music_voice[1])
            >>> container = abjad.on_beat_grace_container(
            ...     "g'16 gs' a' as'", music_voice[2:3]
            ... )
            >>> abjad.attach(abjad.Articulation(">"), container[0])
            >>> container = abjad.AfterGraceContainer("fs'16")
            >>> abjad.attach(container, music_voice[3])
            >>> staff = abjad.Staff([music_voice])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    \context Voice = "Music_Voice"
                    {
                        c'4
                        \grace {
                            cs'16
                        }
                        d'4
                        <<
                            \context Voice = "On_Beat_Grace_Container"
                            {
                                \set fontSize = #-3 %! abjad.on_beat_grace_container(1)
                                \slash %! abjad.on_beat_grace_container(2)
                                \voiceOne %! abjad.on_beat_grace_container(3)
                                <
                                    \tweak font-size #0
                                    \tweak transparent ##t
                                    e'
                                    g'
                                >16
                                - \accent
                                [
                                (
                                gs'16
                                a'16
                                as'16
                                )
                                ]
                            }
                            \context Voice = "Music_Voice"
                            {
                                \voiceTwo %! abjad.on_beat_grace_container(4)
                                e'4
                            }
                        >>
                        \oneVoice %! abjad.on_beat_grace_container(5)
                        \afterGrace
                        f'4
                        {
                            fs'16
                        }
                    }
                }

            Leave ``grace`` unset to iterate grace and nongrace leaves
            together:

            >>> for leaf in abjad.iterate(staff).leaves():
            ...     leaf
            Note("c'4")
            Note("cs'16")
            Note("d'4")
            Chord("<e' g'>16")
            Note("gs'16")
            Note("a'16")
            Note("as'16")
            Note("e'4")
            Note("f'4")
            Note("fs'16")

            Set ``grace=True`` to iterate only grace leaves:

            >>> for leaf in abjad.iterate(staff).leaves(grace=True):
            ...     leaf
            Note("cs'16")
            Chord("<e' g'>16")
            Note("gs'16")
            Note("a'16")
            Note("as'16")
            Note("fs'16")

            Set ``grace=False`` to iterate only nongrace leaves:

            >>> for leaf in abjad.iterate(staff).leaves(grace=False):
            ...     leaf
            Note("c'4")
            Note("d'4")
            Note("e'4")
            Note("f'4")

        ..  container:: example

            Pitched iteration is controlled by a ternary flag.

            >>> staff = abjad.Staff()
            >>> staff.extend("<c' bf'>8 <g' a'>8")
            >>> staff.extend("af'8 r8")
            >>> staff.extend("r8 gf'8")
            >>> abjad.attach(abjad.TimeSignature((2, 8)), staff[0])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    \time 2/8
                    <c' bf'>8
                    <g' a'>8
                    af'8
                    r8
                    r8
                    gf'8
                }

            Leaves ``pitched`` unset to iterate pitched and unpitched leaves
            together:

            >>> for leaf in abjad.iterate(staff).leaves():
            ...     leaf
            ...
            Chord("<c' bf'>8")
            Chord("<g' a'>8")
            Note("af'8")
            Rest('r8')
            Rest('r8')
            Note("gf'8")

            >>> for leaf in abjad.iterate(staff).leaves(reverse=True):
            ...     leaf
            Note("gf'8")
            Rest('r8')
            Rest('r8')
            Note("af'8")
            Chord("<g' a'>8")
            Chord("<c' bf'>8")

            Set ``pitched=True`` to iterate pitched leaves only:

            >>> for leaf in abjad.iterate(staff).leaves(pitched=True):
            ...     leaf
            ...
            Chord("<c' bf'>8")
            Chord("<g' a'>8")
            Note("af'8")
            Note("gf'8")

            >>> for leaf in abjad.iterate(staff).leaves(
            ...     pitched=True, reverse=True
            ...     ):
            ...     leaf
            Note("gf'8")
            Note("af'8")
            Chord("<g' a'>8")
            Chord("<c' bf'>8")

            Set ``pitched=False`` to iterate unpitched leaves only:

            >>> for leaf in abjad.iterate(staff).leaves(pitched=False):
            ...     leaf
            ...
            Rest('r8')
            Rest('r8')

            >>> for leaf in abjad.iterate(staff).leaves(pitched=False):
            ...     leaf
            ...
            Rest('r8')
            Rest('r8')

        Returns generator.
        """
        prototype = prototype or Leaf
        if pitched is True:
            prototype = (Chord, Note)
        elif pitched is False:
            prototype = (MultimeasureRest, Rest, Skip)
        return self.components(
            prototype=prototype, exclude=exclude, grace=grace, reverse=reverse
        )

    def logical_ties(
        self, *, exclude=None, grace=None, nontrivial=None, pitched=None, reverse=None,
    ):
        r"""
        Iterates logical ties.

        ..  container:: example

            Iterates logical ties:

            >>> string = r"c'4 ~ \times 2/3 { c'16 d'8 } e'8 f'4 ~ f'16"
            >>> staff = abjad.Staff(string)
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    ~
                    \times 2/3 {
                        c'16
                        d'8
                    }
                    e'8
                    f'4
                    ~
                    f'16
                }

            >>> for logical_tie in abjad.iterate(staff).logical_ties():
            ...     logical_tie
            ...
            LogicalTie([Note("c'4"), Note("c'16")])
            LogicalTie([Note("d'8")])
            LogicalTie([Note("e'8")])
            LogicalTie([Note("f'4"), Note("f'16")])

        ..  container:: example

            Grace iteration is controlled by a ternary flag.

            >>> music_voice = abjad.Voice("c'4 d' e' f'", name="Music_Voice")
            >>> container = abjad.BeforeGraceContainer("cs'16")
            >>> abjad.attach(container, music_voice[1])
            >>> container = abjad.on_beat_grace_container(
            ...     "g'16 gs' a' as'", music_voice[2:3]
            ... )
            >>> abjad.attach(abjad.Articulation(">"), container[0])
            >>> container = abjad.AfterGraceContainer("fs'16")
            >>> abjad.attach(container, music_voice[3])
            >>> staff = abjad.Staff([music_voice])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    \context Voice = "Music_Voice"
                    {
                        c'4
                        \grace {
                            cs'16
                        }
                        d'4
                        <<
                            \context Voice = "On_Beat_Grace_Container"
                            {
                                \set fontSize = #-3 %! abjad.on_beat_grace_container(1)
                                \slash %! abjad.on_beat_grace_container(2)
                                \voiceOne %! abjad.on_beat_grace_container(3)
                                <
                                    \tweak font-size #0
                                    \tweak transparent ##t
                                    e'
                                    g'
                                >16
                                - \accent
                                [
                                (
                                gs'16
                                a'16
                                as'16
                                )
                                ]
                            }
                            \context Voice = "Music_Voice"
                            {
                                \voiceTwo %! abjad.on_beat_grace_container(4)
                                e'4
                            }
                        >>
                        \oneVoice %! abjad.on_beat_grace_container(5)
                        \afterGrace
                        f'4
                        {
                            fs'16
                        }
                    }
                }

            Leave ``grace`` unset to iterate grace and nongrace logical ties
            together:

            >>> for lt in abjad.iterate(staff).logical_ties():
            ...     lt
            LogicalTie([Note("c'4")])
            LogicalTie([Note("cs'16")])
            LogicalTie([Note("d'4")])
            LogicalTie([Chord("<e' g'>16")])
            LogicalTie([Note("gs'16")])
            LogicalTie([Note("a'16")])
            LogicalTie([Note("as'16")])
            LogicalTie([Note("e'4")])
            LogicalTie([Note("f'4")])
            LogicalTie([Note("fs'16")])

            >>> for lt in abjad.iterate(staff).logical_ties(reverse=True):
            ...     lt
            LogicalTie([Note("fs'16")])
            LogicalTie([Note("f'4")])
            LogicalTie([Note("e'4")])
            LogicalTie([Note("as'16")])
            LogicalTie([Note("a'16")])
            LogicalTie([Note("gs'16")])
            LogicalTie([Chord("<e' g'>16")])
            LogicalTie([Note("d'4")])
            LogicalTie([Note("cs'16")])
            LogicalTie([Note("c'4")])

            Set ``grace=True`` to iterate grace logical ties only:

            >>> for lt in abjad.iterate(staff).logical_ties(grace=True):
            ...     lt
            LogicalTie([Note("cs'16")])
            LogicalTie([Chord("<e' g'>16")])
            LogicalTie([Note("gs'16")])
            LogicalTie([Note("a'16")])
            LogicalTie([Note("as'16")])
            LogicalTie([Note("fs'16")])

            >>> for lt in abjad.iterate(staff).logical_ties(
            ...     grace=True, reverse=True
            ...     ):
            ...     lt
            LogicalTie([Note("fs'16")])
            LogicalTie([Note("as'16")])
            LogicalTie([Note("a'16")])
            LogicalTie([Note("gs'16")])
            LogicalTie([Chord("<e' g'>16")])
            LogicalTie([Note("cs'16")])

            Set ``grace=False`` to iterate nongrace logical ties only:

            >>> for lt in abjad.iterate(staff).logical_ties(grace=False):
            ...     lt
            LogicalTie([Note("c'4")])
            LogicalTie([Note("d'4")])
            LogicalTie([Note("e'4")])
            LogicalTie([Note("f'4")])

            >>> for lt in abjad.iterate(staff).logical_ties(
            ...     grace=False, reverse=True
            ...     ):
            ...     lt
            LogicalTie([Note("f'4")])
            LogicalTie([Note("e'4")])
            LogicalTie([Note("d'4")])
            LogicalTie([Note("c'4")])

        ..  container:: example

            Logical tie triviality is controlled by a ternary flag.

            >>> string = r"c'4 ~ \times 2/3 { c'8 d'4 }"
            >>> string += r" e'4 ~ \times 2/3 { e'8 f' }"
            >>> staff = abjad.Staff(string)
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    ~
                    \times 2/3 {
                        c'8
                        d'4
                    }
                    e'4
                    ~
                    \tweak edge-height #'(0.7 . 0)
                    \times 2/3 {
                        e'8
                        f'8
                    }
                }

            Leave ``nontrivial`` unset to iterate trivial and nontrivial
            logical ties together:

            >>> for lt in abjad.iterate(staff).logical_ties():
            ...     lt
            LogicalTie([Note("c'4"), Note("c'8")])
            LogicalTie([Note("d'4")])
            LogicalTie([Note("e'4"), Note("e'8")])
            LogicalTie([Note("f'8")])

            >>> for lt in abjad.iterate(staff).logical_ties(reverse=True):
            ...     lt
            LogicalTie([Note("f'8")])
            LogicalTie([Note("e'4"), Note("e'8")])
            LogicalTie([Note("d'4")])
            LogicalTie([Note("c'4"), Note("c'8")])

            Set ``nontrivial=True`` to iterate nontrivial logical ties only:

            >>> for lt in abjad.iterate(staff).logical_ties(nontrivial=True):
            ...     lt
            LogicalTie([Note("c'4"), Note("c'8")])
            LogicalTie([Note("e'4"), Note("e'8")])

            >>> for lt in abjad.iterate(staff).logical_ties(
            ...     nontrivial=True, reverse=True
            ...     ):
            ...     lt
            LogicalTie([Note("e'4"), Note("e'8")])
            LogicalTie([Note("c'4"), Note("c'8")])

            Set ``nontrivial=False`` to iterate trivial logical ties only:

            >>> for lt in abjad.iterate(staff).logical_ties(nontrivial=False):
            ...     lt
            LogicalTie([Note("d'4")])
            LogicalTie([Note("f'8")])

            >>> for lt in abjad.iterate(staff).logical_ties(
            ...     nontrivial=False, reverse=True
            ...     ):
            ...     lt
            LogicalTie([Note("f'8")])
            LogicalTie([Note("d'4")])

        ..  container:: example

            Logical tie pitchedness is controlled by a ternary flag.

            >>> string = r"c'4 ~ \times 2/3 { c'8 r4 }"
            >>> string += r"d'4 ~ \times 2/3 { d'8 r4 }"
            >>> staff = abjad.Staff(string)
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'4
                    ~
                    \times 2/3 {
                        c'8
                        r4
                    }
                    d'4
                    ~
                    \times 2/3 {
                        d'8
                        r4
                    }
                }

            Leave ``pitched`` unset to iterate pitched and unpitched logical
            ties together:

            >>> for lt in abjad.iterate(staff).logical_ties():
            ...     lt
            LogicalTie([Note("c'4"), Note("c'8")])
            LogicalTie([Rest('r4')])
            LogicalTie([Note("d'4"), Note("d'8")])
            LogicalTie([Rest('r4')])

            >>> for lt in abjad.iterate(staff).logical_ties(reverse=True):
            ...     lt
            LogicalTie([Rest('r4')])
            LogicalTie([Note("d'4"), Note("d'8")])
            LogicalTie([Rest('r4')])
            LogicalTie([Note("c'4"), Note("c'8")])

            Set ``pitched=True`` to iterate pitched logical ties only:

            >>> for lt in abjad.iterate(staff).logical_ties(pitched=True):
            ...     lt
            LogicalTie([Note("c'4"), Note("c'8")])
            LogicalTie([Note("d'4"), Note("d'8")])

            >>> for lt in abjad.iterate(staff).logical_ties(
            ...     pitched=True, reverse=True
            ...     ):
            ...     lt
            LogicalTie([Note("d'4"), Note("d'8")])
            LogicalTie([Note("c'4"), Note("c'8")])

            Set ``pitched=False`` to iterate unpitched logical ties only:

            >>> for lt in abjad.iterate(staff).logical_ties(pitched=False):
            ...     lt
            LogicalTie([Rest('r4')])
            LogicalTie([Rest('r4')])

            >>> for lt in abjad.iterate(staff).logical_ties(
            ...     pitched=False, reverse=True
            ...     ):
            ...     lt
            LogicalTie([Rest('r4')])
            LogicalTie([Rest('r4')])

        ..  container:: example

            REGRESSION. Yields logical tie even when leaves are missing in
            input:

            >>> voice = abjad.Voice("c'8 [ ~ c' ~ c' d' ]")
            >>> abjad.show(voice) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(voice)
                \new Voice
                {
                    c'8
                    [
                    ~
                    c'8
                    ~
                    c'8
                    d'8
                    ]
                }

            >>> selection = voice[:2]
            >>> for logical_tie in abjad.iterate(selection).logical_ties():
            ...     logical_tie
            ...
            LogicalTie([Note("c'8"), Note("c'8"), Note("c'8")])

        Returns generator.
        """
        yielded_logical_ties = set()
        for leaf in self.leaves(
            exclude=exclude, grace=grace, pitched=pitched, reverse=reverse
        ):
            logical_tie = Inspection._get_logical_tie(leaf)
            if leaf is not logical_tie.head:
                continue
            if (
                nontrivial is None
                or (nontrivial is True and not logical_tie.is_trivial)
                or (nontrivial is False and logical_tie.is_trivial)
            ):
                if logical_tie not in yielded_logical_ties:
                    yielded_logical_ties.add(logical_tie)
                    yield logical_tie

    def pitches(self):
        r"""
        Iterates pitches.

        ..  container:: example

            Iterates pitches in container:

            >>> staff = abjad.Staff("c'8 d'8 e'8 f'8")
            >>> abjad.beam(staff[:])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    c'8
                    [
                    d'8
                    e'8
                    f'8
                    ]
                }

            >>> for pitch in abjad.iterate(staff).pitches():
            ...     pitch
            ...
            NamedPitch("c'")
            NamedPitch("d'")
            NamedPitch("e'")
            NamedPitch("f'")

        ..  container:: example

            Iterates pitches in pitch set:

            >>> pitch_set = abjad.PitchSet([0, 2, 4, 5])

            >>> for pitch in abjad.iterate(pitch_set).pitches():
            ...     pitch
            ...
            NumberedPitch(0)
            NumberedPitch(2)
            NumberedPitch(4)
            NumberedPitch(5)

        ..  container:: example

            Iterates different types of object in tuple:

            >>> argument = (
            ...     abjad.NamedPitch("c'"),
            ...     abjad.Note("d'4"),
            ...     abjad.Chord("<e' fs' g>4"),
            ...     )

            >>> for pitch in abjad.iterate(argument).pitches():
            ...     pitch
            ...
            NamedPitch("c'")
            NamedPitch("d'")
            NamedPitch('g')
            NamedPitch("e'")
            NamedPitch("fs'")

        Returns generator.
        """
        if isinstance(self.client, Pitch):
            pitch = NamedPitch(self.client)
            yield pitch
        result = []
        try:
            result.extend(self.client.pitches)
        except AttributeError:
            pass
        if isinstance(self.client, Chord):
            result.extend(self.client.written_pitches)
        elif isinstance(self.client, PitchSet):
            result.extend(sorted(list(self.client)))
        elif isinstance(self.client, (list, tuple, set)):
            for item in self.client:
                for pitch_ in Iteration(item).pitches():
                    result.append(pitch_)
        else:
            for leaf in Iteration(self.client).leaves():
                try:
                    result.append(leaf.written_pitch)
                except AttributeError:
                    pass
                try:
                    result.extedn(leaf.written_pitches)
                except AttributeError:
                    pass
        for pitch in result:
            yield pitch

    def timeline(self, prototype=None, *, exclude=None, reverse=None):
        r"""
        Iterates timeline.

        ..  container:: example

            Timeline-iterates leaves:

            >>> score = abjad.Score()
            >>> score.append(abjad.Staff("c'4 d'4 e'4 f'4"))
            >>> score.append(abjad.Staff("g'8 a'8 b'8 c''8"))
            >>> abjad.show(score) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(score)
                \new Score
                <<
                    \new Staff
                    {
                        c'4
                        d'4
                        e'4
                        f'4
                    }
                    \new Staff
                    {
                        g'8
                        a'8
                        b'8
                        c''8
                    }
                >>

            >>> for leaf in abjad.iterate(score).timeline():
            ...     leaf
            ...
            Note("c'4")
            Note("g'8")
            Note("a'8")
            Note("d'4")
            Note("b'8")
            Note("c''8")
            Note("e'4")
            Note("f'4")

            >>> for component in abjad.iterate(score).timeline(reverse=True):
            ...     component
            ...
            Note("f'4")
            Note("e'4")
            Note("c''8")
            Note("b'8")
            Note("d'4")
            Note("a'8")
            Note("g'8")
            Note("c'4")

        ..  container:: example

            REGRESSION. Works with grace note (and containers):

            >>> music_voice = abjad.Voice("c'4 d' e' f'", name="Music_Voice")
            >>> container = abjad.BeforeGraceContainer("cs'16")
            >>> abjad.attach(container, music_voice[1])
            >>> container = abjad.on_beat_grace_container(
            ...     "g'16 gs' a' as'", music_voice[2:3]
            ... )
            >>> abjad.attach(abjad.Articulation(">"), container[0])
            >>> container = abjad.AfterGraceContainer("fs'16")
            >>> abjad.attach(container, music_voice[3])
            >>> staff = abjad.Staff([music_voice])
            >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff
                {
                    \context Voice = "Music_Voice"
                    {
                        c'4
                        \grace {
                            cs'16
                        }
                        d'4
                        <<
                            \context Voice = "On_Beat_Grace_Container"
                            {
                                \set fontSize = #-3 %! abjad.on_beat_grace_container(1)
                                \slash %! abjad.on_beat_grace_container(2)
                                \voiceOne %! abjad.on_beat_grace_container(3)
                                <
                                    \tweak font-size #0
                                    \tweak transparent ##t
                                    e'
                                    g'
                                >16
                                - \accent
                                [
                                (
                                gs'16
                                a'16
                                as'16
                                )
                                ]
                            }
                            \context Voice = "Music_Voice"
                            {
                                \voiceTwo %! abjad.on_beat_grace_container(4)
                                e'4
                            }
                        >>
                        \oneVoice %! abjad.on_beat_grace_container(5)
                        \afterGrace
                        f'4
                        {
                            fs'16
                        }
                    }
                }

            >>> for leaf in abjad.iterate(staff).timeline():
            ...     leaf
            Note("c'4")
            Note("cs'16")
            Note("d'4")
            Chord("<e' g'>16")
            Note("gs'16")
            Note("a'16")
            Note("as'16")
            Note("e'4")
            Note("f'4")
            Note("fs'16")

            >>> for leaf in abjad.iterate(staff).timeline(reverse=True):
            ...     leaf
            Note("fs'16")
            Note("f'4")
            Note("e'4")
            Note("as'16")
            Note("a'16")
            Note("gs'16")
            Chord("<e' g'>16")
            Note("d'4")
            Note("cs'16")
            Note("c'4")

        Iterates leaves when ``prototype`` is none.
        """
        components = self.leaves(prototype=prototype, exclude=exclude)
        components = list(components)
        components.sort(key=lambda _: Inspection(_).timespan().start_offset)
        offset_to_components = OrderedDict()
        for component in components:
            start_offset = Inspection(component).timespan().start_offset
            if start_offset not in offset_to_components:
                offset_to_components[start_offset] = []
        for component in components:
            start_offset = Inspection(component).timespan().start_offset
            offset_to_components[start_offset].append(component)
        components = []
        for start_offset, list_ in offset_to_components.items():
            components.extend(list_)
        if reverse:
            components.reverse()
        return tuple(components)


### FUNCTIONS ###


def iterate(client=None):
    r"""
    Makes iteration agent.

    ..  container:: example

        Iterates leaves:

        >>> staff = abjad.Staff("c'4 e'4 d'4 f'4")
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                c'4
                e'4
                d'4
                f'4
            }

        >>> for leaf in abjad.iterate(staff).leaves():
        ...     leaf
        ...
        Note("c'4")
        Note("e'4")
        Note("d'4")
        Note("f'4")

    """
    if client is not None:
        return Iteration(client=client)
    expression = Expression()
    expression = expression.iterate()
    return expression
