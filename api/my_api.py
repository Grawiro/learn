from flask import Flask
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

STUDENTS = {
    'api': {'name': 'Kamila', 'age': 20, 'spec': 'programmer'},
    '2': {'name': 'Bob', 'age': 22, 'spec': 'UX'},
    '3': {'name': 'Tom', 'age': 21, 'spec': 'tester'},
    '4': {'name': 'Jim', 'age': 20, 'spec': 'engineer'},
}

parser = reqparse.RequestParser()


class StudentsList(Resource):
    @staticmethod
    def get():
        return STUDENTS

    @staticmethod
    def post():
        parser.add_argument('name')
        parser.add_argument('age')
        parser.add_argument('spec')
        args = parser.parse_args()

        student_id = str(int(max(STUDENTS.keys()))+1)
        STUDENTS[student_id] = {
            'name': args['name'],
            'age': args['age'],
            'spec': args['spec'],
        }
        return STUDENTS[student_id], 201


class Student(Resource):
    @staticmethod
    def get(student_id):
        if student_id not in STUDENTS:
            return 'Not found', 404
        else:
            return STUDENTS[student_id]

    @staticmethod
    def put(student_id):
        parser.add_argument('name')
        parser.add_argument('age')
        parser.add_argument('spec')
        args = parser.parse_args()

        if student_id not in STUDENTS:
            return 'Record not found', 404
        else:
            student = STUDENTS[student_id]
            student['name'] = args['name'] if args['name'] is not None else student['name']
            student['age'] = args['age'] if args['age'] is not None else student['age']
            student['spec'] = args['spec'] if args['spec'] is not None else student['spec']
        return STUDENTS[student_id], 200

    @staticmethod
    def delete(student_id):
        if student_id not in STUDENTS:
            return 'Not found', 404
        else:
            del STUDENTS[student_id]
            return '', 204


api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')

if __name__ == "__main__":
    app.run(host='192.168.0.3', debug=True)
