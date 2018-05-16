from IPython.core.display import HTML
from IPython.core.display import display

import numpy as np
import os
import copy
import pyqtgraph as pg
from skimage import transform

try:
    from PyQt4.QtGui import QFileDialog
    from PyQt4 import QtCore, QtGui, QtWidgets
    from PyQt4.QtGui import QMainWindow, QDialog
except ImportError:
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

from __code.color import  Color
from __code.file_handler import retrieve_time_stamp, make_ascii_file
from __code.ui_profile import Ui_MainWindow as UiMainWindow
from __code.decorators import wait_cursor


class ProfileUi(QMainWindow):

    data_dict = {}
    data_dict_raw = {}
    timestamp_dict = {}

    rotation_angle = 0
    histogram_level = []

    # size of tables
    _width = 65
    guide_table_width = [80, _width, _width, _width, _width]
    guide_table_height = 50
    summary_table_width = [300, 150, 100]

    live_image = []
    grid_view = {'pos': None,
                 'adj': None,
                 'item': None,
                 'color': (0, 0, 255, 255, 1)}

    profile_color = (0, 255, 0, 255, 1)

    display_ui = []

    # guide and profile pg ROIs
    list_guide_pyqt_roi = list()
    list_profile_pyqt_roi = list()
    list_table_widget_checkbox = list()
    default_guide_roi = {'x0': 0, 'y0': 0, 'width':200, 'height': 800,
                         'isChecked': True,
                         'color_activated':'r',
                         'color_deactivated': 'b'}
    previous_active_row = -1 # use to deactivated the guide and profile roi

    # default_guide_table_values = {'isChecked': True, 'x0': 0, 'y0': 0,
    #                               'width': 200, 'height': 200}
    default_profile_width_values = np.arange(1,50,2)


    #remove-me
    test_roi = None


    # col_width = 65
    # table_column_width = [col_width, col_width, col_width, col_width, 100]
    # default_measurement_roi = {'x0': 0, 'y0': 0,
    #                            'width': np.NaN, 'height': np.NaN}
    #
    # # where the mean counts and calibrated value will be displayed
    # calibration = {}      # '1' : {'mean_counts' : _mean, 'value': _value}
    #
    # measurement_dict = {}   # '1': [ measurement data calibrated ]
    #
    # calibration_widgets = {}
    # calibration_widgets_label = {}
    # calibrated_roi = {'1': {'x0': 0,
    #                         'y0': 0,
    #                         'width': 200,
    #                         'height': 200,
    #                         'value': 1,  #np.NaN
    #                         },
    #                   '2': {'x0': np.NaN,
    #                         'y0': np.NaN,
    #                         'width': 200,
    #                         'height': 200,
    #                         'value': 10, #np.NaN
    #                         },
    #                   }
    #
    # roi_ui_measurement = list() # keep record of all the pyqtgraph.ROI ui
    # roi_ui_calibrated = []


    def __init__(self, parent=None, working_dir='', data_dict=None):

        display(HTML('<span style="font-size: 20px; color:blue">Check UI that poped up \
            (maybe hidden behind this browser!)</span>'))

        QMainWindow.__init__(self, parent=parent)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Profile")

        self.working_dir = working_dir
        self.data_dict = data_dict # Normalization data dictionary  {'file_name': [],
                                                                     #'data': [[...],[...]]],
                                                                     #'metadata': [],
                                                                     #'shape': {}}

        # untouched array of images (used to move and rotate images)
        self.data_dict_raw = copy.deepcopy(data_dict)

        # initialization
        self.init_timestamp_dict()
        self.init_table()
        self.init_parameters()
        self.init_widgets()
        self.init_pyqtgraph()

        # self.init_statusbar()
        #
        # # display first image
        self.slider_file_changed(-1)

        #
        # self.ui.tableWidget.cellChanged['int', 'int'].connect(self.cell_changed)

    # initialization
    def init_timestamp_dict(self):
        list_files = self.data_dict['file_name']
        self.timestamp_dict = retrieve_time_stamp(list_files)

    def init_statusbar(self):
        pass
        # self.ui.info_label = QtGui.QLabel("")
        # self.ui.statusbar.addPermanentWidget(self.ui.info_label)

    def init_widgets(self):
        """size and label of any widgets"""

        _file_path = os.path.dirname(__file__)
        left_rotation_fast_file = os.path.abspath(os.path.join(_file_path,
                                                               'static/profile/button_rotation_left_fast.png'))
        self.ui.left_rotation_button_fast.setStyleSheet("background-image: "
                                                        "url('" + left_rotation_fast_file + "'); " + \
                                                        "background-repeat: no-repeat")

        right_rotation_fast_file = os.path.abspath(os.path.join(_file_path,
                                                                'static/profile/button_rotation_right_fast.png'))
        self.ui.right_rotation_button_fast.setStyleSheet("background-image: "
                                                         "url('" + right_rotation_fast_file + "'); " + \
                                                        "background-repeat: no-repeat")

        left_rotation_slow_file = os.path.abspath(os.path.join(_file_path,
                                                               'static/profile/button_rotation_left_slow.png'))
        self.ui.left_rotation_button_slow.setStyleSheet("background-image: "
                                                        "url('" + left_rotation_slow_file + "'); " + \
                                                            "background-repeat: no-repeat")

        right_rotation_slow_file = os.path.abspath(os.path.join(_file_path,
                                                                'static/profile/button_rotation_right_slow.png'))
        self.ui.right_rotation_button_slow.setStyleSheet("background-image: "
                                                         "url('" + right_rotation_slow_file + "'); " + \
                                                        "background-repeat: no-repeat")

        self.ui.splitter_2.setSizes([250, 50])
        self.ui.splitter.setSizes([250, 50])

        # file slider
        self.ui.file_slider.setMaximum(len(self.data_dict['data'])-1)

        # update size of table columns
        nbr_columns = self.ui.tableWidget.columnCount()
        for _col in range(nbr_columns):
            self.ui.tableWidget.setColumnWidth(_col, self.guide_table_width[_col])

        # update size of summary table
        nbr_columns = self.ui.summary_table.columnCount()
        for _col in range(nbr_columns):
            self.ui.summary_table.setColumnWidth(_col, self.summary_table_width[_col])

        self.display_ui = [self.ui.display_size_label,
                           self.ui.grid_size_slider,
                           self.ui.display_transparency_label,
                           self.ui.transparency_slider]

    def init_pyqtgraph(self):
        # image
        self.ui.image_view = pg.ImageView(view=pg.PlotItem())
        self.ui.image_view.ui.menuBtn.hide()
        self.ui.image_view.ui.roiBtn.hide()
        vertical_layout = QtGui.QVBoxLayout()
        vertical_layout.addWidget(self.ui.image_view)
        self.ui.pyqtgraph_widget.setLayout(vertical_layout)

        # profile
        self.ui.profile_view = pg.PlotWidget()
        self.legend = self.ui.profile_view.addLegend()
        vertical_layout2 = QtGui.QVBoxLayout()
        vertical_layout2.addWidget(self.ui.profile_view)
        self.ui.profile_widget.setLayout(vertical_layout2)

    def init_table(self):
        # init the summary table
        list_files_full_name = self.data_dict['file_name']
        list_files_short_name = [os.path.basename(_file) for _file in list_files_full_name]

        list_time_stamp = self.timestamp_dict['list_time_stamp']
        list_time_stamp_user_format = self.timestamp_dict['list_time_stamp_user_format']
        time_0 = list_time_stamp[0]
        for _row, _file in enumerate(list_files_short_name):
            self.ui.summary_table.insertRow(_row)
            self.set_item_summary_table(row=_row, col=0, value=_file)
            self.set_item_summary_table(row=_row, col=1, value=list_time_stamp_user_format[_row])
            _offset = list_time_stamp[_row] - time_0
            self.set_item_summary_table(row=_row, col=2, value="{:0.2f}".format(_offset))

    def init_parameters(self):
        # init the position of the measurement ROI
        [height, width] = np.shape(self.data_dict['data'][0])
        self.default_guide_roi['width'] = np.int(width/10)
        self.default_guide_roi['height'] = np.int(height/5)
        self.default_guide_roi['x0'] = np.int(width/2)
        self.default_guide_roi['y0'] = np.int(height/2)
        self.default_profile_width_values = [str(_value) for _value in self.default_profile_width_values]

    # main methods
    def remove_all_guides(self):
        # remove all teh guids
        for _roi in self.list_guide_pyqt_roi:
            self.ui.image_view.removeItem(_roi)

    def display_guides(self):
        # check if we want to display this guide or not
        nbr_row = self.ui.tableWidget.rowCount()
        for row in np.arange(nbr_row):
            _guide = self.list_guide_pyqt_roi[row]
            _widget = self.ui.tableWidget.cellWidget(row, 0).children()[1]
            if _widget.isChecked():
                self.ui.image_view.addItem(_guide)

    def remove_all_profiles(self):
        for _roi in self.list_profile_pyqt_roi:
            self.ui.image_view.removeItem(_roi)

    def display_profiles(self):
        nbr_row = self.ui.table_widget.rowCount()
        is_x_profile_direction = self.ui.profile_direction_x_axis.isChecked()
        for _row in np.arange(nbr_row):
            [x0, y0, width, height] = self.get_item_row(row=_row)
            _profile_width = self.get_profile_width(row=_row)
            print("_profile_width: {}".format(_profile_width))


    def display_image(self, recalculate_image=False):
        """display the image selected by the file slider"""
        _image = self.get_image_selected(recalculate_image=recalculate_image)
        _view = self.ui.image_view.getView()
        _view_box = _view.getViewBox()
        _state = _view_box.getState()

        first_update = False
        if self.histogram_level == []:
            first_update = True
        _histo_widget = self.ui.image_view.getHistogramWidget()
        self.histogram_level = _histo_widget.getLevels()

        _image = np.transpose(_image)
        self.ui.image_view.setImage(_image)
        self.live_image = _image
        _view_box.setState(_state)

        if not first_update:
            _histo_widget.setLevels(self.histogram_level[0], self.histogram_level[1])

        # remove previous grid if any
        if self.grid_view['item']:
            self.ui.image_view.removeItem(self.grid_view['item'])

        # if we want a grid
        if self.ui.grid_display_checkBox.isChecked():

            grid_size = self.ui.grid_size_slider.value()
            [height, width] = np.shape(self.live_image)

            pos_adj_dict = self.calculate_matrix_grid(grid_size=grid_size,
                                                      height=height,
                                                      width=width)
            pos = pos_adj_dict['pos']
            adj = pos_adj_dict['adj']

            line_color = self.grid_view['color']
            _transparency_value = 255 - (np.float(str(self.ui.transparency_slider.value()))/100) * 255
            _list_line_color = list(line_color)
            _list_line_color[3] = _transparency_value
            line_color = tuple(_list_line_color)
            lines = np.array([line_color for n in np.arange(len(pos))],
                             dtype=[('red', np.ubyte), ('green', np.ubyte),
                                    ('blue', np.ubyte), ('alpha', np.ubyte),
                                    ('width', float)])

            grid = pg.GraphItem()
            self.ui.image_view.addItem(grid)
            grid.setData(pos=pos,
                         adj=adj,
                         pen=lines,
                         symbol=None,
                         pxMode=False)
            self.grid_view['item'] = grid


        # calibrated and measurement ROIs
        # self.display_roi()

    def calculate_matrix_grid(self, grid_size=1, height=1, width=1):
        """calculate the matrix that defines the vertical and horizontal lines
        that allow pyqtgraph to display the grid"""

        pos_adj_dict = {}

        # pos - each matrix defines one side of the line
        pos = []
        adj = []

        # vertical lines
        x = 0
        index = 0
        while (x <= width):
            one_edge = [x, 0]
            other_edge = [x, height]
            pos.append(one_edge)
            pos.append(other_edge)
            adj.append([index, index + 1])
            x += grid_size
            index += 2

        # vertical lines
        y = 0
        while (y <= height):
            one_edge = [0, y]
            other_edge = [width, y]
            pos.append(one_edge)
            pos.append(other_edge)
            adj.append([index, index + 1])
            y += grid_size
            index += 2

        pos_adj_dict['pos'] = np.array(pos)
        pos_adj_dict['adj'] = np.array(adj)

        return pos_adj_dict

    def remove_row(self, row=-1):

        if row == -1:
            return

        self.ui.tableWidget.removeRow(row)
        self.ui.tableWidget_2.removeRow(row)
        self.ui.image_view.removeItem(self.list_guide_pyqt_roi[row])
        self.list_guide_pyqt_roi.remove(self.list_guide_pyqt_roi[row])
        # self.list_profile_pyqt_roi.remove(self.list_profile_pyqt_roi[row])
        #self.list_table_widget_checkbox.remove(self.list_profile_pyqt_roi[row])

        nbr_row = self.ui.tableWidget.rowCount()
        if row == nbr_row:
            row -= 1

        if nbr_row > 0:
            nbr_col = self.ui.tableWidget.columnCount()
            new_selection = QtGui.QTableWidgetSelectionRange(row, 0, row, nbr_col - 1)
            self.ui.tableWidget.setRangeSelected(new_selection, True)
            new_selection_2 = QtGui.QTableWidgetSelectionRange(row, 0, row, 1)
            self.ui.tableWidget_2.setRangeSelected(new_selection_2, True)

    def update_guide_roi_using_guide_table(self, row=-1):
        [x0, y0, width, height] = self.get_item_row(row=row)
        roi_ui = self.list_guide_pyqt_roi[row]
        roi_ui.blockSignals(True)
        roi_ui.setPos((x0, y0))
        roi_ui.setSize((width, height))
        roi_ui.blockSignals(False)

    def update_profile_roi_using_guide_table(self, row=-1):
        pass

    def update_guide_table_using_guide_rois(self):
        for _row, _roi in enumerate(self.list_guide_pyqt_roi):
            region = _roi.getArraySlice(self.live_image,
                                        self.ui.image_view.imageItem)

            x0 = region[0][0].start
            x1 = region[0][0].stop
            y0 = region[0][1].start
            y1 = region[0][1].stop

            width = np.abs(x1 - x0)-1
            height = np.abs(y1 - y0)-1

            self.set_item_main_table(row=_row, col=1, value=str(x0))
            self.set_item_main_table(row=_row, col=2, value=str(y0))
            self.set_item_main_table(row=_row, col=3, value=str(width))
            self.set_item_main_table(row=_row, col=4, value=str(height))

    def add_guide_and_profile_pyqt_roi(self, row=-1):
        """add the pyqtgraph roi guide and profiles"""
        if row == -1:
            row = 0

        # guide
        guide_roi = pg.RectROI([self.default_guide_roi['x0'], self.default_guide_roi['y0']],
                                [self.default_guide_roi['width'], self.default_guide_roi['height']],
                            pen=self.default_guide_roi['color_activated'])
        guide_roi.addScaleHandle([1, 1], [0, 0])
        guide_roi.addScaleHandle([0, 0], [1, 1])
        guide_roi.sigRegionChanged.connect(self.guide_changed)
        self.ui.image_view.addItem(guide_roi)
        self.list_guide_pyqt_roi.insert(row, guide_roi)

        # profile
        [x0, y0, width, height] = self.get_item_row(row=row)
        _profile_width = self.get_profile_width(row=row)
        is_x_profile_direction = self.ui.profile_direction_x_axis.isChecked()
        delta_profile = (_profile_width - 1) / 2.
        if is_x_profile_direction:

            profile_center = y0 + np.abs(np.int((height)/2.))

            y_top = profile_center - delta_profile
            y_bottom = profile_center + delta_profile

            x_left = x0
            x_right = x0 + width

            pos = []
            pos.append([x_left, y_top])
            pos.append([x_right, y_top])
            adj = []
            adj.append([0, 1])

            if y_top != y_bottom: # height == 1
                pos.append([x_left, y_bottom])
                pos.append([x_right, y_bottom])
                adj.append([2, 3])

            adj = np.array(adj)
            pos = np.array(pos)

        else: # y-profile direction

            profile_center = x0 + np.abs(np.int((width) / 2.))

            x_left = profile_center - delta_profile
            x_right = profile_center + delta_profile

            y_top = y0
            y_bottom = y0 + height

            pos = []
            pos.append([x_left, y_top])
            pos.append([x_right, y_top])
            adj = []
            adj.append([0, 1])

            if y_top != y_bottom:  # height == 1
                pos.append([x_left, y_bottom])
                pos.append([x_right, y_bottom])
                adj.append([2, 3])

            adj = np.array(adj)
            pos = np.array(pos)




        line_color = self.profile_color
        _list_line_color = list(line_color)
        line_color = tuple(_list_line_color)
        lines = np.array([line_color for n in np.arange(len(pos))],
                         dtype=[('red', np.ubyte), ('green', np.ubyte),
                                ('blue', np.ubyte), ('alpha', np.ubyte),
                                ('width', float)])

        grid = pg.GraphItem()
        self.ui.image_view.addItem(grid)
        grid.setData(pos=pos,
                     adj=adj,
                     pen=lines,
                     symbol=None,
                     pxMode=False)

    def insert_row(self, row=-1):
        if row == -1:
            row = 0

        self.ui.tableWidget.blockSignals(True)
        default_values = self.default_guide_roi

        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setRowHeight(row, self.guide_table_height)

        self.set_item_main_table(row=row, col=0, value=default_values['isChecked'])
        self.set_item_main_table(row=row, col=1, value=default_values['x0'])
        self.set_item_main_table(row=row, col=2, value=default_values['y0'])
        self.set_item_main_table(row=row, col=3, value=default_values['width'])
        self.set_item_main_table(row=row, col=4, value=default_values['height'])

        # select new entry
        nbr_row = self.ui.tableWidget.rowCount()
        nbr_col = self.ui.tableWidget.columnCount()
        full_range = QtGui.QTableWidgetSelectionRange(0, 0, nbr_row - 1, nbr_col - 1)
        self.ui.tableWidget.setRangeSelected(full_range, False)
        new_selection = QtGui.QTableWidgetSelectionRange(row, 0, row, nbr_col - 1)
        self.ui.tableWidget.setRangeSelected(new_selection, True)
        self.ui.tableWidget.blockSignals(False)

        self.ui.tableWidget_2.blockSignals(True)
        self.ui.tableWidget_2.insertRow(row)
        self.ui.tableWidget_2.setRowHeight(row, self.guide_table_height)
        self.set_item_profile_table(row=row)

        # select new entry
        nbr_col = self.ui.tableWidget_2.columnCount()
        full_range = QtGui.QTableWidgetSelectionRange(0, 0, nbr_row - 1, nbr_col - 1)
        self.ui.tableWidget_2.setRangeSelected(full_range, False)
        new_selection = QtGui.QTableWidgetSelectionRange(row, 0, row, nbr_col - 1)
        self.ui.tableWidget_2.setRangeSelected(new_selection, True)
        self.ui.tableWidget_2.blockSignals(False)

    # setter
    def set_item_profile_table(self, row=0):
        spacerItem_left = QtGui.QSpacerItem(408, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        widget = QtGui.QComboBox()
        widget.addItems(self.default_profile_width_values)
        widget.blockSignals(True)
        spacerItem_right = QtGui.QSpacerItem(408, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        hori_layout = QtGui.QHBoxLayout()
        hori_layout.addItem(spacerItem_left)
        hori_layout.addWidget(widget)
        hori_layout.addItem(spacerItem_right)
        cell_widget = QtGui.QWidget()
        cell_widget.setLayout(hori_layout)
        self.ui.tableWidget_2.setCellWidget(row, 0, cell_widget)

    def set_item_main_table(self, row=0, col=0, value=''):
        if col == 0:
            spacerItem_left = QtGui.QSpacerItem(408, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
            widget = QtGui.QCheckBox()
            widget.blockSignals(True)
            self.list_table_widget_checkbox.insert(row, widget)
            widget.stateChanged.connect(self.guide_state_changed)
            spacerItem_right = QtGui.QSpacerItem(408, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
            hori_layout = QtGui.QHBoxLayout()
            hori_layout.addItem(spacerItem_left)
            hori_layout.addWidget(widget)
            hori_layout.addItem(spacerItem_right)
            cell_widget = QtGui.QWidget()
            cell_widget.setLayout(hori_layout)
            if value is True:
                widget.setCheckState(QtCore.Qt.Checked)
            else:
                widget.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tableWidget.setCellWidget(row, col, cell_widget)
            widget.blockSignals(False)
        else:
            item = QtGui.QTableWidgetItem(str(value))
            self.ui.tableWidget.setItem(row, col, item)

    def get_profile_width(self, row=0):
        _widget = self.ui.tableWidget_2.cellWidget(row, 0).children()[1]
        return np.int(str(_widget.currentText()))

    def get_item_row(self, row=0):
        x0 = np.int(str(self.ui.tableWidget.item(row, 1).text()))
        y0 = np.int(str(self.ui.tableWidget.item(row, 2).text()))
        width = np.int(str(self.ui.tableWidget.item(row, 3).text()))
        height = np.int(str(self.ui.tableWidget.item(row, 4).text()))
        return (x0, y0, width, height)

    def get_image_selected(self, recalculate_image=False):
        slider_index = self.ui.file_slider.value()
        if recalculate_image:
            angle = self.rotation_angle
            # rotate all images
            self.data_dict['data'] = [transform.rotate(_image, angle) for _image in self.data_dict_raw['data']]

        _image = self.data_dict['data'][slider_index]
        return _image

    def get_selected_row(self, source='tableWidget'):
        if source == 'tableWidget':
            ui = self.ui.tableWidget
        else:
            ui = self.ui.tableWidget_2
        selection = ui.selectedRanges()
        if selection:
            top_row = selection[0].topRow()
            return top_row
        else:
            return -1

    def _highlights_guide_profile_pyqt_roi(self, row=-1, status='activated'):
        if row == -1:
            return
        _guide_ui = self.list_guide_pyqt_roi[row]
        _guide_ui.setPen(self.default_guide_roi['color_' + status])

    def highlight_guide_profile_pyqt_rois(self, row=-1):
        """When user click a row in the table, the correspoinding ROI will be activated and ots
        color will change. The old activated guide and profile will then be deactivated and color will
        change as well according to the color definition found in the self.default_guide_roi dictionary"""
        previous_active_row = self.previous_active_row
        if previous_active_row == -1:
            return

        self._highlights_guide_profile_pyqt_roi(row=previous_active_row, status='deactivated')
        self._highlights_guide_profile_pyqt_roi(row=row, status='activated')

        # _guide_ui = self.list_guide_pyqt_roi[previous_active_row]
        # _guide_ui.setPen(self.default_guide_roi['color_deactivated'])
        #
        # new_guide_ui = self.list_guide_pyqt_roi[row]
        # new_guide_ui.setPen(self.default_guide_roi['color_activated'])


















    def display_roi(self):
        """display the calibrated and measurement rois"""

        # first we remove the calibrated rois
        for _roi_id in self.roi_ui_calibrated:
            self.ui.image_view.removeItem(_roi_id)

        if self.ui.use_calibration1_checkbox.isChecked():
            # yes, we have calibrated rois
            slider_index = self.ui.file_slider.value()

            # calibration1
            cal1_file_index = np.int(self.ui.calibration1_index.text())
            if slider_index == cal1_file_index:
                self.ui.image_view.addItem(self.roi_ui_calibrated[0])

        if self.ui.use_calibration2_checkbox.isChecked():
            # yes, we have calibrated rois
            slider_index = self.ui.file_slider.value()

            # calibration2
            cal2_file_index = np.int(self.ui.calibration2_index.text())
            if slider_index == cal2_file_index:
                self.ui.image_view.addItem(self.roi_ui_calibrated[1])

    def record_calibration(self, index=1):
        x0 = np.int(str(self.calibration_widgets[str(index)]['x0'].text()))
        y0 = np.int(str(self.calibration_widgets[str(index)]['y0'].text()))
        width = np.int(str(self.calibration_widgets[str(index)]['width'].text()))
        height = np.int(str(self.calibration_widgets[str(index)]['height'].text()))
        if np.isnan(np.float(str(self.calibration_widgets[str(index)]['value'].text()))):
            return

        value = np.float(str(self.calibration_widgets[str(index)]['value'].text()))

        if index == 1:
            file_index = np.int(str(self.ui.calibration1_index.text()))
        else:
            file_index = np.int(str(self.ui.calibration2_index.text()))

        _file_data = self.data_dict['data'][file_index]
        _region_data = _file_data[y0:y0+height, x0:x0+width]
        _mean = np.nanmean(_region_data)

        self.calibration[str(index)] = {}
        self.calibration[str(index)]['mean_counts'] = _mean
        self.calibration[str(index)]['value'] = value









    #
    #
    #
    # def insert_column_in_summary_table(self, roi_index=-1):
    #     col_offset = 3
    #     if roi_index == -1:
    #         roi_index = 0
    #
    #     roi_index += col_offset
    #     self.ui.summary_table.insertColumn(roi_index)
    #     item = QtWidgets.QTableWidgetItem()
    #     self.ui.summary_table.setHorizontalHeaderItem(roi_index, item)
    #     self.renamed_summary_table_region_header()
    #
    # def remove_column_in_summary_table(self, roi_index=-1):
    #     col_offset = 3
    #     if roi_index == -1:
    #         roi_index = 0
    #
    #     roi_index += col_offset
    #     self.ui.summary_table.removeColumn(roi_index)
    #     self.renamed_summary_table_region_header()
    #
    # def renamed_summary_table_region_header(self):
    #     # rename all the headers
    #     nbr_col = self.ui.summary_table.columnCount()
    #     if nbr_col <= 3:
    #         return
    #
    #     _index = 1
    #     for _col in np.arange(3, nbr_col):
    #         item = self.ui.summary_table.horizontalHeaderItem(_col)
    #         item.setText("Region {}".format(_index))
    #         _index += 1

    # def update_mean_counts(self, row=-1, all=False):
    #     if all == True:
    #         nbr_row = self.ui.tableWidget.rowCount()
    #         for _row in np.arange(nbr_row):
    #             self.update_mean_counts(row=_row)
    #     else:
    #         # FIXME
    #         pass
    #
    # def insert_measurement_roi_ui(self, row=-1):
    #     default_roi = self.default_measurement_roi
    #     new_roi = pg.RectROI([default_roi['x0'], default_roi['y0']],
    #                          [default_roi['height'], default_roi['width']],
    #                          pen='g')
    #     new_roi.addScaleHandle([1, 1], [0, 0])
    #     new_roi.addScaleHandle([0, 0], [1, 1])
    #     self.ui.image_view.addItem(new_roi)
    #     new_roi.sigRegionChanged.connect(self.measurement_roi_moved)
    #     self.roi_ui_measurement.insert(row, new_roi)
    #
    # def remove_measurement_roi_ui(self, row=-1):
    #     """roi_ui_measurement is where the ROI ui (pyqtgraph) are saved"""
    #     if row == -1:
    #         return
    #     old_roi = self.roi_ui_measurement[row]
    #     self.roi_ui_measurement.remove(old_roi)
    #     self.ui.image_view.removeItem(old_roi)

    def check_status_next_prev_image_button(self):
        """this will enable or not the prev or next button next to the slider file image"""
        current_slider_value = self.ui.file_slider.value()
        min_slider_value = self.ui.file_slider.minimum()
        max_slider_value = self.ui.file_slider.maximum()

        _prev = True
        _next = True

        if current_slider_value == min_slider_value:
            _prev = False
        elif current_slider_value == max_slider_value:
            _next = False

        self.ui.previous_image_button.setEnabled(_prev)
        self.ui.next_image_button.setEnabled(_next)



    def set_item_summary_table(self, row=0, col=0, value=''):
        item = QtGui.QTableWidgetItem(str(value))
        self.ui.summary_table.setItem(row, col, item)
        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)



    def change_slider(self, offset=+1):
        self.ui.file_slider.blockSignals(True)
        current_slider_value = self.ui.file_slider.value()
        new_row_selected = current_slider_value + offset
        self.ui.file_slider.setValue(new_row_selected)
        self.check_status_next_prev_image_button()
        self.display_image()
        self.ui.file_slider.blockSignals(False)

    def measurement_roi_moved(self):
        self.update_all_measurement_rois_from_view()
        self.display_measurement_profiles()

    def slider_file_changed(self, index_selected):
        self.display_image()
        slider_value = self.ui.file_slider.value()
        self.ui.image_slider_value.setText(str(slider_value))
        self.check_status_next_prev_image_button()
        # self.display_measurement_profiles()


    ## Event Handler
    def guide_changed(self):
        self.update_guide_table_using_guide_rois()

        # print(self.list_guide_pyqt_roi.index(source))

    def table_widget_selection_changed(self):
        self.ui.tableWidget_2.blockSignals(True)
        nbr_col = self.ui.tableWidget_2.columnCount()
        nbr_row = self.ui.tableWidget_2.rowCount()
        full_range = QtGui.QTableWidgetSelectionRange(0, 0, nbr_row - 1, nbr_col - 1)
        self.ui.tableWidget_2.setRangeSelected(full_range, False)
        row = self.get_selected_row()
        new_selection = QtGui.QTableWidgetSelectionRange(row, 0, row, nbr_col - 1)
        self.ui.tableWidget_2.setRangeSelected(new_selection, True)
        self.highlight_guide_profile_pyqt_rois(row=row)
        self.ui.tableWidget_2.blockSignals(False)
        self.previous_active_row = row

    def table_widget_2_selection_changed(self):
        self.ui.tableWidget.blockSignals(True)
        nbr_col = self.ui.tableWidget.columnCount()
        nbr_row = self.ui.tableWidget.rowCount()
        full_range = QtGui.QTableWidgetSelectionRange(0, 0, nbr_row - 1, nbr_col - 1)
        self.ui.tableWidget.setRangeSelected(full_range, False)
        row = self.get_selected_row(source='tableWidget_2')
        new_selection = QtGui.QTableWidgetSelectionRange(row, 0, row, nbr_col - 1)
        self.ui.tableWidget.setRangeSelected(new_selection, True)
        self.highlight_guide_profile_pyqt_rois(row=row)
        self.ui.tableWidget.blockSignals(False)
        self.previous_active_row = row

    def table_widget_cell_changed(self, row, column):
        self.update_guide_roi_using_guide_table(row=row)

    def guide_state_changed(self, state):
        self.remove_all_guides()
        self.display_guides()
        self.remove_all_profiles()
        self.display_profiles()

    def display_grid_clicked(self):
        status = self.ui.grid_display_checkBox.isChecked()
        for _widget in self.display_ui:
            _widget.setEnabled(status)
        self.display_image()

    def grid_size_slider_clicked(self):
        self.display_image()

    def grid_size_slider_released(self):
        self.display_image()

    def grid_size_slider_moved(self, value):
        self.display_image()

    def transparency_slider_clicked(self):
        self.display_image()

    def transparency_slider_moved(self, value):
        self.display_image()

    @wait_cursor
    def right_rotation_slow_clicked(self):
        self.rotation_angle -= 0.1
        self.display_image(recalculate_image=True)

    @wait_cursor
    def left_rotation_slow_clicked(self):
        self.rotation_angle += 0.1
        self.display_image(recalculate_image=True)

    @wait_cursor
    def right_rotation_fast_clicked(self):
        self.rotation_angle -= 1
        self.display_image(recalculate_image=True)

    @wait_cursor
    def left_rotation_fast_clicked(self):
        self.rotation_angle += 1
        self.display_image(recalculate_image=True)

    def add_row_button_clicked(self):
        selected_row = self.get_selected_row()
        self._highlights_guide_profile_pyqt_roi(row=selected_row, status='deactivated')
        self.insert_row(row=selected_row)
        self.add_guide_and_profile_pyqt_roi(row=selected_row)
        self.previous_active_row = selected_row

    def remove_row_button_clicked(self):
        selected_row = self.get_selected_row()
        self.remove_row(row=selected_row)

    def profile_along_axis_changed(self):
        self.display_profiles()

    def export_button_clicked(self):
        print("export button clicked")
        # _export_folder = QFileDialog.getExistingDirectory(self,
        #                                                   directory=self.working_dir,
        #                                                   caption = "Select Output Folder",
        #                                                   options=QFileDialog.ShowDirsOnly)
        # if _export_folder:
        #     o_export = ExportCalibration(parent = self,
        #                                  export_folder = _export_folder)
        #     o_export.run()
        #     QtGui.QGuiApplication.processEvents()

    def previous_image_button_clicked(self):
        self.change_slider(offset = -1)
        # self.display_measurement_profiles()

    def next_image_button_clicked(self):
        self.change_slider(offset = +1)
        # self.display_measurement_profiles()

    def help_button_clicked(self):
        import webbrowser
        webbrowser.open("https://neutronimaging.pages.ornl.gov/en/tutorial/notebooks/profile/")

    def closeEvent(self, event=None):
        pass
