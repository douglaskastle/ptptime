# -*- coding: utf-8 -*-
import unittest
import ptptime.ptptime as ptptime
from ptptime.Test.utils import checkAttributes

class TestTimestamp(unittest.TestCase):
	def testFromPtp(self):
		t = ptptime.timefromptp(0x0000000000000000)
		if not isinstance(t, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(t))
		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': 0}
		checkAttributes(t, d)
		
		t = ptptime.timefromptp(0x386d438000000000)
		if not isinstance(t, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(t))
		d = {'year': 2000, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': 0}
		checkAttributes(t, d)

		t = ptptime.timefromptp(0x386d43A000000000, leapyear=-1)
		if not isinstance(t, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(t))
		d = {'year': 2000, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': -1}
		checkAttributes(t, d)

		t = ptptime.timefromptp(0x386d438100000000, leapyear=1)
		if not isinstance(t, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(t))
		d = {'year': 2000, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': 1}
		checkAttributes(t, d)

		t = ptptime.timefromptp(0x14b0823f3b9ac618)
		if not isinstance(t, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(t))
		d = {'year': 1980, 'month': 12 , 'day': 31, 'hour': 11, 'minute': 59, 'second': 59, 'microsecond': 999999, 'nanosecond': 0, 'leapyear': 0}
		checkAttributes(t, d)

		t = ptptime.timefromptp(0x14b12aff3b9ac618)
		if not isinstance(t, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(t))
		d = {'year': 1980, 'month': 12 , 'day': 31, 'hour': 23, 'minute': 59, 'second': 59, 'microsecond': 999999, 'nanosecond': 0, 'leapyear': 0}
		checkAttributes(t, d)

		d = {'year': 1981, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)

		t = t - ptptime.timedelta(microseconds=1)
		d = {'year': 1980, 'month': 12 , 'day': 31, 'hour': 23, 'minute': 59, 'second': 59, 'microsecond': 999999, 'nanosecond': 0, 'leapyear': 0}
		checkAttributes(t, d)
		expected = 0x14b12aff3b9ac618
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		
		t = t - ptptime.timedelta(hours=12)
		d = {'year': 1980, 'month': 12 , 'day': 31, 'hour': 11, 'minute': 59, 'second': 59, 'microsecond': 999999, 'nanosecond': 0, 'leapyear': 0}
		checkAttributes(t, d)
		expected = 0x14b0823f3b9ac618
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
