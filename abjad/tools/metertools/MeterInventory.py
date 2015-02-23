# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import markuptools
from abjad.tools import sequencetools
from abjad.tools import timespantools
from abjad.tools.datastructuretools.TypedList import TypedList


class MeterInventory(TypedList):
    r'''An ordered list of meters.

    ..  container:: example

        ::

            >>> inventory = metertools.MeterInventory([
            ...     (3, 4), (5, 16), (7, 8),
            ...     ])
            >>> print(format(inventory))
            metertools.MeterInventory(
                [
                    metertools.Meter(
                        '(3/4 (1/4 1/4 1/4))'
                        ),
                    metertools.Meter(
                        '(5/16 (1/16 1/16 1/16 1/16 1/16))'
                        ),
                    metertools.Meter(
                        '(7/8 ((3/8 (1/8 1/8 1/8)) (2/8 (1/8 1/8)) (2/8 (1/8 1/8))))'
                        ),
                    ]
                )

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### SPECIAL METHODS ###

    def __illustrate__(self, denominator=16, range_=None, scale=None):
        r'''Illustrates meter inventory.

        ..  container:: example

            ::

                >>> meter_inventory = metertools.MeterInventory([
                ...     (3, 4), (5, 16), (7, 8),
                ...     ])
                >>> show(meter_inventory, scale=0.5) # doctest: +SKIP

            ..  doctest

                >>> illustration = meter_inventory.__illustrate__()
                >>> print(format(illustration))
                % ...
                <BLANKLINE>
                \version "..."
                \language "english"
                <BLANKLINE>
                \header {
                    tagline = \markup {}
                }
                <BLANKLINE>
                \layout {}
                <BLANKLINE>
                \paper {}
                <BLANKLINE>
                \markup {
                    \combine
                        \combine
                            \combine
                                \combine
                                    \postscript
                                        #"
                                        0.2 setlinewidth
                                        1.0 -2.0 moveto
                                        49.3870967742 -2.0 lineto
                                        stroke
                                        1.0 -1.25 moveto
                                        1.0 -2.75 lineto
                                        stroke
                                        49.3870967742 -1.25 moveto
                                        49.3870967742 -2.75 lineto
                                        stroke
                                        49.3870967742 -2.0 moveto
                                        69.5483870968 -2.0 lineto
                                        stroke
                                        49.3870967742 -1.25 moveto
                                        49.3870967742 -2.75 lineto
                                        stroke
                                        69.5483870968 -1.25 moveto
                                        69.5483870968 -2.75 lineto
                                        stroke
                                        69.5483870968 -2.0 moveto
                                        126.0 -2.0 lineto
                                        stroke
                                        69.5483870968 -1.25 moveto
                                        69.5483870968 -2.75 lineto
                                        stroke
                                        126.0 -1.25 moveto
                                        126.0 -2.75 lineto
                                        stroke
                                        "
                                    \postscript
                                        #"
                                        1.0 -4.0 moveto
                                        0.0 -6.15384615385 rlineto
                                        stroke
                                        5.03225806452 -4.0 moveto
                                        0.0 -1.53846153846 rlineto
                                        stroke
                                        9.06451612903 -4.0 moveto
                                        0.0 -3.07692307692 rlineto
                                        stroke
                                        13.0967741935 -4.0 moveto
                                        0.0 -1.53846153846 rlineto
                                        stroke
                                        17.1290322581 -4.0 moveto
                                        0.0 -4.61538461538 rlineto
                                        stroke
                                        21.1612903226 -4.0 moveto
                                        0.0 -1.53846153846 rlineto
                                        stroke
                                        25.1935483871 -4.0 moveto
                                        0.0 -3.07692307692 rlineto
                                        stroke
                                        29.2258064516 -4.0 moveto
                                        0.0 -1.53846153846 rlineto
                                        stroke
                                        33.2580645161 -4.0 moveto
                                        0.0 -4.61538461538 rlineto
                                        stroke
                                        37.2903225806 -4.0 moveto
                                        0.0 -1.53846153846 rlineto
                                        stroke
                                        41.3225806452 -4.0 moveto
                                        0.0 -3.07692307692 rlineto
                                        stroke
                                        45.3548387097 -4.0 moveto
                                        0.0 -1.53846153846 rlineto
                                        stroke
                                        49.3870967742 -4.0 moveto
                                        0.0 -6.15384615385 rlineto
                                        stroke
                                        49.3870967742 -4.0 moveto
                                        0.0 -10.0 rlineto
                                        stroke
                                        53.4193548387 -4.0 moveto
                                        0.0 -5.0 rlineto
                                        stroke
                                        57.4516129032 -4.0 moveto
                                        0.0 -5.0 rlineto
                                        stroke
                                        61.4838709677 -4.0 moveto
                                        0.0 -5.0 rlineto
                                        stroke
                                        65.5161290323 -4.0 moveto
                                        0.0 -5.0 rlineto
                                        stroke
                                        69.5483870968 -4.0 moveto
                                        0.0 -10.0 rlineto
                                        stroke
                                        69.5483870968 -4.0 moveto
                                        0.0 -5.51724137931 rlineto
                                        stroke
                                        73.5806451613 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        77.6129032258 -4.0 moveto
                                        0.0 -2.75862068966 rlineto
                                        stroke
                                        81.6451612903 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        85.6774193548 -4.0 moveto
                                        0.0 -2.75862068966 rlineto
                                        stroke
                                        89.7096774194 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        93.7419354839 -4.0 moveto
                                        0.0 -4.13793103448 rlineto
                                        stroke
                                        97.7741935484 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        101.806451613 -4.0 moveto
                                        0.0 -2.75862068966 rlineto
                                        stroke
                                        105.838709677 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        109.870967742 -4.0 moveto
                                        0.0 -4.13793103448 rlineto
                                        stroke
                                        113.903225806 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        117.935483871 -4.0 moveto
                                        0.0 -2.75862068966 rlineto
                                        stroke
                                        121.967741935 -4.0 moveto
                                        0.0 -1.37931034483 rlineto
                                        stroke
                                        126.0 -4.0 moveto
                                        0.0 -5.51724137931 rlineto
                                        stroke
                                        "
                                \translate
                                    #'(1.0 . 1)
                                    \sans
                                        \fontsize
                                            #-3
                                            \center-align
                                                \fraction
                                                    3
                                                    4
                            \translate
                                #'(49.3870967742 . 1)
                                \sans
                                    \fontsize
                                        #-3
                                        \center-align
                                            \fraction
                                                5
                                                16
                        \translate
                            #'(69.5483870968 . 1)
                            \sans
                                \fontsize
                                    #-3
                                    \center-align
                                        \fraction
                                            7
                                            8
                    }

        Returns LilyPond file.
        '''
        from abjad.tools import metertools
        durations = [_.duration for _ in self]
        total_duration = sum(durations)
        offsets = mathtools.cumulative_sums(durations, start=0)
        timespan_inventory = timespantools.TimespanInventory()
        for one, two in sequencetools.iterate_sequence_nwise(offsets):
            timespan = timespantools.Timespan(
                start_offset=one,
                stop_offset=two,
                )
            timespan_inventory.append(timespan)

        if range_ is not None:
            minimum, maximum = range_
        else:
            minimum, maximum = 0, total_duration
        minimum = float(durationtools.Offset(minimum))
        maximum = float(durationtools.Offset(maximum))
        if scale is None:
            scale = 1.
        assert 0 < scale
        postscript_scale = 125. / (maximum - minimum)
        postscript_scale *= float(scale)
        postscript_x_offset = (minimum * postscript_scale) - 1
        timespan_markup = timespan_inventory._make_timespan_inventory_markup(
            timespan_inventory,
            postscript_x_offset,
            postscript_scale,
            draw_offsets=False,
            )
        ps = markuptools.Postscript()
        rational_x_offset = durationtools.Offset(0)
        for meter in self:
            kernel_denominator = denominator or meter.denominator
            kernel = metertools.MetricAccentKernel.from_meter(
                meter, kernel_denominator)
            for offset, weight in sorted(kernel.kernel.items()):
                weight = float(weight) * -40
                ps_x_offset = float(rational_x_offset + offset)
                ps_x_offset *= postscript_scale
                ps_x_offset += 1
                ps = ps.moveto(ps_x_offset, -4)
                ps = ps.rlineto(0, weight)
                ps = ps.stroke()
            rational_x_offset += meter.duration
        ps = markuptools.Markup.postscript(ps)
        markup = markuptools.Markup.combine(timespan_markup, ps)
        for meter, offset in zip(self, offsets):
            numerator, denominator = meter.numerator, meter.denominator
            fraction = markuptools.Markup.fraction(numerator, denominator)
            fraction = fraction.center_align().fontsize(-3).sans()
            x_translation = (float(offset) * postscript_scale)
            x_translation -= postscript_x_offset
            fraction = fraction.translate((x_translation, 1))
            markup = markuptools.Markup.combine(markup, fraction)
        return markup.__illustrate__()

    ### PRIVATE PROPERTIES ###

    @property
    def _item_coercer(self):
        from abjad.tools import metertools
        return metertools.Meter