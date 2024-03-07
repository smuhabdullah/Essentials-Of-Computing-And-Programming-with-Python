#  First import flask and redirect, url_for

from flask import Flask, render_template, request

app = Flask(__name__)


from flask import redirect, url_for

   
@app.route('/', methods=['GET', 'POST'])
   # If the request is POST, extracts user input data such as name, pickup and dropoff locations,
   # date, time, and contact number from the submitted form.
def index():
    if request.method == 'POST':
        name = request.form['name']
        pickup_location = request.form['pickup_location']
        dropoff_location = request.form['dropoff_location']
        date = request.form['date']
        time = request.form['time']
        contact_number = request.form['contact_number']

        #  Let's just print the details.
        print(f"Name: {name}, Pickup Location: {pickup_location}, Dropoff Location: {dropoff_location}, Date: {date}, Time: {time}, Contact Number: {contact_number}")

        # Redirect to the confirmation page
        return redirect(url_for('confirmation'))

    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


if __name__ == '__main__':
    app.run(debug=True)
