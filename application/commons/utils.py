# -*- coding: utf-8 -*-
import re


def is_valid_mobile(mobile_no):
    """validate given mobile number"""

    if type(mobile_no) != str:  # convert to string
        mobile_no = str(mobile_no)
    if re.match("\d{10}$", mobile_no):
        return True
    else:
        return False


def is_valid_token(token):
    """validate given mobile number"""

    if type(token) != str:  # convert to string
        token = str(token)
    if re.match("\d{6}$", token):
        return True
    else:
        return False
