MIN_LOWER_ALPHA = 97
MAX_LOWER_ALPHA = 122

MIN_UPPER_ALPHA = 65
MAX_UPPER_ALPHA = 90

MIN_NUM_CODE = 48
MAX_NUM_CODE = 57

DASH_CODE = 45
DOT_CODE = 46
UNDERSCORE_CODE = 95

AT_CODE = 64


# noinspection PyBroadException
class EmailValidator:

    def __init__(self):
        pass

    def validate(self, email: str):
        errors = []

        email = email.replace('[at]', '@')
        email = email.replace('[.at]', '@')
        email = email.replace('[dot]', '.')
        email = email.replace('[.dot]', '.')

        at_count = email.count('@')

        if at_count != 1:
            less = 'Missing @'
            more = 'There are %d \'@\'s' % at_count
            errors.append(less if at_count < 1 else more)

        after_at = ''
        try:
            after_at = email[email.rindex('@') + 1:]
            if after_at.count('.') < 1:
                errors.append('Missing . after @')
        except Exception:
            pass

        invalid_chars = []
        for ch in after_at:
            if not self.__check_char__(ch):
                invalid_chars.append(ch)
        for ch in invalid_chars:
            errors.append('Invalid character: \'%s\'' % ch)

        try:
            last_dot = after_at.rindex('.')
            last_part = after_at[last_dot + 1:]
            if not (2 <= len(last_part) <= 15):
                text = 'Domain extension must be between 2 and 15 characters long.'
                errors.append(text + ' Found: %d characters.' % len(last_part))
        except Exception:
            pass

        return len(errors) <= 0, errors

    def __check_char__(self, char):
        try:
            if MIN_LOWER_ALPHA <= ord(char) <= MAX_LOWER_ALPHA:
                return True
            elif MIN_UPPER_ALPHA <= ord(char) <= MAX_UPPER_ALPHA:
                return True
            elif MIN_NUM_CODE <= ord(char) <= MAX_NUM_CODE:
                return True
            elif ord(char) == DOT_CODE or ord(char) == UNDERSCORE_CODE or ord(char) == DASH_CODE:
                return True
        except Exception:
            pass
        return False
