'''
Python Firebase Course for
Beginners
https://codeloop.org/python-firebase-course-for-beginners/
'''
import pyrebase

# Cofiguración específica para el Firebase
config = {
"apiKey": "AIzaSyCkZtABLrWDkAvyqf8IRr5s3kIwp724vXo",
"authDomain": "corintios-5023e.firebaseapp.com",
"databaseURL": "https://corintios-5023e-default-rtdb.firebaseio.com/",
"projectId": "corintios-5023e",
"storageBucket": "corintios-5023e.appspot.com",
"messagingSenderId": "65486733713",
"appId": "1:65486733713:web:cbe0776a0cf8fadefbda30",
"measurementId": "G-SBB7DD27KG"
}

firebase = pyrebase.initialize_app(config)
#Accediendo a la base de datos de Firebase
db = firebase.database()
# Declarar a la base de datos de firebase como "db"


# Leer los atributos de los elementos

# Obtener todos los datos de la aplicación
all_users = db.child("app_inventor").get()
i = 0
# Imprimir cada uno de los datos
# Si el index del dato es 4, no imprimirlo y guardar su valor en "num"
# Este es el dato del número
for users in all_users.each():
    if (i == 4):
        break
    print(users.val())
    i = i + 1
num = int(users.val())

# Imprimir el valor del número (num)
print("Valor de Número: ")
print(num)

# Si el número es mayor a 9, se actualiza la aplicación para mencionarlo.
if (num > 9):
    db.child("app_inventor").update({"Usuario":"Elemento mayor a 9"})
    print("Actualizado")
else:
    print("No Actualizado")
