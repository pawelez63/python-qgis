from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

def run_script(iface):
        layer = iface.activeLayer()
        layer.startEditing()

        res = layer.dataProvider().addAttributes([QgsField("x", QVariant.Double)])
        res = layer.dataProvider().addAttributes([QgsField("y", QVariant.Double)])
        res = layer.dataProvider().addAttributes([QgsField("z", QVariant.Double)])
        layer.updateFields()
