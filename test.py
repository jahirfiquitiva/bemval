from bemval.validator import EmailValidator


def main():
    validator = EmailValidator()
    valid, errors = validator.validate('is.this-an@email.com')

    print('Is a valid email? -> %s' % ('YES' if valid else 'NO'))
    if len(errors) > 0:
        print('Errors:\n- %s' % '\n- '.join(errors))


if __name__ == '__main__':
    main()
