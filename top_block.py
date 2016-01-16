#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jan 17 00:27:30 2016
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

    def __init__(self, large_sig_len=0.0015, signal_mult=2, freq=433866000):
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
        self.large_sig_len = large_sig_len
        self.signal_mult = signal_mult
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 240000

        ##################################################
        # Blocks
        ##################################################
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.2, 1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(-24, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(1, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 10000, 10000, firdes.WIN_HAMMING, 6.76))
        self.blocks_threshold_ff_2 = blocks.threshold_ff(0, 0, 0)
        self.blocks_threshold_ff_1 = blocks.threshold_ff(0, 0, 0)
        self.blocks_sub_xx_2 = blocks.sub_ff(1)
        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "localhost", "52001", 10000, False)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((signal_mult, ))
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(int(samp_rate*large_sig_len), 0.8/samp_rate/large_sig_len, 4000)
        self.blocks_float_to_char_1 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, int(samp_rate*0.00005))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.bitgate_triggered_bits_0 = bitgate.triggered_bits(int(samp_rate*large_sig_len*5), False)
        self.analog_rail_ff_1 = analog.rail_ff(0.001, 1)
        self.analog_rail_ff_0 = analog.rail_ff(0, 1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.bitgate_triggered_bits_0, 'pdus'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_float_to_char_0_0, 0))    
        self.connect((self.analog_rail_ff_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.analog_rail_ff_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_delay_1, 0), (self.blocks_float_to_char_1, 0))    
        self.connect((self.blocks_float_to_char_0_0, 0), (self.bitgate_triggered_bits_0, 1))    
        self.connect((self.blocks_float_to_char_1, 0), (self.bitgate_triggered_bits_0, 0))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_sub_xx_1, 1))    
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_sub_xx_2, 1))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.single_pole_iir_filter_xx_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.analog_rail_ff_0, 0))    
        self.connect((self.blocks_sub_xx_1, 0), (self.blocks_sub_xx_2, 0))    
        self.connect((self.blocks_sub_xx_1, 0), (self.blocks_threshold_ff_1, 0))    
        self.connect((self.blocks_sub_xx_2, 0), (self.blocks_threshold_ff_2, 0))    
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_threshold_ff_2, 0), (self.blocks_delay_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_sub_xx_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_large_sig_len(self):
        return self.large_sig_len

    def set_large_sig_len(self, large_sig_len):
        self.large_sig_len = large_sig_len
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.samp_rate*self.large_sig_len), 0.8/self.samp_rate/self.large_sig_len)

    def get_signal_mult(self):
        return self.signal_mult

    def set_signal_mult(self, signal_mult):
        self.signal_mult = signal_mult
        self.blocks_multiply_const_vxx_1.set_k((self.signal_mult, ))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_delay_1.set_dly(int(self.samp_rate*0.00005))
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.samp_rate*self.large_sig_len), 0.8/self.samp_rate/self.large_sig_len)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 10000, 10000, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--large-sig-len", dest="large_sig_len", type="eng_float", default=eng_notation.num_to_str(0.0015),
        help="Set large_sig_len [default=%default]")
    parser.add_option(
        "", "--signal-mult", dest="signal_mult", type="eng_float", default=eng_notation.num_to_str(2),
        help="Set signal_mult [default=%default]")
    parser.add_option(
        "", "--freq", dest="freq", type="intx", default=433866000,
        help="Set freq [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(large_sig_len=options.large_sig_len, signal_mult=options.signal_mult, freq=options.freq)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
