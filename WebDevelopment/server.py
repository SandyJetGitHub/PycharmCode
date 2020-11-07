from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Shubhangi!'


# @app.route('/home')
# def home():
#     return render_template('index.html')


# @app.route('/project')
# def project():
#     return render_template('project.html')

@app.route('/<path:subpath>')
def render_view(subpath):
    return render_template(subpath)


@app.route('/submit_form', methods=['POST', 'GET'])
def send_message():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_data_to_database(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'


def write_data_to_database(enquiry_data):
    with open('./database.txt', mode='a+') as database_file:
        email = enquiry_data['email']
        subject = enquiry_data['subject']
        message = enquiry_data['message']
        database_file.write(f'\nEmail:{email} Subject:{subject} Message:{message}')
