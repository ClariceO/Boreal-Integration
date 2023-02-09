from wtforms import Form, StringField, SelectField, DecimalField, TextAreaField, IntegerField, EmailField, DateField, TimeField, validators
from wtforms import widgets, SelectMultipleField
from datetime import date
import shelve

# Ana's
from wtforms import FileField


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Appointment Booking
class CreateBookingForm(Form):
    name = StringField('', render_kw={"value": "Bob", "disabled": "disabled"})
    contact = IntegerField('', render_kw={"value": "81236458", "disabled": "disabled"})
    email = EmailField('', render_kw={"value": "bob@gmail.com", "disabled": "disabled"})
    hairstylist = SelectField('', choices=[('', '--Please select your hairstylist--'), ('Mark Chan', 'Mark Chan'), ('Harry Cheong', 'Harry Cheong'), ('Candy Loh', 'Candy Loh'),('Ray Tan', 'Ray Tan')], default='')
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

    services = MultiCheckboxField('', name="service", choices=choices_list, coerce=int)

    remarks = TextAreaField('', [validators.Optional('')])

# Service


class CreateServiceForm(Form):
    service = StringField('', [validators.data_required()])  # Service Type
    description = TextAreaField('', [validators.data_required()])  # Description
    service_price = DecimalField('', [validators.data_required()])  # Price
    service_image = StringField('', [validators.data_required()])  # Image Address


# Ana's
class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Name of hairstylist', [validators.DataRequired()], choices=[('', 'Select'), ('A', 'AAA'), ('B', 'BBB'), ('C', "CCC"),("D","DDD")],default='')
    date = DateField('Select the date of your appointment', [validators.DataRequired()])
    file = FileField('Upload a photo', [validators.Optional()])
    remarks = TextAreaField('Remarks', [validators.DataRequired()])


