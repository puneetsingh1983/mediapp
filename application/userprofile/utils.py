from common.models import (Qualification, Specialization, Research, Language, Discipline,
                           RegistrationAuthority)
from organization.models import Organization


def validate_n_get(class_name, records_ids):
    """Factory- validation"""
    if not records_ids:
        return None
    if type(records_ids) != list:
        records_ids = [records_ids]

    model_class = None
    if class_name == 'Qualification':
        model_class = Qualification
    elif class_name == 'Specialization':
        model_class = Specialization
    # elif class_name == 'Research':
    #     model_class = Research
    elif class_name == 'Language':
        model_class = Language
    elif class_name == 'Organization':
        model_class = Organization
    elif class_name == 'Discipline':
        model_class = Discipline
    elif class_name == 'RegistrationAuthority':
        model_class = RegistrationAuthority

    records = model_class.get_records(records_ids)
    if len(records_ids) != records.count():
        raise Exception('Some records are not valid for {}. Please verify once'.format(class_name,))

    return records


def bulk_create_get(class_name, values):
    """Factory- validation"""
    if not values:
        return None
    if type(values) != list:
        records_ids = [values]

    model_class = None
    if class_name == 'Qualification':
        model_class = Qualification
    elif class_name == 'Specialization':
        model_class = Specialization
    # elif class_name == 'Research':
    #     model_class = Research
    elif class_name == 'Language':
        model_class = Language
    elif class_name == 'Organization':
        model_class = Organization

    return model_class.create_bulk_records(values=values, return_records=True)


# def build_address(data_dict):
#     record_id = data_dict.pop('id')
#     address, created = Address.objecs.update_or_create(id=record_id, defaults=data_dict)
#         # address_line_1=data_dict.get("address_line_1"),
#         # address_line_2=data_dict.get("address_line_2"),
#         # address_line_3=data_dict.get("address_line_3"),
#         # district=data_dict.get("district"),
#         # city=data_dict.get("city"),
#         # pincode=data_dict.get("pincode"),
#         # state=data_dict.get("state"))
#     return address

def build_doc_dict(reg_certificate, profile_pic, del_reg_certificate, del_profile_pic):
    fields = {}
    if reg_certificate:
        fields['registration_certificate'] = reg_certificate
    if profile_pic:
        fields['profile_pic'] = profile_pic
    if del_reg_certificate:
        fields['registration_certificate'] = None
    if del_profile_pic:
        fields['profile_pic'] = None

    return fields