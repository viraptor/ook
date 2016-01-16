#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Sep 26 21:43:35 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import bitgate
import osmosdr
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, collecting_average_len=2500, edge_average_len=400, freq=434000000):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.collecting_average_len = collecting_average_len
        self.edge_average_len = edge_average_len
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2000000

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(-60, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(1, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 200000, 50000, firdes.WIN_HAMMING, 6.76))
        self.blocks_threshold_ff_1 = blocks.threshold_ff(0.02, 0.1, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.08, 0.1, 0)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "localhost", "52001", 10000, False)
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(edge_average_len, 1.0/edge_average_len, 4000)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(collecting_average_len, 1.0/collecting_average_len, 4000)
        self.blocks_float_to_char_1 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.bitgate_triggered_bits_0 = bitgate.triggered_bits(collecting_average_len*4)
        self.analog_rail_ff_0 = analog.rail_ff(0, 1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.bitgate_triggered_bits_0, 'pdus'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_float_to_char_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_float_to_char_0_0, 0), (self.bitgate_triggered_bits_0, 1))    
        self.connect((self.blocks_float_to_char_1, 0), (self.bitgate_triggered_bits_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_threshold_ff_1, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.analog_rail_ff_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_char_1, 0))    
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_collecting_average_len(self):
        return self.collecting_average_len

    def set_collecting_average_len(self, collecting_average_len):
        self.collecting_average_len = collecting_average_len
        self.blocks_moving_average_xx_0.set_length_and_scale(self.collecting_average_len, 1.0/self.collecting_average_len)

    def get_edge_average_len(self):
        return self.edge_average_len

    def set_edge_average_len(self, edge_average_len):
        self.edge_average_len = edge_average_len
        self.blocks_moving_average_xx_1.set_length_and_scale(self.edge_average_len, 1.0/self.edge_average_len)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 200000, 50000, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--collecting-average-len", dest="collecting_average_len", type="intx", default=2500,
        help="Set collecting_average_len [default=%default]")
    parser.add_option("", "--edge-average-len", dest="edge_average_len", type="intx", default=400,
        help="Set edge_average_len [default=%default]")
    parser.add_option("", "--freq", dest="freq", type="intx", default=434000000,
        help="Set freq [default=%default]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block(collecting_average_len=options.collecting_average_len, edge_average_len=options.edge_average_len, freq=options.freq)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
