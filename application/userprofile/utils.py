from common.models import Qualification, Specialization, Research, Language
from organization.models import Organization


def validate_n_get(class_name, records_ids):
    """Factory- validation"""
    if not records_ids:
        return None
    if type(records_ids) != list:
        records_ids = [records_ids]

    model_func = None
    if class_name == 'Qualification':
        model_func = Qualification.get_qualifications
    elif class_name == 'Specialization':
        model_func = Specialization.get_specializations
    elif class_name == 'Research':
        model_func = Research.get_researches
    elif class_name == 'Language':
        model_func = Language.get_languages
    elif class_name == 'Organization':
        model_func = Organization.get_organizations

    records = model_func(records_ids)
    if len(records_ids) != records.count():
        raise Exception('Some records are not valid. Please verify once')

    return records
