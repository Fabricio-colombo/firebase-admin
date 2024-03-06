import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

caminho_chave_servico = "E:/DESKTOP_2/firebase-admin/key_firebase/serviceAccountKey.json"
cred = credentials.Certificate(caminho_chave_servico)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-with-python-84d06-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')

data = ref.get()
print("Dados do Firebase:")
print(data)