from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Regexp
from wtforms import TextAreaField


# Define a custom validator for phone numbers that match "+17066641258"
class PhoneNumberValidator(Regexp):

    def __init__(self):
        super().__init__(
            # The regular expression to match phone numbers
            r'^\+[1-9]\d{10}$',
            # The error message to display if the phone number is invalid
            message=
            'The phone number must be in the format +######### with the country code included'
        )


class InteractionForm(FlaskForm):
    recipient_name = StringField('Recipient Name', validators=[DataRequired()])
    recipient_information = TextAreaField('Recipient Information',
                                      validators=[DataRequired()])
    recipient_phone_number = StringField('Phone Number',
                                     validators=[PhoneNumberValidator()])
    campaign_name = StringField('Campaign Name', validators=[DataRequired()])
    campaign_information = TextAreaField('Campaign Information',
                                     validators=[DataRequired()])
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    sender_information = TextAreaField('Sender Information',
                                          validators=[DataRequired()])
    campaign_end_date = DateField('End Date', validators=[DataRequired()])
    interaction_type = SelectField('Interaction Type',
                                     choices=[('call', 'Call'),
                                              ('text', 'Text'),
                                              ('plan', 'Plan')])
    submit = SubmitField('Submit')