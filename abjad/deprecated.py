import copy

from .core.Component import attach
from .core.Iteration import Iteration
from .core.Leaf import Leaf
from .core.MultimeasureRest import MultimeasureRest
from .core.Selection import Selection
from .core.Voice import Voice
from .core.inspectx import Inspection
from .indicators.BarLine import BarLine
from .overrides import override
from .tags import Tag


def add_final_bar_line(score, abbreviation="|.", to_each_voice=False) -> BarLine:
    r"""
    Adds final bar line to end of score.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
        >>> score = abjad.Score([staff])
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
            >>

        >>> bar_line = abjad.deprecated.add_final_bar_line(score)
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
                    \bar "|." %! SCORE_1
                }
            >>

    Set ``to_each_voice`` to true to make part extraction easier.
    """
    bar_line = BarLine(abbreviation)
    if not to_each_voice:
        last_leaf = Inspection(score).leaf(-1)
        attach(bar_line, last_leaf, tag=Tag("SCORE_1"))
    else:
        for voice in Iteration(score).components(Voice):
            last_leaf = Inspection(voice).leaf(-1)
            attach(bar_line, last_leaf, tag=Tag("SCORE_1"))
    return bar_line


def add_final_markup(score, markup, extra_offset=None) -> None:
    r"""
    Adds ``markup`` to end of score.

    ..  container:: example

        Adds markup to last leaf:

        >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
        >>> score = abjad.Score([staff])
        >>> place = abjad.Markup('Bremen - Boston - LA.', direction=abjad.Down)
        >>> date = abjad.Markup('July 2010 - May 2011.')
        >>> markup = abjad.Markup.right_column([place, date], direction=abjad.Down)
        >>> markup = markup.italic()
        >>> markup = abjad.deprecated.add_final_markup(
        ...     score,
        ...     markup,
        ...     extra_offset=(0.5, -2),
        ...     )
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(score)
            \new Score
            <<
                \new Staff
                {
                    c'4
                    d'4
                    e'4
                    \once \override TextScript.extra-offset = #'(0.5 . -2)
                    f'4
                    _ \markup {                             %! SCORE_2
                        \italic                             %! SCORE_2
                            \right-column                   %! SCORE_2
                                {                           %! SCORE_2
                                    "Bremen - Boston - LA." %! SCORE_2
                                    "July 2010 - May 2011." %! SCORE_2
                                }                           %! SCORE_2
                        }                                   %! SCORE_2
                }
            >>

    ..  container:: example

        Adds markup to last multimeasure rest:

        >>> staff = abjad.Staff("c'4 d'4 e'4 f'4")
        >>> staff.append(abjad.MultimeasureRest((4, 4)))
        >>> score = abjad.Score([staff])
        >>> place = abjad.Markup(
        ...     'Bremen - Boston - LA.',
        ...     direction=abjad.Down,
        ...     )
        >>> date = abjad.Markup('July 2010 - May 2011.')
        >>> markup = abjad.Markup.right_column(
        ...     [place, date],
        ...     direction=abjad.Down,
        ...     )
        >>> markup = markup.italic()
        >>> markup = abjad.deprecated.add_final_markup(
        ...     score,
        ...     markup,
        ...     extra_offset=(14.5, -2),
        ...     )
        >>> abjad.show(staff) # doctest: +SKIP

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
                    \once \override MultiMeasureRestText.extra-offset = #'(14.5 . -2)
                    R1
                    _ \markup {                             %! SCORE_2
                        \italic                             %! SCORE_2
                            \right-column                   %! SCORE_2
                                {                           %! SCORE_2
                                    "Bremen - Boston - LA." %! SCORE_2
                                    "July 2010 - May 2011." %! SCORE_2
                                }                           %! SCORE_2
                        }                                   %! SCORE_2
                }
            >>

    """
    selection = Selection(score)
    last_leaf = selection._get_component(Leaf, -1)
    markup = copy.copy(markup)
    attach(markup, last_leaf, tag=Tag("SCORE_2"))
    if extra_offset is not None:
        if isinstance(last_leaf, MultimeasureRest):
            grob_proxy = override(last_leaf).multi_measure_rest_text
        else:
            grob_proxy = override(last_leaf).text_script
        grob_proxy.extra_offset = extra_offset
    return markup
