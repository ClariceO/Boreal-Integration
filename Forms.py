from wtforms import *
from datetime import date
import shelve
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms.fields import EmailField


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Appointment Booking
class CreateBookingForm(Form):
    name = StringField('', render_kw={"value": "Bob", "disabled": "disabled"})
    contact = IntegerField('', render_kw={"value": "81236458", "disabled": "disabled"})
    email = EmailField('', render_kw={"value": "bob@gmail.com", "disabled": "disabled"})
    hairstylist = SelectField('', choices=[('', '--Please select your hairstylist--'), ('Julie Watson', 'Julie Watson'), ('Marc McKnew', 'Marc McKnew'), ('Jet Atkin', 'Jet Atkin'),('Jose Eber', 'Jose Eber')], default='')
    date = DateField('', default=date.today())
    time = TimeField('')

    # getting checklist from db :)))))

    db = shelve.open('service.db')
    services_dict = db.get('Services')
    services_list = []
    for key in services_dict:
        item = services_dict.get(key)
        service = item.get_service()
        price = item.get_service_price()
        services_list.append(price)
        services_list.append(service)

    choices_list = []
    for i in range(0, len(services_list), 2):
        choices_list.append((services_list[i], services_list[i+1]))
    # print(choices_list)
    db.close()

    services = MultiCheckboxField('', name="service", choices=choices_list, coerce=str)

    remarks = TextAreaField('', [validators.Optional('')])

# Service


class CreateServiceForm(Form):
    service = StringField('', [validators.data_required()])  # Service Type
    description = TextAreaField('', [validators.data_required()])  # Description
    service_price = DecimalField('', [validators.data_required()])  # Price
    service_image = StringField('', [validators.data_required()])  # Image Address


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Submit")


# Ana's
class CreateUserForm(Form):
    first_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    hairstylistname = SelectField('', [validators.DataRequired()], choices=[('', 'Click to select your hairstylist'), ('JW', 'Julie Watson'), ('MM', 'Marc McKnew'), ('JA', "Jet Atkins"),("JE","Jose Eber")],default='')
    date = DateField('Select the date of your appointment :', [validators.DataRequired()])
    file = StringField('', [validators.DataRequired() , ])
    remarks = TextAreaField('', [validators.DataRequired()])


class CreateReviewForm(Form):
    helpful = RadioField('Was our website helpful ?', choices=(("Very helpful","Very helpful"),("Helpful", "Helpful"),("Not helpful","Not helpful")))
    convenience = RadioField("Was our website easy to use ?", choices = (("Very easy","Very Easy"), ("Easy" , "Easy"), ("Not easy","Not Easy")))
    feedback = TextAreaField('Feedback : ',[ validators.data_required()])


# Asykin

class CreateHairstylistForm(Form):
    first_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    hairstylists = SelectField('', [validators.DataRequired()], choices=[('', 'Select Hairstylist'), ('JW', 'Julie Watson'), ('MM', 'Marc McKnew'),('JA', 'Jet Atkin'), ('JE', 'Jose Eber') ], default='')
    email = EmailField('', [validators.Email(), validators.DataRequired()])
    remarks = TextAreaField('', [validators.Optional()])

