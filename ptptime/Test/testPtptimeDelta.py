# -*- coding: utf-8 -*-
import datetime
import unittest
import ptptime.ptptime as ptptime
from ptptime.Test.utils import checkAttributes

class TestPtptimeDelta(unittest.TestCase):
	
	def testPTPTimeDelta(self):
		#i = {'max': 0, 'min': 0,'total_seconds': 0}
		e = {'years': 0, 'months': 0 , 'hours': 0, 'minutes': 0,}
		t = ptptime.timedelta()
# 		for key in e.keys():
# 			if not getattr(t, key):
# 				assert False, "Timedelta Attribute: '{0}' not as expected {1}, received {2}".format(key, d[key], getattr(t, key))
		
		t = ptptime.timedelta(days=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = 1
		checkAttributes(t, d)

		if not str(t) == "1 day, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(hours=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['seconds'] = 3600
		checkAttributes(t, d)

		if not str(t) == "1:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(minutes=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['seconds'] = 60
		checkAttributes(t, d)
	
		if not str(t) == "0:01:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(seconds=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['seconds'] = 1
		checkAttributes(t, d)
	
		if not str(t) == "0:00:01":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(microseconds=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['microseconds'] = 1
		checkAttributes(t, d)
	
		if not str(t) == "0:00:00.000001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(nanoseconds=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['nanoseconds'] = 1
		checkAttributes(t, d)

		t = ptptime.timedelta(nanoseconds=1001)
		d = {'days': 0, 'seconds': 0, 'microseconds': 1, 'nanoseconds': 0,}
		d['nanoseconds'] = 1
		checkAttributes(t, d)

		if not str(t) == "0:00:00.000001:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(days=1, hours=1, minutes=1, seconds=1, microseconds=1, nanoseconds=1)
		d = {'days': 1, 'seconds': 3661, 'microseconds': 1, 'nanoseconds': 1,}
		checkAttributes(t, d)

		if not str(t) == "1 day, 1:01:01.000001:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(days=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		checkAttributes(t, d)

		if not str(t) == "-1 day, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(hours=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 82800
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(minutes=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 86340
		checkAttributes(t, d)
	
		if not str(t) == "-1 day, 23:59:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(seconds=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 86399
		checkAttributes(t, d)
	
		if not str(t) == "-1 day, 23:59:59":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(microseconds=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 86399
		d['microseconds'] = 999999
		checkAttributes(t, d)
	
		if not str(t) == "-1 day, 23:59:59.999999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(days=-1, hours=-1)
		d = {'days': -2, 'seconds': 82800, 'microseconds': 0, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 23:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(days=-1, hours=-1, minutes=-1)
		d = {'days': -2, 'seconds': 82740, 'microseconds': 0, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:59:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1)
		d = {'days': -2, 'seconds': 82739, 'microseconds': 0, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:58:59":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1, microseconds=-1, nanoseconds=1)
		d = {'days': -2, 'seconds': 82738, 'microseconds': 999999, 'nanoseconds': 1,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:58:58.999999:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(nanoseconds=-1)
		d = {'days': -1, 'seconds': 86399, 'microseconds': 999999, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(nanoseconds=-1001)
		d = {'days': -1, 'seconds': 86399, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:59.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

# 		m = datetime.timedelta(microseconds=-1)
# 		d = {'days': -1, 'seconds': 86399, 'microseconds': 999999}
# 		checkAttributes(m, d)
		
		t = ptptime.timedelta(microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 86399, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:59.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 86398, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = ptptime.timedelta(minutes=-1, seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 86338, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:58:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))


		t = datetime.timedelta(hours=-1, minutes=-1, seconds=-1, microseconds=-1)
		if not str(t) == "-1 day, 22:58:58.999999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		d = {'days': -1, 'seconds': 82738, 'microseconds': 999999}
		checkAttributes(t, d)

		t = ptptime.timedelta(hours=-1, minutes=-1, seconds=-1, microseconds=-1)
		d = {'days': -1, 'seconds': 82738, 'microseconds': 999999, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 22:58:58.999999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		
		t = ptptime.timedelta(hours=-1, minutes=-1, seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 82738, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 22:58:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		

		t = ptptime.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -2, 'seconds': 82738, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:58:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
	
	def testPTPSubTimeDelta(self):
		t0 = ptptime.ptptime(2000,1,1,0,0,0,0,0)
		expected = 0x386d437f3b9ac9ff
		t = t0 - ptptime.timedelta(nanoseconds=1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		t = t0 + ptptime.timedelta(nanoseconds=-1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		
		expected = 0x386d437f3b9ac618
		t = t0 - ptptime.timedelta(microseconds=1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		t = t0 + ptptime.timedelta(microseconds=-1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)

		expected = 0x386d437f00000000
		t = t0 - ptptime.timedelta(seconds=1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		t = t0 + ptptime.timedelta(seconds=-1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)

		expected = 0x386bf20000000000
		t = t0 - ptptime.timedelta(days=1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		t = t0 + ptptime.timedelta(days=-1)
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
