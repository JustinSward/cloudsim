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
        return render_template('index.html')







if __name__ == "__main__":
    app.run(debug=True)