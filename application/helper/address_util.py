from common.models import (Qualification, Specialization, Research, Language, Discipline,
                           RegistrationAuthority, Address, State)


def build_address(data_dict):
    """Create or update address"""

    record_id = data_dict.get('id') and data_dict.pop('id') or None

    try:
        data_dict['state'] = State.objects.get(id=data_dict.get('state'))
    except State.DoesNotExist:
        raise Exception('Given State does not exist in our system')
    obj, created = Address.objects.update_or_create(id=record_id, defaults=data_dict)
    return obj