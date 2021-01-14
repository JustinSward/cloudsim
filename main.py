from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from operator import itemgetter, attrgetter

app = Flask(__name__)


# Definition of the Part class
# @param partType The type of part (0=VDC, 1=VAC, 2=Resistor, 3=Capacitor,4=Inductor)
# @param partId The instance of the part within that type
# @param partValue The absolute value in base units (Ohms, Farads, Henries) of the part
# @param node1 The numerical value of the positive or first node the part is connected
# @param node2 The numerical value of the negative or second node the part is connected
class Part:
    number_of_parts = 0 # Keeps track of the number of parts

    def __init__(self, partType, partId,partValue, node1, node2):
        self.partType = partType
        self.partId = partId    #TYPE CAST TO int() if needed!
        self.partValue = partValue
        self.node1 = node1
        self.node2 = node2
        Part.number_of_parts += 1

    def getType(self):
        return self.partType

    def getId(self):
        return self.partId
    
    def getValue(self):
        return self.partValue

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    def getUnits(self):
        if self.partType == "V":
            return "Volts"
        elif self.partType == "R":
            return "Ohms"
        elif self.partType == "C":
            return "Farads"
        elif self.partType == "L":
            return "Henry"
    
    def getPartName(self):
        return str(self.partType) + str(self.partId)

    def deletePart(self):   # NEEDS TO BE COMPLETED!! (find index of part, remove part from parts_name_list, etc)
        Part.number_of_parts -= 1
        return True


class Simulation:
    def __init__(self, simtype, simnode, simstartfreq, simendfreq):
        self.simtype = simtype
        self.simnode = simnode
        self.simstartfreq = simstartfreq
        self.simendfreq = simendfreq

    def getType(self):
        if self.simtype == "1":
            return "Voltage Reading"
        elif self.simtype == "2":
            return "Time Domain Analysis"
        elif self.simtype == "3":
            return "Frequency Domain Analysis"
        else:
            return "Something went wrong!"

    def getNode(self):
        return str(self.simnode)
    
    def getStart(self):
        return str(self.simstartfreq)
    
    def getEnd(self):
        return str(self.simendfreq)




@app.route('/', methods=['POST', 'GET'])
def index():
    partAdded = False
    if request.method == 'POST':    # If new part added, read in the parameters and create the new Part object
        form_type = request.form['ptype']
        form_ident = request.form['pident']
        form_value = request.form['pvalue']
        form_node1 = request.form['pnode1']
        form_node2 = request.form['pnode2']
        # NEED TO CHECK IF PART NAME IS USED ALREADY --> IF NOT, DO NOT ADD!!
        part_array.append(Part(form_type, form_ident, form_value, form_node1, form_node2))  # Create the new part and append to the list
        part_array.sort(key=attrgetter('partType','partId'))    # Keep the parts list sorted
        partAdded = True    # Part successfully added to the net list

    # # # REMOVE THIS LATER # # #
    print(Part.number_of_parts) # Prints the number of parts to the console (not to the HTML page)
    print(partAdded)

    for part in part_array:
        print(part.getPartName())
    
    # # # # # # # # # # # # # # #

    return render_template('index.html', PartHTML = Part, part_arrayHTML = part_array, simHTML = sim, partAddedH = partAdded)




@app.route('/run', methods=['POST', 'GET'])
def run():
    if request.method == 'POST':
        sim.simtype = request.form['simtype']
        sim.simnode = request.form['simnode']
        sim.simstartfreq = request.form['simstartfreq']
        sim.simendfreq = request.form['simendfreq']
    return render_template('run.html', simHTML = sim)



@app.route('/clear')
def clearList():
    part_array.clear()
    Part.number_of_parts = 0
    Part.part_names_list.clear()
    return redirect('/')


@app.route('/undo') # BROKEN CURRENTLY -- REMOVES THE WRONG COMPONENT !!!!!!!!!!!!!!!!!!!
def undoAdd():
    Part.part_names_list.pop()
    part_array.pop()
    Part.number_of_parts -= 1
    return redirect('/')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/instructions')
def instructions():
    return render_template('instructions.html')



if __name__ == "__main__":
    part_array = []             # Establish the list holding the parts
    part_names_list = []        # Keeps track of all the part names
    sim = Simulation("0",0,0,0) # Keeps track of the simulation settings
    app.run(debug=True)