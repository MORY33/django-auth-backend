try:
    from secrets import SystemRandom
except ImportError:
    from random import SystemRandom


UNICODE_ASCII_CHARACTER_SET = (
    'abcdefghijklmnopqrstuvwxyz' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' '0123456789'
)


def CustomTokenGenerator(request, length=30, chars=UNICODE_ASCII_CHARACTER_SET):
    """Generates a non-guessable OAuth Json Web Token
    OAuth (1 and 2) does not specify the format of tokens except that they
    should be strings of random characters. Tokens should not be guessable
    and entropy when generating the random characters is important. Which is
    why SystemRandom is used instead of the default random.choice method.
    """
    from django.conf import settings
    from jose import jwt
    from decouple import config
    rand = SystemRandom()
    secret = getattr(settings, 'SECRET_KEY')
    print(secret)
    print("in my custom generate_token")
    token = ''.join(rand.choice(chars) for x in range(length))
    jwtted_token = jwt.encode({'token': token, 'user': str(request.user), 'test': 'testo'}, secret, algorithm='HS256')
    return jwtted_token


