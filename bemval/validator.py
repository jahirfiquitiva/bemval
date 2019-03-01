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

    def validate(self, email):
        errors = []
        at_count = email.count('@')

        if at_count != 1:
            less = 'Falta el @'
            more = 'Hay %d \'@\'s' % at_count
            errors.append(less if at_count < 1 else more)

        portions = []
        try:
            portions = email.split('@')
            if portions[1].count('.') < 1:
                errors.append('Falta el . después del @')
        except Exception:
            pass

        invalid_chars = []
        for ch in ''.join(portions):
            if not self.__check_char__(ch):
                invalid_chars.append(ch)
        for ch in invalid_chars:
            errors.append('Caracter inválido: \'%s\'' % ch)

        try:
            last_dot = portions[1].rindex('.')
            last_part = portions[1][last_dot + 1:]
            if not (2 <= len(last_part) <= 15):
                text = 'La extensión de dominio debe tener entre 2 y 15 caracteres.'
                errors.append(text + ' Se encontraron: %d' % len(last_part))
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
