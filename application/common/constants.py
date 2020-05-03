# Gender
GENDER = (('-', ' -- '),
          ('M', 'Male'),
          ('F', 'Female'),
          ('O', 'Other'))


# Availability mode
MODE_1 = 'online'
MODE_2 = 'offline'
MODE_3 = 'out_door'


AVAILABILITY_MODE = ((MODE_1, 'Online'),
                     (MODE_2, 'Offline'),
                     (MODE_3, 'Out Door'))

# Identity Types
AADHAAR_CARD = 'uid'
PASSPORT = 'pp'
DRIVING_LICENSE = 'dl'
VOTER_ID_CARD = 'vid'
PAN_CARD = 'pan'
COMPANY_ID_CARD = 'cid'


ID_CARD_TYPE = (('', ' -- '),
                (AADHAAR_CARD, 'Aadhaar Card (UID)'),
                (COMPANY_ID_CARD, 'Company ID Card'),
                (DRIVING_LICENSE, 'Driving License'),
                (PAN_CARD, 'Pan Card'),
                (PASSPORT, 'Passport'),
                (VOTER_ID_CARD, 'Voter ID Card '))


# Relationships
SELF, FATHER, MOTHER, SPOUSE, CHILD, OTHER = 'se', 'fa', 'mo', 'sp', 'ch', 'ot'
RELATIONSHIP = (('', ' -- '),
                (SELF, 'Self'),
                (FATHER, 'Father'),
                (MOTHER, 'Mother'),
                (SPOUSE, 'Spouse'),
                (CHILD, 'Child'),
                (OTHER, 'Other'))