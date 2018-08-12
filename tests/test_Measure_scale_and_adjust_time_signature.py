import abjad
import pytest


def test_Measure_scale_and_adjust_time_signature_01():
    """
    Scales power-of-two measure to non-power-of-two measure.
    No note-head rewriting necessary.
    """

    measure = abjad.Measure((3, 8), "c'8 d'8 e'8")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(2, 3))

    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            #(ly:expect-warning "strange time signature found")
            \time 3/12
            \scaleDurations #'(2 . 3) {
                c'8
                d'8
                e'8
            }
        }   % measure
        """
        )

    assert abjad.inspect(measure).is_wellformed()



def test_Measure_scale_and_adjust_time_signature_02():
    """
    Scale non-power-of-two time signature to power-of-two.
    No note-head rewriting necessary.
    """

    measure = abjad.Measure((3, 12), "c'8 d'8 e'8")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(3, 2))

    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 3/8
            c'8
            d'8
            e'8
        }   % measure
        """
        )

    assert abjad.inspect(measure).is_wellformed()


def test_Measure_scale_and_adjust_time_signature_03():
    """
    Scale power-of-two time signature to power-of-two time signature.
    Note-heads rewrite with dots.
    """

    measure = abjad.Measure((3, 8), "c'8 d'8 e'8")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(3, 2))

    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 9/16
            c'8.
            d'8.
            e'8.
        }   % measure
        """
        )

    assert abjad.inspect(measure).is_wellformed()


def test_Measure_scale_and_adjust_time_signature_04():
    """
    Scale power-of-two time signature to power-of-two time signature.
    Note-heads rewrite without dots.
    """

    measure = abjad.Measure((9, 16), "c'8. d'8. e'8.")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(2, 3))

    assert abjad.inspect(measure).is_wellformed()
    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 3/8
            c'8
            d'8
            e'8
        }   % measure
        """
        )


def test_Measure_scale_and_adjust_time_signature_05():
    """
    Scale power-of-two time signature to non-power-of-two time signature.
    No note-head rewriting necessary.
    """

    measure = abjad.Measure((9, 16), "c'16 d'16 e'16 f'16 g'16 a'16 b'16 c''16 d''16")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(2, 3))

    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            #(ly:expect-warning "strange time signature found")
            \time 9/24
            \scaleDurations #'(2 . 3) {
                c'16
                d'16
                e'16
                f'16
                g'16
                a'16
                b'16
                c''16
                d''16
            }
        }   % measure
        """
        )

    assert abjad.inspect(measure).is_wellformed()


def test_Measure_scale_and_adjust_time_signature_06():
    """
    Scale non-power-of-two time signature to power-of-two time signature.
    Note-heads rewrite with double duration.
    """

    measure = abjad.Measure((3, 12), "c'8 d'8 e'8")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(3))

    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 3/4
            c'4
            d'4
            e'4
        }   % measure
        """
        )

    assert abjad.inspect(measure).is_wellformed()


def test_Measure_scale_and_adjust_time_signature_07():
    """
    Scale power-of-two time signature by one half.
    Note-heads rewrite with half duration.
    Time signature rewrites with double denominator.
    """

    measure = abjad.Measure((6, 16), "c'16 d'16 e'16 f'16 g'16 a'16")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(1, 2))

    assert abjad.inspect(measure).is_wellformed()
    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 6/32
            c'32
            d'32
            e'32
            f'32
            g'32
            a'32
        }   % measure
        """
        )


def test_Measure_scale_and_adjust_time_signature_08():
    """
    Scale power-of-two time signature by one quarter.
    Note-heads rewrite with quarter duration.
    Time signature rewrites with quadruple denominator.
    """

    measure = abjad.Measure((6, 16), "c'16 d'16 e'16 f'16 g'16 a'16")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(1, 4))

    assert abjad.inspect(measure).is_wellformed()
    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 6/64
            c'64
            d'64
            e'64
            f'64
            g'64
            a'64
        }   % measure
        """
        )


def test_Measure_scale_and_adjust_time_signature_09():
    """
    Scale power-of-two time signature by two.
    Note-heads rewrite with double duration.
    Time signature rewrites with half denominator.
    """

    measure = abjad.Measure((6, 16), "c'16 d'16 e'16 f'16 g'16 a'16")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(2))

    assert abjad.inspect(measure).is_wellformed()
    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 6/8
            c'8
            d'8
            e'8
            f'8
            g'8
            a'8
        }   % measure
        """
        )


def test_Measure_scale_and_adjust_time_signature_10():
    """
    Scale power-of-two time signature by four.
    Note-heads rewrite with quadruple duration.
    Time signature rewrites with quarter denominator.
    """

    measure = abjad.Measure((6, 16), "c'16 d'16 e'16 f'16 g'16 a'16")
    measure.scale_and_adjust_time_signature(abjad.Multiplier(4))

    assert abjad.inspect(measure).is_wellformed()
    assert format(measure) == abjad.String.normalize(
        r"""
        {   % measure
            \time 6/4
            c'4
            d'4
            e'4
            f'4
            g'4
            a'4
        }   % measure
        """
        )
