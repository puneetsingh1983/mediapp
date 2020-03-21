import time

from django_otp.oath import TOTP
from django_otp.util import random_hex

from django.conf import settings


class TOTPVerification(object):

    TOTP_KEY = random_hex(20)
    LAST_VERIFIED_COUNTER = -1
    VERIFIED = False
    NO_OF_DIGITS = 6
    TOKEN_VALIDITY_PERIOD = 120 # valid for 2 mins

    def __init__(self):
        # secret key that will be used to generate a token,
        # User can provide a custom value to the key.
        self.key = self.TOTP_KEY
        # counter with which last token was verified.
        # Next token must be generated at a higher counter value.
        self.last_verified_counter = self.LAST_VERIFIED_COUNTER
        # this value will return True, if a token has been successfully
        # verified.
        self.verified = self.VERIFIED
        # number of digits in a token. Default is 6
        self.number_of_digits = self.NO_OF_DIGITS
        # validity period of a token. Default is 30 second.
        self.token_validity_period = self.TOKEN_VALIDITY_PERIOD

    def totp_obj(self):
        # create a TOTP object
        totp = TOTP(key=self.key,
                    step=self.token_validity_period,
                    digits=self.number_of_digits)
        # the current time will be used to generate a counter
        totp.time = time.time()
        return totp

    def generate_token(self):
        # get the TOTP object and use that to create token
        totp = self.totp_obj()
        # token can be obtained with `totp.token()`
        token = str(totp.token()).zfill(6)
        return token

    def verify_token(self, token, tolerance=0):
        try:
            # convert the input token to integer
            token = int(token)
        except ValueError:
            # return False, if token could not be converted to an integer
            self.verified = False
        else:
            totp = self.totp_obj()
            # check if the current counter value is higher than the value of
            # last verified counter and check if entered token is correct by
            # calling totp.verify_token()
            if ((totp.t() > self.last_verified_counter) and
                    (totp.verify(token, tolerance=tolerance))):
                # if the condition is true, set the last verified counter value
                # to current counter value, and return True
                self.last_verified_counter = totp.t()
                self.verified = True
            else:
                # if the token entered was invalid or if the counter value
                # was less than last verified counter, then return False
                self.verified = False
        return self.verified


if __name__ == '__main__':
    phone1 = TOTPVerification()
    generated_token = phone1.generate_token()
    print("Generated token is: ", generated_token)
    token = int(input("Enter token: "))
    phone2 = TOTPVerification()

    print(phone2.verify_token(token))
