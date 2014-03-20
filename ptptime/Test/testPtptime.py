# -*- coding: utf-8 -*-
import os
import sys
import shutil
import datetime
import unittest
import ptptime.ptptime as ptptime
from ptptime.Test.utils import checkAttributes

class TestPtptime(unittest.TestCase):
	
	def setUp(self):
		self.workdir = "./nose_temp"
		os.mkdir(self.workdir)

	def tearDown(self):
		shutil.rmtree(self.workdir)

	def test_b(self):
		assert 'b' == 'b'

	def testPTPAddition(self):
		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(days=1)
		d['day'] = 13
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-13 16:24:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(hours=1)
		d['hour'] = 17
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 17:24:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(minutes=1)
		d['minute'] = 25
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:25:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(seconds=1)
		d['second'] = 35
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:35.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(microseconds=1)
		d['microsecond'] = 123457
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123457:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 1
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123456:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=999)
		d['nanosecond'] = 999
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123456:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=1000)
		d['nanosecond'] = 0
		d['microsecond'] = 123457
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123457:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=1001)
		d['nanosecond'] = 1
		d['microsecond'] = 123457
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123457:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 999999, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=1001)
		d['nanosecond'] = 1
		d['microsecond'] = 0
		d['second'] = 35
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:35.000000:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 1, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], d['nanosecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 2
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123456:002":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 501, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], d['nanosecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=501)
		d['nanosecond'] = 2
		d['microsecond'] = 123457
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123457:002":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 1, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], nanosecond=d['nanosecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 2
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123456:002":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 501, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], nanosecond=d['nanosecond'])
		checkAttributes(t, d)
		tn = t + ptptime.timedelta(nanoseconds=501)
		d['nanosecond'] = 2
		d['microsecond'] = 123457
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123457:002":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

	def testPTPSubtraction(self):
		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(days=1)
		d['day'] = 11
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-11 16:24:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(hours=1)
		d['hour'] = 15
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 15:24:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(minutes=1)
		d['minute'] = 23
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:23:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(seconds=1)
		d['second'] = 33
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:33.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(microseconds=1)
		d['microsecond'] = 123455
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123455:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 54, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 53
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123456:053":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 123455
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:34.123455:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 33
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:24:33.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 23
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 16:23:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 15
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-12 15:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 23
		d['day'] = 11
		checkAttributes(tn, d)
		if not str(tn) == "1972-11-11 23:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 11 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 23
		d['day'] = 31
		d['month'] = 10
		checkAttributes(tn, d)
		if not str(tn) == "1972-10-31 23:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 23
		d['day'] = 31
		d['month'] = 12
		d['year'] = 1971
		checkAttributes(tn, d)
		if not str(tn) == "1971-12-31 23:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1)
		d['nanosecond'] = 999
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 23
		d['day'] = 31
		d['month'] = 12
		d['year'] = 1969
		checkAttributes(tn, d)
		if not str(tn) == "1969-12-31 23:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1001)
		d['nanosecond'] = 999
		d['microsecond'] = 999998
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 23
		d['day'] = 31
		d['month'] = 12
		d['year'] = 1971
		checkAttributes(tn, d)
		if not str(tn) == "1971-12-31 23:59:59.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

		d = {'year': 1972, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 501, 'leapyear': False}
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)
		tn = t - ptptime.timedelta(nanoseconds=1002)
		d['nanosecond'] = 499
		d['microsecond'] = 999999
		d['second'] = 59
		d['minute'] = 59
		d['hour'] = 23
		d['day'] = 31
		d['month'] = 12
		d['year'] = 1971
		checkAttributes(tn, d)
		if not str(tn) == "1971-12-31 23:59:59.999999:499":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=999)
# 		d['nanosecond'] = 999
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123456:999":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=1000)
# 		d['nanosecond'] = 0
# 		d['microsecond'] = 123457
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123457:000":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=1001)
# 		d['nanosecond'] = 1
# 		d['microsecond'] = 123457
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123457:001":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 999999, 'nanosecond': 0, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=1001)
# 		d['nanosecond'] = 1
# 		d['microsecond'] = 0
# 		d['second'] = 35
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:35.000000:001":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 1, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], d['nanosecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=1)
# 		d['nanosecond'] = 2
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123456:002":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 501, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], d['nanosecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=501)
# 		d['nanosecond'] = 2
# 		d['microsecond'] = 123457
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123457:002":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 1, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], nanosecond=d['nanosecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=1)
# 		d['nanosecond'] = 2
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123456:002":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
# 
# 		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 501, 'leapyear': False}
# 		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], nanosecond=d['nanosecond'])
# 		checkAttributes(t, d)
# 		tn = t + ptptime.timedelta(nanoseconds=501)
# 		d['nanosecond'] = 2
# 		d['microsecond'] = 123457
# 		checkAttributes(tn, d)
# 		if not str(tn) == "1972-11-12 16:24:34.123457:002":
# 				assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

	def testPTPutcfromtimestamp(self):
		x0 = ptptime.ptptime(1970,1,1,0,0,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		checkAttributes(x1, d)

		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)
		expected = 0
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)
		

		x0 = ptptime.ptptime(1970,1,1,0,1,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1		
		
		x0 = ptptime.ptptime(1970,1,1,0,0,1,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		checkAttributes(x1, d)

		d = {'days': 0, 'seconds': 1, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)
		
		expected = 1
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)

		x0 = ptptime.ptptime(1970,1,1,0,1,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1		

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'days': 0, 'seconds': 60, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)
		
		expected = 60
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)

		x0 = ptptime.ptptime(1970,1,1,1,0,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'days': 0, 'seconds': 3600, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)

		expected = 3600
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)

		x0 = ptptime.ptptime(1970,1,2,0,0,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'days': 1, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)

		expected = 86400
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)

		x0 = ptptime.ptptime(1970,2,1,0,0,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'days': 31, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)

		expected = 2678400
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)

		x0 = ptptime.ptptime(1971,1,1,0,0,0,0,0)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'days': 365, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0}
		checkAttributes(x2, d)

		expected = 31536000
		if not expected == x0.total_seconds:
			assert False, "Incorrect Total Seconds: '{0}' expected '{1}'".format(x0.total_seconds, expected)

		x0 = ptptime.ptptime(1971,2,2,1,1,1,1,1)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		checkAttributes(x1, d)

		d = {'days': 397, 'seconds': 3661, 'microseconds': 1, 'nanoseconds': 1}
		checkAttributes(x2, d)
		x0 = ptptime.ptptime(1971,2,2,1,1,1,1,1001)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		checkAttributes(x1, d)

		d = {'days': 397, 'seconds': 3661, 'microseconds': 2, 'nanoseconds': 1}
		checkAttributes(x2, d)

		x0 = ptptime.ptptime(1971,2,2,1,1,1,999999,1001)
		x1 = ptptime.ptptime.utcfromtimestamp(0)
		x2 = x0 - x1

		if not isinstance(x0, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x0))
		if not isinstance(x1, ptptime.ptptime):
			assert False, "Incorrect Instance type: '{0}'".format(str(x1))
		if not isinstance(x2, ptptime.timedelta):
			assert False, "Incorrect Instance type: '{0}'".format(str(x2))

		d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		checkAttributes(x1, d)

		d = {'days': 397, 'seconds': 3662, 'microseconds': 0, 'nanoseconds': 1}
		checkAttributes(x2, d)
		

	def testPTPTimeCheck(self):
		t = ptptime.ptptime(1970,1,1,0,0,0,0,0)
		if not t.ptp == 0x0000000000000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(1970,1,1,0,0,1,0,0)
		if not t.ptp == 0x0000000100000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(1970,1,1,0,1,0,0,0)
		if not t.ptp == 0x0000003c00000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(1970,1,1,1,0,0,0,0)
		if not t.ptp == 0x00000e1000000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(1970,1,2,0,0,0,0,0)
		if not t.ptp == 0x0001518000000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(1970,2,1,0,0,0,0,0)
		if not t.ptp == 0x0028de8000000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(1971,1,1,0,0,0,0,0)
		if not t.ptp == 0x01e1338000000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		t = ptptime.ptptime(2000,1,1,0,0,0,0,0)
		expected = 0x386d438000000000
		if not t.ptp == expected:
				assert False, "Incorrect PTP value: 0x{0:016x}, expected 0x{1:016x}".format(t.ptp, expected)
		
	def testPTPCreation(self):
		
		d = {'year': 2000, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0, 'leapyear': False}
		
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		
		if not str(t) == "2000-1-1 00:00:00.000000:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		if not t.ptp == 0x386d438000000000:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0, 'leapyear': False}
		
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
		checkAttributes(t, d)
		
		if not str(t) == "1972-11-12 16:24:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		if not t.ptp == 0x0563e7c2075bca00:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		if not t.sbi == 0x04160317cb2434563456:
				assert False, "Incorrect SBI value: '0x{0:020x}'".format(t.sbi)
		if not t.iena == 0x18e296f216c0:
				assert False, "Incorrect IENA value: '0x{0:012x}'".format(t.iena)

# 		x = t.printPTP()
# 		if not x == "0x0563e7c2075bca00":
# 				assert False, "Incorrect printPTP: '0x{0:016x}'".format(t.ptp)
# 		
		d['nanosecond'] = 235
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
		checkAttributes(t, d)

		if not str(t) == "1972-11-12 16:24:34.123456:235":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		if not t.ptp == 0x0563e7c2075bcaeb:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		if not t.sbi == 0x04160317cb2434563456:
				assert False, "Incorrect SBI value: '0x{0:020x}'".format(t.sbi)
		if not t.iena == 0x18e296f216c0:
				assert False, "Incorrect IENA value: '0x{0:012x}'".format(t.iena)
		
		d['nanosecond'] = 123
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],nanosecond=d['nanosecond'])
		checkAttributes(t, d)

		if not str(t) == "1972-11-12 16:24:34.123456:123":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		if not t.ptp == 0x0563e7c2075bca7b:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		if not t.sbi == 0x04160317cb2434563456:
				assert False, "Incorrect SBI value: '0x{0:020x}'".format(t.sbi)
		if not t.iena == 0x18e296f216c0:
				assert False, "Incorrect IENA value: '0x{0:012x}'".format(t.iena)
		

		d['year'] = 2008
		d['leapyear'] = True
		d['nanosecond'] = 0
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], leapyear=d['leapyear'])
		checkAttributes(t, d)
		
		if not str(t) == "2008-11-12 16:24:34.123456:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		
		if not t.ptp == 0x491b0343075bca00:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		if not t.sbi == 0x377303174b2434563456:
				assert False, "Incorrect SBI value: '0x{0:020x}'".format(t.sbi)
		if not t.iena == 0x18e297015900:
				assert False, "Incorrect IENA value: '0x{0:012x}'".format(t.iena)

		d['nanosecond'] = 235
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'], leapyear=d['leapyear'])
		checkAttributes(t, d)

		if not str(t) == "2008-11-12 16:24:34.123456:235":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		if not t.ptp == 0x491b0343075bcaeb:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		if not t.sbi == 0x377303174b2434563456:
				assert False, "Incorrect SBI value: '0x{0:020x}'".format(t.sbi)
		if not t.iena == 0x18e297015900:
				assert False, "Incorrect IENA value: '0x{0:012x}'".format(t.iena)
		
		d['nanosecond'] = 123
		t = ptptime.ptptime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],nanosecond=d['nanosecond'], leapyear=d['leapyear'])
		checkAttributes(t, d)

		if not str(t) == "2008-11-12 16:24:34.123456:123":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		if not t.ptp == 0x491b0343075bca7b:
				assert False, "Incorrect PTP value: '0x{0:016x}'".format(t.ptp)
		if not t.sbi == 0x377303174b2434563456:
				assert False, "Incorrect SBI value: '0x{0:020x}'".format(t.sbi)
		if not t.iena == 0x18e297015900:
				assert False, "Incorrect IENA value: '0x{0:012x}'".format(t.iena)
