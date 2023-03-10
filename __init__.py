# Clarice's
from flask import *
from Forms import *
import shelve
import Appointment, Service, User, Hairstylist
from werkzeug.utils import secure_filename
import os
from chat import get_response


app = Flask(__name__)
app.secret_key = 'HiImTheKey'
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


@app.route('/')
def home():
    return render_template('home.html')


# Asykin
@app.route('/new')
def contact_hairstylists():
    return render_template('new.html')


@app.route('/chat')
def chat():
    hairstylist_dict = {}
    db = shelve.open('hairstylist.db', 'r')
    hairstylist_dict = db['Hairstylist']
    db.close()

    hairstylist_list = []
    for key in hairstylist_dict:
        hairstylist = hairstylist_dict.get(key)
        hairstylist_list.append(hairstylist)

    return render_template('chat.html',count=len(hairstylist_list), hairstylist_list=hairstylist_list)


@app.route('/chatbot')
def bot():
    return render_template('chatbot.html')


@app.route('/createchat', methods=['GET', 'POST'])
def create_hairstylist():
    create_hairstylist_form = CreateHairstylistForm(request.form)
    if request.method == 'POST' and create_hairstylist_form.validate():
        hairstylist_dict = {}
        db = shelve.open('hairstylist.db', 'c')

        try:
            hairstylist_dict = db['Hairstylist']
        except:
            print("Error in retrieving Hairstylist from hairstylist.db.")

        hairstylist = Hairstylist.Hairstylist(create_hairstylist_form.first_name.data, create_hairstylist_form.last_name.data,
                         create_hairstylist_form.hairstylists.data, create_hairstylist_form.email.data, create_hairstylist_form.remarks.data)
        hairstylist_dict[hairstylist.get_hairstylist_id()] = hairstylist
        db['Hairstylist'] = hairstylist_dict

        db.close()
        return redirect(url_for('chat'))
    return render_template('createchat.html', form=create_hairstylist_form)


@app.route('/retrievechat')
def retrieve_hairstylist():
    hairstylist_dict = {}
    db = shelve.open('hairstylist.db', 'r')
    hairstylist_dict = db['Hairstylist']
    db.close()

    hairstylist_list = []
    for key in hairstylist_dict:
        hairstylist = hairstylist_dict.get(key)
        hairstylist_list.append(hairstylist)

    return render_template('retrievechat.html',count=len(hairstylist_list), hairstylist_list=hairstylist_list)


@app.route('/updatechat/<int:id>/', methods=['GET', 'POST'])
def update_hairstylist(id):
    update_hairstylist_form = CreateHairstylistForm(request.form)
    if request.method == 'POST' and update_hairstylist_form.validate():
        hairstylist_dict = {}
        db = shelve.open('hairstylist.db', 'w')
        hairstylist_dict = db['Hairstylist']
        hairstylist = hairstylist_dict.get(id)
        hairstylist.set_first_name(update_hairstylist_form.first_name.data)
        hairstylist.set_last_name(update_hairstylist_form.last_name.data)
        hairstylist.set_email(update_hairstylist_form.email.data)
        hairstylist.set_hairstylists(update_hairstylist_form.hairstylists.data)
        hairstylist.set_remarks(update_hairstylist_form.remarks.data)
        db['Hairstylist'] = hairstylist_dict
        db.close()

        return redirect(url_for('retrieve_hairstylist'))
    else:
        hairstylist_dict = {}
        db = shelve.open('hairstylist.db', 'r')
        hairstylist_dict = db['Hairstylist']
        db.close()
        hairstylist = hairstylist_dict.get(id)
        update_hairstylist_form.first_name.data = hairstylist.get_first_name()
        update_hairstylist_form.last_name.data = hairstylist.get_last_name()
        update_hairstylist_form.email.data = hairstylist.get_email()
        update_hairstylist_form.hairstylists.data = hairstylist.get_hairstylists()
        update_hairstylist_form.remarks.data = hairstylist.get_remarks()

        return render_template('updatechat.html', form=update_hairstylist_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_hairstylist(id):
    hairstylist_dict = {}
    db = shelve.open('hairstylist.db', 'w')
    hairstylist_dict = db['Hairstylist']
    hairstylist_dict.pop(id)
    db['Hairstylist'] = hairstylist_dict
    db.close()
    return redirect(url_for('retrieve_hairstylist'))


@app.route('/chatbot', methods=['GET'])
def index_get():
    return render_template("chatbot.html")


@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

# Ana's


@app.route('/Review')
def review():
    return render_template('Review.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    form = UploadFileForm()
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,create_user_form.hairstylistname.data, create_user_form.date.data, create_user_form.remarks.data , create_user_form.file.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=form, create_user_form=create_user_form)


@app.route('/websitereview')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('websitereview.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    form = UploadFileForm()
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_hairstylistname(update_user_form.hairstylistname.data)
        user.set_date(update_user_form.date.data)
        user.set_file(update_user_form.file.data)
        user.set_remarks(update_user_form.remarks.data)
        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.hairstylistname.data = user.get_hairstylistname()
        update_user_form.date.data = user.get_date()
        update_user_form.file.data = user.get_file()
        update_user_form.remarks.data = user.get_remarks()
        return render_template('updateUser.html' ,  create_user_form= update_user_form , form = form )


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))


@app.route('/reviewforwebsite' ,methods=["GET",'POST'])
def create_feedback():
    create_feedback_form = CreateReviewForm(request.form)
    if request.method =="POST" and create_feedback_form.validate():
        return redirect(url_for("retrieve_users"))
    return render_template('reviewforwebsite.html', form = create_feedback_form)


# Clarice's
#  Boreal Services :)
@app.route('/createService', methods=['GET',"POST"])
def create_services():
    form = UploadFileForm()
    create_service_form = CreateServiceForm(request.form)

    try:
        db = shelve.open('service.db', 'c')

    except:
        print("Error in retrieving Services from service.db.")

    if request.method == 'POST' and create_service_form.validate():
        services_dict = db['Services']
        id = len(services_dict)
        service = Service.Service(id, create_service_form.service.data, create_service_form.description.data, create_service_form.service_price.data, create_service_form.service_image.data)
        services_dict[id] = service
        db['Services'] = services_dict

        # # Test codes
        # services_dict = db['Services']
        # service = services_dict[service.get_service_id()]
        # print(service.get_service(), service.get_service_price(), "was stored in service.db successfully with service_id ==", service.get_service_id())
        # db.close()

        session['service_created'] = service.get_service()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file

        return redirect(url_for('retrieve_services'))

    return render_template('createService.html', form=form, create_service_form=create_service_form)


@app.route('/retrieveServices')
def retrieve_services():
    services_dict = {}
    db = shelve.open('service.db', 'r')
    services_dict = db['Services']
    db.close()

    services_list = []
    for key in services_dict:
        service = services_dict.get(key)
        services_list.append(service)
    return render_template('retrieveServices.html', count=len(services_list), services_list=services_list)


@app.route('/updateService/<int:_id>/', methods=['GET', 'POST'])
def update_service(_id):
    update_service_form = CreateServiceForm(request.form)
    form = UploadFileForm()

    if request.method == 'POST' and update_service_form.validate():
        services_dict = {}
        db = shelve.open('service.db', 'w')
        services_dict = db['Services']

        service = services_dict.get(_id)
        service.set_description(update_service_form.description.data)
        service.set_service(update_service_form.service.data)
        service.set_service_price(update_service_form.service_price.data)
        service.set_service_image(update_service_form.service_image.data)

        db['Services'] = services_dict
        db.close()
        session['service_updated'] = service.get_service()
        return redirect(url_for('retrieve_services'))
    else:
        services_dict = {}
        db = shelve.open('service.db', 'r')
        services_dict = db['Services']
        db.close()
        service = services_dict.get(_id)
        update_service_form.service.data = service.get_service()
        update_service_form.description.data = service.get_description()
        update_service_form.service_price.data = service.get_service_price()
        update_service_form.service_image.data = service.get_service_image()
        return render_template('updateService.html', form=form, update_service_form=update_service_form)


@app.route('/deleteService/<int:_id>/', methods=['POST'])
def delete_service(_id):
    services_dict = {}
    db = shelve.open('service.db', 'w')
    services_dict = db['Services']
    service = services_dict.pop(_id)
    db['Services'] = services_dict
    db.close()
    session['service_deleted'] = service.get_service()
    return redirect(url_for('retrieve_services'))


# booking appointment


@app.route('/bookingAnAppointment', methods=['GET', 'POST'])
def create_appointment():
    create_appointment_form = CreateBookingForm(request.form)
    services_list = []
    services_dict = {}
    db_services = shelve.open('service.db', 'r')
    services_dict = db_services['Services']
    db_services.close()

    for key in services_dict:
        service = services_dict.get(key)
        services_list.append(service)
    try:
        db = shelve.open('appointment.db', 'c')
        appointments_dict = {}
        appointments_dict = db['Appointments']
        # db_services = shelve.open('service.db', 'r')
        # services_dict = db_services['Services']
        # services_dict = {}
    except:
        print("Error in retrieving Appointments from appointment.db.")
    else:
        if request.method == 'POST':

            appointment = Appointment.Appointment(create_appointment_form.hairstylist.data, create_appointment_form.date.data, create_appointment_form.time.data, create_appointment_form.services.data, create_appointment_form.name.data, create_appointment_form.contact.data, create_appointment_form.email.data, create_appointment_form.remarks.data)
            appointments_dict[appointment.get_appointment_id()] = appointment
            db['Appointments'] = appointments_dict

            # # Test codes
            # appointments_dict = db['Appointments']
            # appointment = appointments_dict[appointment.get_appointment_id()]
            # print("was stored in appointment.db successfully with appointment_id ==", appointment.get_appointment_id())

            db.close()
            session['appointment_created'] = appointment.get_appointment_id()

            return redirect(url_for('retrieve_appointments'))

        return render_template('bookingAnAppointment.html', form=create_appointment_form, services_list=services_list)
    return "Error"


@app.route('/retrieveAppointments')
def retrieve_appointments():
    appointments_dict = {}
    db = shelve.open('appointment.db', 'r')
    appointments_dict = db['Appointments']
    db.close()

    appointments_list = []
    for key in appointments_dict:
        appointment = appointments_dict.get(key)
        appointments_list.append(appointment)

    return render_template('retrieveAppointments.html', count=len(appointments_list), appointments_list=appointments_list)


@app.route('/updateAppointment/<int:_id>/', methods=['GET', 'POST'])
def update_appointment(_id):
    update_appointment_form = CreateBookingForm(request.form)
    services_list = []
    services_dict = {}
    db_services = shelve.open('service.db', 'r')
    services_dict = db_services['Services']
    db_services.close()

    for key in services_dict:
        service = services_dict.get(key)
        services_list.append(service)

    if request.method == 'POST':
        appointments_dict = {}
        db = shelve.open('appointment.db', 'w')
        appointments_dict = db['Appointments']

        appointment = appointments_dict.get(_id)
        appointment.set_hairstylist(update_appointment_form.hairstylist.data)
        appointment.set_date(update_appointment_form.date.data)
        appointment.set_time(update_appointment_form.time.data)
        appointment.set_services(update_appointment_form.services.data)
        appointment.set_name(update_appointment_form.name.data)
        appointment.set_contact(update_appointment_form.contact.data)
        appointment.set_email(update_appointment_form.email.data)
        appointment.set_remarks(update_appointment_form.remarks.data)

        db['Appointments'] = appointments_dict
        session['appointment_updated'] = appointment.get_appointment_id()
        db.close()


        return redirect(url_for('retrieve_appointments'))
    else:
        appointments_dict = {}
        db = shelve.open('appointment.db', 'r')
        appointments_dict = db['Appointments']
        db.close()

        appointment = appointments_dict.get(_id)
        update_appointment_form.hairstylist.data = appointment.get_hairstylist()
        update_appointment_form.date.data = appointment.get_date()
        update_appointment_form.time.data = appointment.get_time()
        update_appointment_form.services.data = appointment.get_services()
        update_appointment_form.name.data = appointment.get_name()
        update_appointment_form.contact.data = appointment.get_contact()
        update_appointment_form.email.data = appointment.get_email()
        update_appointment_form.remarks.data = appointment.get_remarks()

        return render_template('updateAppointment.html', services_list=services_list, form=update_appointment_form)


@app.route('/deleteAppointment/<int:_id>/', methods=['POST'])
def delete_appointment(_id):
    appointments_dict = {}
    db = shelve.open('appointment.db', 'w')
    appointments_dict = db['Appointments']
    appointment = appointments_dict.pop(_id)
    db['Appointments'] = appointments_dict
    db.close()
    session['appointment_deleted'] = appointment.get_appointment_id()
    return redirect(url_for('retrieve_appointments'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run()
