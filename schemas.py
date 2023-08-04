from marshmallow import Schema, fields


class olevelSchema(Schema):
    candidate_name = fields.Str(required=True)
    candidate_number = fields.Str(required=True)
    year = fields.Int(required=True)
    random_code = fields.Int(required=True)
    subject_code = fields.Str(required=True)


class alevelSchema(Schema):
    candidate_name = fields.Str(required=True)
    candidate_number = fields.Str(required=True)
    year = fields.Int(required=True)
    random_code = fields.Int(required=True)
    subject_code = fields.Str(required=True)
