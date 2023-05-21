from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de contactos (simulada)
contacts = [
    {'id': 1, 'name': 'Juan Garcia', 'phone': '123456789'},
    {'id': 2, 'name': 'Maria Gonzalez', 'phone': '987654321'}
]
next_id = 3

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    global next_id
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        contact = {'id': next_id, 'name': name, 'phone': phone}
        next_id += 1
        contacts.append(contact)
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if contact is None:
        return redirect(url_for('index'))
    if request.method == 'POST':
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        return redirect(url_for('index'))
    return render_template('edit_contact.html', contact=contact)

@app.route('/delete/<int:contact_id>')
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c['id'] != contact_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
