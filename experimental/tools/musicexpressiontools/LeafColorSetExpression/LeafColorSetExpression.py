from abjad.tools import labeltools
from experimental.tools.musicexpressiontools.LeafSetExpression \
    import LeafSetExpression


class LeafColorSetExpression(LeafSetExpression):
    r'''Leaf color set expression.
    '''

    ### PUBLIC METHODS ###

    def execute_against_score(self, score):
        r'''Execute note head color set expression against `score`.
        '''
        color = self.source_expression.payload
        for leaf in self._iterate_selected_leaves_in_score(score):
            labeltools.color_leaf(leaf, color)
            leaf.override.beam.color = color
            leaf.override.flag.color = color
            leaf.override.stem.color = color
