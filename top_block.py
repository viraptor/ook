#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Jan 16 19:00:37 2016
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
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import bitgate
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, freq=434000000, large_sig_len=0.0015, signal_mult=1):
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
        self.freq = freq
        self.large_sig_len = large_sig_len
        self.signal_mult = signal_mult

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 240000

        ##################################################
        # Blocks
        ##################################################
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.05, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(1/samp_rate/4)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	20000, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.1)
        self.qtgui_time_sink_x_1.set_y_axis(-5, 2)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ["data", "acc", "trigger", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	20000, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(1)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["mag", "mag avg", "acc", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 3, 3,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 20000, 10000, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/viraptor/Projects/ook/weather_station.wav", False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_threshold_ff_2 = blocks.threshold_ff(0.004, 0.006, 0)
        self.blocks_threshold_ff_1 = blocks.threshold_ff(0.005, 0.008, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.002, 0.006, 0)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "localhost", "52001", 10000, False)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((signal_mult, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((4.5, ))
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(int(samp_rate*large_sig_len), 1.0/samp_rate/large_sig_len, 4000)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_float_to_char_1 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((-3, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1.5, ))
        self.bitgate_triggered_bits_0 = bitgate.triggered_bits(int(samp_rate*large_sig_len*4))
        self.analog_rail_ff_0 = analog.rail_ff(0, 1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.bitgate_triggered_bits_0, 'pdus'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_float_to_char_0_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_time_sink_x_1, 1))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.qtgui_time_sink_x_1, 2))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_float_to_char_0_0, 0), (self.bitgate_triggered_bits_0, 1))    
        self.connect((self.blocks_float_to_char_0_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.blocks_float_to_char_1, 0), (self.bitgate_triggered_bits_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_threshold_ff_2, 0))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.single_pole_iir_filter_xx_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.analog_rail_ff_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_threshold_ff_1, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_threshold_ff_2, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_threshold_ff_2, 0), (self.blocks_float_to_char_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.qtgui_time_sink_x_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate)

    def get_large_sig_len(self):
        return self.large_sig_len

    def set_large_sig_len(self, large_sig_len):
        self.large_sig_len = large_sig_len
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.samp_rate*self.large_sig_len), 1.0/self.samp_rate/self.large_sig_len)

    def get_signal_mult(self):
        return self.signal_mult

    def set_signal_mult(self, signal_mult):
        self.signal_mult = signal_mult
        self.blocks_multiply_const_vxx_1.set_k((self.signal_mult, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.samp_rate*self.large_sig_len), 1.0/self.samp_rate/self.large_sig_len)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 20000, 10000, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_update_time(1/self.samp_rate/4)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--freq", dest="freq", type="intx", default=434000000,
        help="Set freq [default=%default]")
    parser.add_option(
        "", "--large-sig-len", dest="large_sig_len", type="eng_float", default=eng_notation.num_to_str(0.0015),
        help="Set large_sig_len [default=%default]")
    parser.add_option(
        "", "--signal-mult", dest="signal_mult", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set signal_mult [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(freq=options.freq, large_sig_len=options.large_sig_len, signal_mult=options.signal_mult)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
