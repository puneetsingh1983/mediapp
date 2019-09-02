from common.models import (Qualification, Specialization, Research, Language, Discipline,
                           RegistrationAuthority, Address, State)
from helper.exception_response_handlers import DoesNotExistInSystemException


def get_state(value):
    try:
        return State.objects.get(id=value)
    except State.DoesNotExist:
        raise DoesNotExistInSystemException('State', value)


def build_address(data_dict):
    """Create or update address"""

    record_id = data_dict.get('id') and data_dict.pop('id') or None
    data_dict['state'] = get_state(data_dict.get('state'))
    obj, created = Address.objects.update_or_create(id=record_id, defaults=data_dict)
    return obj