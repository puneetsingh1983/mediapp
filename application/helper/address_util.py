from common.models import (Qualification, Specialization, Research, Language, Discipline,
                           RegistrationAuthority, Address)


def build_address(data_dict):
    """Create or update address"""

    record_id = data_dict.get('id') and data_dict.pop('id') or None
    if data_dict.get('state'):
        data_dict['state_id'] = data_dict.get('state') and data_dict.pop('state') or None

    obj, created = Address.objects.update_or_create(id=record_id, defaults=data_dict)
    return obj