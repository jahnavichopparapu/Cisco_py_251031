from flask import Flask, request, jsonify
application=Flask(__name__)

employee=[
    {'id':101,'name':'jahnavi'},
    {'id':102,'name':'sha'}
          ]

@application.route('/employee',methods=['GET'])
def read_all_employee():
    return jsonify(employee)

@application.route('/employee/<emp_id>',methods=['GET'])
def read_all_employee_id(emp_id):
    emp_id=int(emp_id)
    queried_emp=None
    for emp in employee:
        if emp['id']==emp_id:
            queried_emp=emp
            break
    return jsonify(queried_emp)

application.run(debug=True)
