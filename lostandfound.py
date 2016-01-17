from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
lostEntries = []
foundEntries = []

class Entry(object):
	def __init__(self, itemname, description, zone, email):
		self.itemname = itemname
		self.description = description
		self.zone = zone
		self.email = email

class Zone(object):
	def __init__(self, state, city, zipcode):
		self.state = state
		self.city = city
		self.zip = zipcode

@app.route('/')
@app.route('/lost')
def lost():
	return render_template('losthome.html', lostEntries = lostEntries)

@app.route('/found')
def found():
	return render_template('foundhome.html', foundEntries = foundEntries)

@app.route('/lostfilter', methods = ["POST"])
def lostFilter():
	global lostEntries
	filtered = []
	for i in lostEntries:
		if request.form.get("zip") == '' or request.form.get("zip") == i.zone.zip:
			if request.form.get("city") == '' or request.form.get("city") == i.zone.city:
				if request.form.get("state") == '' or request.form.get("state") == i.zone.state:
					filtered.append(i)
	return render_template('lostfilter.html', lostEntries = filtered)

@app.route('/foundfilter', methods = ["POST"])
def foundFilter():
	global foundEntries
	filtered = []
	for i in foundEntries:
		if request.form.get("zip") == '' or request.form.get("zip") == i.zone.zip:
			if request.form.get("city") == '' or request.form.get("city") == i.zone.city:
				if request.form.get("state") == '' or request.form.get("state") == i.zone.state:
					filtered.append(i)
	return render_template('foundfilter.html', foundEntries = filtered)

@app.route('/lostentry')
def lostEntry():
	return render_template('lostentry.html')

@app.route('/foundentry')
def foundEntry():
	return render_template('foundentry.html')

@app.route('/lostentrysubmission', methods = ["POST"])
def lostEntrySubmission():
	zone = Zone(request.form.get("state"), request.form.get("city"), request.form.get("zip"))
	new = Entry(request.form.get("itemname"), request.form.get("description"), zone, request.form.get("email"))
	global lostEntries
	lostEntries.append(new)
	return render_template('lostentrysubmission.html')

@app.route('/foundentrysubmission', methods = ["POST"])
def foundEntrySubmission():
	zone = Zone(request.form.get("state"), request.form.get("city"), request.form.get("zip"))
	new = Entry(request.form.get("itemname"), request.form.get("description"), zone, request.form.get("email"))
	global foundEntries
	foundEntries.append(new)
	return render_template('foundentrysubmission.html')

@app.route('/reply')
def reply():
	return render_template('email.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug = True)