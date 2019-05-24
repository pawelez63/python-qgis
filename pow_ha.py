# Customize this starter script by adding code
# to the run_script function. See the Help for
# complete information on how to create a script
# and use Script Runner.

""" Your Description of the script goes here """

# Some commonly used imports

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
    layer = iface.activeLayer()
    layer.startEditing()

    res = layer.dataProvider().addAttributes([QgsField(name="pow[ha]", type=QVariant.Double, len=10, prec=4)])
    layer.updateFields()

    expression = QgsExpression("$area / 1000")
    index = layer.fieldNameIndex("pow[ha]")
    expression.prepare(layer.pendingFields())
    layer.startEditing()

    for feature in layer.getFeatures():
        value = expression.evaluate(feature)
        layer.changeAttributeValue(feature.id(), index, value)

    layer.commitChanges()
