#!/usr/bin/env python

#############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

from taurus.external.qt import QtGui

class PlotLegendTool(QtGui.QAction):

    def __init__(self, parent=None):
        QtGui.QAction.__init__(self, 'Show/hide legend', parent)
        self.triggered.connect(self.onTriggered)
        self._legend = None
        self._legendIsEnable = None

    def attachToPlotItem(self, plotItem, parentWidget=None):

        self._legend = plotItem.addLegend()
        self._legendIsEnable = True

        menu = plotItem.getViewBox().menu
        menu.addAction(self)
        self.setParent(parentWidget or menu)


    def onTriggered(self):
        if self._legendIsEnable:
            self._legend.hide()
            self._legendIsEnable = False
        else:
            self._legend.show()
            self._legendIsEnable = True