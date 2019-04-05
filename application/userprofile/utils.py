from common.models import Qualification, Specialization, Research, Language
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
    elif class_name == 'Research':
        model_class = Research
    elif class_name == 'Language':
        model_class = Language
    elif class_name == 'Organization':
        model_class = Organization.get_organizations

    records = model_class.get_records(records_ids)
    if len(records_ids) != records.count():
        raise Exception('Some records are not valid. Please verify once')

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
    elif class_name == 'Research':
        model_class = Research
    elif class_name == 'Language':
        model_class = Language
    elif class_name == 'Organization':
        model_class = Organization.get_organizations

    return model_class.create_bulk_records(values=values, return_records=True)
