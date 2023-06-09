# Importing the Flask class
from flask import Flask,request
# Importing the json module for JSON serialization
import json
# Importing the dbhelper module
import dbhelper

# Creating a Flask application instance
app=Flask(__name__)

# Item table with (GET/POST/PATCH/DELET) requests
# GET REQUEST
# Added Route decorator for handling GET requests to the  '/api/item' endpoint getting all items
@app.get('/api/item')
#  Created  GET request handler function that handles the GET data sent from client
def get_all_items():
     # Call the 'get_all_items()' procedure from the 'dbhelper' module and store the result in a variable
    results = dbhelper.run_procedure('CAll get_all_items()',[])
    # Checking if the results are of type list
    if(type(results)==list):
    # And if so convert the 'results' list to a JSON string using json.dumps function
        item_json= json.dumps(results,default=str)
    # Return the animals JSON string
        return item_json
    # Else return an error message
    else:
        return 'sorry please try again'

# POST REQUEST
# Added Route decorator for handling POST requests to the  '/api/item' endpoint to add data
@app.post('/api/item')
#  Created   POST request handler function that handles the POST data sent from client
def post_new_item():
    name=request.json.get('name') # Get item name from request data and storing it in a variable name
    description=request.json.get('description')  # Get item description from request data and storing it in a variable description
    price=request.json.get('price') # Get item price from request data and storing it in a variable name price
    # Call the create_new_item() procedure from the 'dbhelper' module and store the result in a variable
    results = dbhelper.run_procedure('CAll create_new_item(?,?,?)',[name,description,price])
    # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string using json.dumps function
        item_json= json.dumps(results,default=str)
        # Return the animals JSON string
        return item_json
        # Else return an error message
    else:
        return 'sorry please try again'
    
# PATCH REQUEST
# Added Route decorator for handling PATCH requests to the  '/api/item' endpoint  to update data
@app.patch('/api/item')
#  Created  PATCH request handler function that handles the data that needs to be added to update data sent by client
def patch_new_item():
    id=request.json.get("id") #Get item id from request data and storing it in a variable name id
    new_price=request.json.get('price') #Get new item price from request data and storing it in a variable new_price
    results = dbhelper.run_procedure('CAll create_new_price(?,?)',[id,new_price])
       # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string using json.dumps function
            item_json= json.dumps(results,default=str)
        # Return the animals JSON string
            return item_json
        # Else return an error message
    else:
        return 'sorry please try again'
    
# DELETE REQUEST
# Added Route decorator for handling DELETE requests to the  '/api/item' endpoint  to delete data
@app.delete('/api/item')
#  Created  DELETE request handler function that handles the data that needs to be deleted sent from client
def delete_item():

    id=request.json.get("id") # Get item id from request and staore it in a variable id
    # Call stored procedure to delete item  and sore the results in a variable results
    results = dbhelper.run_procedure('CAll delete_item_id(?)',[id])
    # if the results [] empty list which means we dont have the id anymore in our db,
    #  and if so return the success message if not the try again message
    if(results==[]):
        return 'Item deleted successfully'
    else:
        return 'sorry please try again' 
    
# Employee table with (GET/POST/PATCH/DELET) requests

# GET REQUEST
# Added Route decorator for handling GET requests to the  '/api/employee' endpoint to get the employee with the given id
@app.get('/api/employee')
#  Created  GET request handler function that handles the GET data sent from client
def get_all_employee():
    id=request.args.get('id') #Get  employee id from request data and storing it in a variable name id
    # Call stored procedure  get_employee with a id value and sore the results in a variable results
    results = dbhelper.run_procedure('CAll get_employee(?)',[id])
    # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string using json.dumps function
            item_json= json.dumps(results,default=str)
        # Return the animals JSON string
            return item_json
        # Else return an error message
    else:
        return 'sorry please try again'

# POST REQUEST
# Added Route decorator for handling POST requests to the  '/api/employee' endpoint to add data
@app.post('/api/employee')
#  Created   POST request handler function that handles the POST data sent from client
def post_new_employee():
    name=request.json.get('name') #Get employee name from request data and storing it in a variable name name
    position=request.json.get('position')#Get employee position from request data and storing it in a variable name position
    hourly_wage=request.json.get('hourly_wage')#Get employee hourly_wage from request data and storing it in a variable name hourly_wage
    # Call stored procedure  add_new_employee with a name,position and hourly_wage  value and sore the results in a variable results
    results = dbhelper.run_procedure('CAll add_new_employee(?,?,?)',[name,position,hourly_wage])
      # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string using json.dumps function
            item_json= json.dumps(results,default=str)
        # Return the animals JSON string
            return item_json
        # Else return an error message
    else:
        return 'sorry please try again'
# POST REQUEST
# Added Route decorator for handling PATCH requests to the  '/api/employee' endpoint to add data
@app.patch('/api/employee')
#  Created   PATCH request handler function that handles the POST data sent from client
def patch_hourly_wage():
    id=request.json.get("id") #Get employee id from request data and storing it in a variable name id
    new_wage_num=request.json.get('hourly_wage')#Get employee new_wage from request data and storing it in a variable new_wage
        # Call stored procedure  update_hourly_wage with id and new_hourly_wage  value and sore the results in a variable results
    results = dbhelper.run_procedure('CAll update_hourly_wage(?,?)',[id,new_wage_num])
    # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string using json.dumps function
            item_json= json.dumps(results,default=str)
        # Return the animals JSON string
            return item_json
        # Else return an error message
    else:
        return 'sorry please try again'
    
# DELETE REQUEST
# Added Route decorator for handling DELETE requests to the  '/api/employee' endpoint  to delete data
@app.delete('/api/employee')
#  Created  DELETE request handler function that handles the data that needs to be deleted sent from client
def delete_employee():
    id=request.json.get("id")  # Get item id from request and staore it in a variable id
    # Call stored procedure to delete employee  and sore the results in a variable results
    results = dbhelper.run_procedure('CAll delete_employee_id(?)',[id])
    #Checking if the results [] empty list which means we dont have the id anymore in our db,
    #  and if so return the success message if not the try again message
    if(results==[]):
        return 'employee data deleted successfully'
    else:
        return 'sorry please try again' 
app.run(debug=True) 
