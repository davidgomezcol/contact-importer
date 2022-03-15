# Franchise prefixes and length

VISA = [
    {'length': [16], 'prefixes': ['4']}
]
MASTERCARD = [
    {'length': [16], 'prefixes': ['51', '52', '53', '54', '55']}
]

AMEX = [
    {'length': [15], 'prefixes': ['34', '37']}
]

DINERS = [
    {'length': [14], 'prefixes': ['300', '301', '302', '303', '304', '305', '36']},
]

# There are Diners Club (North America) cards that begin with 5.
# These are a joint venture between Diners Club and MasterCard,
# and are processed like a MasterCard

DINERS_US = [
    {'length': [16], 'prefixes': ['54', '55']}
]

DISCOVER = [
    {'length': [16], 'prefixes': ['6011', '622126', '622127', '622128', '622129', '62213',
                                  '62214', '62215', '62216', '62217', '62218', '62219',
                                  '6222', '6223', '6224', '6225', '6226', '6227', '6228',
                                  '62290', '62291', '622920', '622921', '622922', '622923',
                                  '622924', '622925', '644', '645', '646', '647', '648',
                                  '649', '65']}
]

JCB = [
    {'length': [16], 'prefixes': ['3528', '3529', '353', '354', '355', '356', '357', '358']}
]
