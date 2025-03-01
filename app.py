from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos (Docker Compose usa el nombre del servicio "db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:password@db:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para la tabla de estudiantes
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    carrera = db.Column(db.String(100), nullable=False)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "nombre": s.nombre, "edad": s.edad, "carrera": s.carrera} for s in students])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(nombre=data['nombre'], edad=data['edad'], carrera=data['carrera'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Estudiante agregado"}), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Estudiante no encontrado"}), 404
    
    data = request.get_json()
    student.nombre = data.get('nombre', student.nombre)
    student.edad = data.get('edad', student.edad)
    student.carrera = data.get('carrera', student.carrera)
    
    db.session.commit()
    return jsonify({"message": "Estudiante actualizado"}), 200

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Estudiante no encontrado"}), 404
    
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Estudiante eliminado"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
