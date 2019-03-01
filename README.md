# Basic Email Validator (beval)

This is a super simple and/or basic example of an email validator without using external libraries. Just python std functions

## Installation

Run the following command in your terminal:
`pip3 install -U bemval`

## How to use

```python
from bemval.validator import EmailValidator

validator = EmailValidator()
valid, errors = validator.validate('is.this-an@email.com')

print('Is a valid email? -> %s' % ('YES' if valid else 'NO'))
if len(errors) > 0:
    print('Errors:\n- %s' % '\n- '.join(errors))

```