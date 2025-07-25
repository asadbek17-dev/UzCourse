from rest_framework import serializers

#=========== const variables =========
MIN_LEN_PASSWORD = 8
#=====================================


def validate_serilizers_data(attrs):

    username = attrs.get('username')
    email = attrs.get('email')
    first_name = attrs.get('first_name')
    last_name = attrs.get('last_name')
    password = attrs.get('password')
    confirm_password = attrs.get('confirm_password')

    if not username:
        return 'Username maydonini kiritish majburiy'
    if not email:
        return 'Email maydonini kiritish majburiy'
    if not first_name:
        return 'Ismingiz maydonini kiritish majburiy'
    if not last_name:
        return 'Familyangiz maydonini kiritish majburiy'
    if not password:
        return 'Parol maydonini kiritish majburiy'
    if not confirm_password:
        return 'Parol tasdig`i maydonini kiritish majburiy'

    if len(str(password).replace(" ","")) < MIN_LEN_PASSWORD:
        return 'Parol kamida 8 ta belgidan iborat bo`lishi kerak '
    else:
        if str(password) != str(confirm_password):
            return 'Parol tasdiqlanmadi, parolni to`g`ri kiriting'
        
    return 'Test Ok'