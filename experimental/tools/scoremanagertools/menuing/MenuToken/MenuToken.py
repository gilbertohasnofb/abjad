from abjad.tools import stringtools
from abjad.tools.abctools.AbjadObject import AbjadObject


class MenuToken(AbjadObject):
    '''Menu menu_token.

    Return menu menu_token.
    '''

    ### CLASS VARIABLES ###

    return_value_attributes = (
        'display_string', 
        'key', 
        'number', 
        'prepopulated',
        )

    ### INITIALIZER ###

    def __init__(self, expr, 
        number=None, 
        is_modern=False,
        return_value_attribute=None,
        ):
        assert return_value_attribute in self.return_value_attributes
        assert is_modern
        if isinstance(expr, str):
            expr = (expr, )
        assert isinstance(expr, (tuple, type(self))), repr(expr)
        self._number = number
        self._return_value_attribute = return_value_attribute
        if isinstance(expr, type(self)):
            display_string = expr.display_string
            key = expr.key
            existing_value = expr.existing_value
            prepopulated_return_value = expr.prepopulated_return_value
        elif len(expr) == 1:
            display_string = expr[0]
            key = None
            existing_value = None
            prepopulated_return_value = None
        elif len(expr) == 2:
            display_string = expr[0]
            key = expr[1]
            existing_value = None
            prepopulated_return_value = None
        elif len(expr) == 3:
            display_string = expr[0]
            key = expr[1]
            existing_value = expr[2]
            prepopulated_return_value = None
        elif len(expr) == 4:
            display_string = expr[0]
            key = expr[1]
            existing_value = expr[2]
            prepopulated_return_value = expr[3]
        else:
            raise ValueError(expr)
        assert display_string
        self._key = key
        self._display_string = display_string
        self._existing_value = existing_value
        self._prepopulated_return_value = prepopulated_return_value
        if self.return_value_attribute == 'number':
            return_value = str(self.number)
        elif self.return_value_attribute == 'display_string':
            return_value = self.display_string
        elif self.return_value_attribute == 'key':
            return_value = self.key
        elif self.return_value_attribute == 'prepopulated':
            return_value = self.prepopulated_return_value
        assert return_value
        self._return_value = return_value
        matches = []
        if self.number:
            matches.append(str(self.number))
        if self.key is not None:
            matches.append(self.key)
        self._matches = tuple(matches)
        normalized_display_string = \
            stringtools.strip_diacritics_from_binary_string(
            self.display_string)
        normalized_display_string = normalized_display_string.lower()
        self._normalized_display_string = normalized_display_string

    ### SPECIAL METHODS ###

    def __repr__(self):
        return '{}()'.format(self._class_name)

    ### PRIVATE METHODS ###

    def _to_tuple(self):
        return (
            self.key, 
            self.display_string, 
            self.existing_value, 
            self.prepopulated_return_value,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def display_string(self):
        return self._display_string

    @property
    def existing_value(self):
        return self._existing_value

    @property
    def key(self):
        return self._key

    @property
    def number(self):
        return self._number

    @property
    def prepopulated_return_value(self):
        return self._prepopulated_return_value

    @property
    def return_value(self):
        return self._return_value

    @property
    def return_value_attribute(self):
        return self._return_value_attribute

    ### PUBLIC METHODS ###

    def matches(self, user_input):
        if user_input in self._matches:
            return True
        if 3 <= len(user_input):
            if self._normalized_display_string.startswith(user_input):
                return True
        return False 
