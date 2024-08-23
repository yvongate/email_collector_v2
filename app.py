from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)
app.secret_key = 'd198addc927b128dded42d37a58bf10f'

# Échapper le mot de passe pour l'URI MongoDB
username = quote_plus("kouahoyvonmail")
password = quote_plus("nXMirgQKEWtsYPqW")

# Configuration de la connexion à MongoDB
uri = f"mongodb+srv://{username}:{password}@mailuser.ib3td.mongodb.net/?retryWrites=true&w=majority&appName=mailuser"
client = MongoClient(uri)
db = client['mailuser']  # Nom de la base de données
emails_collection = db['emails']  # Nom de la collection

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        
        if email:
            emails_collection.insert_one({'email': email})
            flash('Merci de vous être inscrit !')
            return redirect(url_for('index'))
        else:
            flash('Veuillez entrer une adresse e-mail valide.')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
