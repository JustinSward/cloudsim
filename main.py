from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)


# Definition of the Part class
# @param partType The type of part (0=VDC, 1=VAC, 2=Resistor, 3=Capacitor,4=Inductor)
# @param partId The instance of the part within that type
# @param partValue The absolute value in base units (Ohms, Farads, Henries) of the part
# @param node1 The numerical value of the positive or first node the part is connected
# @param node2 The numerical value of the negative or second node the part is connected
class Part:
    number_of_parts = 0 # Keeps track of the number of parts
    part_names_list = [] # Keeps track of all the part names

    def __init__(self, partType, partId,partValue, node1, node2):
        self.partType = partType
        self.partId = partId
        self.partName = str(self.partType) + str(self.partId)
        self.partValue = partValue
        self.node1 = node1
        self.node2 = node2
        Part.number_of_parts += 1
        Part.part_names_list.append(self.partName)

    def returnType(self):
        return self.partType

    def returnId(self):
        return self.partId
    
    def returnValue(self):
        return self.partValue

    def returnNode1(self):
        return self.node1

    def returnNode2(self):
        return self.node2



@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'POST':    # If new part added, read in the parameters and create the new Part object
            form_type = request.form['ptype']
            form_ident = request.form['pident']
            form_value = request.form['pvalue']
            form_node1 = request.form['pnode1']
            form_node2 = request.form['pnode2']
            part_array.append(Part(form_type, form_ident, form_value, form_node1, form_node2))  # Create the new part and append to the list


        #part_array.append(Part("R",32,4700,1,0))
        print(Part.number_of_parts) # Prints the number of parts to the console (not to the HTML page)
        
        #numParts = Part.number_of_parts # 
        return render_template('index.html', PartHTML = Part, part_arrayHTML = part_array)    # NEED TO INCLUDE VARS HERE (I think)







if __name__ == "__main__":
    part_array = []         # Establish the list holding the parts
    app.run(debug=True)