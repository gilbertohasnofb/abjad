from experimental.settingtools.SingleContextSetting import SingleContextSetting


class ResolvedSingleContextSetting(SingleContextSetting):
    r'''.. versionadded:: 1.0

    Resolved single-context setting::

        >>> from abjad.tools import *
        >>> from experimental import *

    Set `attribute` to `payload` for single-context `selector`::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecification(score_template)
        >>> segment = score_specification.append_segment('red')

    ::

        >>> multiple_context_setting = segment.set_time_signatures([(4, 8), (3, 8)])

    ::

        >>> contexts = ['Voice 1', 'Voice 3']
        >>> multiple_context_setting = segment.set_divisions([(3, 16)], contexts=contexts)

    ::

        >>> score = score_specification.interpret()

    ::

        >>> resolved_single_context_setting = \
        ...     score_specification.resolved_single_context_settings['Voice 1']['divisions'][0]

    ::

        >>> z(resolved_single_context_setting)
        settingtools.ResolvedSingleContextSetting(
            'divisions',
            [(3, 16)],
            [(3, 16)],
            selectortools.SingleSegmentSelector(
                identifier='red'
                ),
            context_name='Voice 1',
            persist=True,
            truncate=False,
            fresh=True
            )

    Composers do not create resolved single-context settings.

    Resolved single-context settings are a byproduct of interpretation.

    Resolved single-context settings are create from single-context settings.

    The `payload` of a resolved single-context setting derives from
    the `source` of a single-context setting.
    '''

    ### INITIALIZER ###

    def __init__(self, attribute, source, payload, selector, context_name=None, 
        index=None, count=None, reverse=None, rotation=None, callback=None,
        persist=True, truncate=False, fresh=True):
        SingleContextSetting.__init__(self, 
            attribute, source, selector, context_name=context_name, 
            index=index, count=count, reverse=reverse, rotation=rotation, callback=callback,
            persist=persist, truncate=truncate)
        assert payload is not None, repr(payload)
        self._payload = payload

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def payload(self):
        '''Setting payload.
        '''
        return self._payload
