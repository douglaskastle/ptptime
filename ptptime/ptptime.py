# -*- coding: utf-8 -*-
import datetime
import time

def getLeapYear(t):
	if  t.year <= 1972:
		return 1
	elif t.year >= 1999 or t.year <= 2000:
		return 32
	elif t.year >= 2013 or t.year <= 2016:
		return 35
	else:
		return 0

def intTobcdConvert(a):
	b = 0
	for kw in a:
		b |= int(a[kw]) << int(kw)
	return b

def bcdTointConvert(a):
	b = 0
	i = 0
	while not 0 == a:
		b += (a & 0xf) * (10**i)
		a = a >> 4
		i += 1
	return b

def digitSplit(a, length=4):
	b = []
	for i in range(length):
		b.append((a/10**i)%10)
	return b

class timedelta(datetime.timedelta):
	def __new__(cls, *args, **kwargs):
		nanoseconds = 0
		if 'nanoseconds' in kwargs.keys():
			nanoseconds = kwargs['nanoseconds']
			del kwargs['nanoseconds']
		if not 'microseconds' in kwargs.keys():
			kwargs['microseconds'] = 0
		
		if nanoseconds < 0:
			kwargs['microseconds'] -= 1

		kwargs['microseconds'] += int(nanoseconds/1000.0)
		nanoseconds = nanoseconds%1000
		
		c = super(timedelta, cls).__new__(cls, *args, **kwargs)
		c.nanoseconds = nanoseconds
		
		return c

	@property
	def hour(self):
		return int(self.seconds/3600)

	@property
	def minute(self):
		return int(self.seconds/60)%60

	@property
	def second(self):
		return self.seconds%60

	def __str__(self, *args, **kwargs):
		days = ""
		micros = ""
		nanos = ""
		if not self.days == 0:
			pural = ""
			if abs(self.days) > 1:
				pural = "s"
			days = "{0:d} day{1}, ".format(self.days, pural)
		if not self.microseconds == 0 or not self.nanoseconds == 0:
			micros = ".{0:06d}".format(self.microseconds)
		if not self.nanoseconds == 0:
			nanos = ":{0:03d}".format(self.nanoseconds)
		return "{0}{1:d}:{2:02d}:{3:02d}{4}{5}".format(
		                days,
						self.hour,self.minute,self.second,
						micros, nanos
						)

class ptptime(datetime.datetime):
	def __new__(cls, *args, **kwargs):
		nanosecond = 0
		leapyear   = False
		if len(args) >= 8:
			if isinstance(args[7],int):
				nanosecond = args[7]
				args = args[0:7] + args[8:]
		if 'nanosecond' in kwargs.keys():
			nanosecond = kwargs['nanosecond']
			del kwargs['nanosecond']
		if 'leapyear' in kwargs.keys():
			leapyear = kwargs['leapyear']
			del kwargs['leapyear']
		
		c = super(ptptime, cls).__new__(cls, *args, **kwargs)
		
		c.nanosecond = nanosecond
		c.leapyear   = leapyear
		
		return c
	
	def __str__(self):
		return "{0}-{1}-{2} {3:02d}:{4:02d}:{5:02d}.{6:06d}:{7:03d}".format(
						self.year,self.month,self.day,
						self.hour,self.minute,self.second,
						self.microsecond,self.nanosecond,
						)

	def iena_str(self):
		return "{1}-{2} {3:02d}:{4:02d}:{5:02d}.{6:06d}".format(
						self.year,self.month,self.day,
						self.hour,self.minute,self.second,
						self.microsecond,self.nanosecond,
						)

	def __add__(self, *args, **kwargs):
		td = args[0]
		c = super(ptptime, self).__add__(*args, **kwargs)
		
		nanoseconds = self.nanosecond + td.nanoseconds
		microsecond = c.microsecond + int(nanoseconds/1000.0)
		nanoseconds %= 1000
		
		t = ptptime(c.year, 
					c.month, 
					c.day,
					c.hour,
					c.minute,
					c.second,
					microsecond,
					nanoseconds,
				   )
		return t
	
	def __sub__(self, *args, **kwargs):
		if isinstance(args[0], timedelta):
			td = args[0]
			x = timedelta(days=-td.days, 
						  seconds=-td.seconds, 
						  microseconds=-td.microseconds, 
						  nanoseconds=-td.nanoseconds
						 )
			args = [x]
		elif isinstance(args[0], ptptime):
			t0 = self
			t1 = args[0]
			d0 = datetime.datetime(t0.year,t0.month,t0.day,t0.hour,t0.minute,t0.second)
			d1 = datetime.datetime(t1.year,t1.month,t1.day,t1.hour,t1.minute,t1.second)
			total_seconds = (d0 - d1).total_seconds()
			attr_list = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'nanosecond',)
			b = {}
			for a in attr_list:
				#print a
				b[a] = getattr(self, a) - getattr(args[0], a)
			return timedelta(seconds=total_seconds, 
						     microseconds=b['microsecond'], 
						     nanoseconds=b['nanosecond'],
							)
		else:
			raise Exception

		t = self.__add__(*args, **kwargs)
		return t
	
	def replace(self, *args, **kwargs):
		attr_list = ['year','month','day','hour','minute','second','microsecond','nanosecond']
		new_dict = {}
		for attr in attr_list:
			new_dict[attr] = getattr(self, attr)
		for kw in kwargs:
			if not kw in attr_list:
				raise NameError("Unknown attr: {0}".format(kw))
			new_dict[kw] = kwargs[kw]
		t = ptptime(new_dict['year'], 
					new_dict['month'], 
					new_dict['day'],
					new_dict['hour'],
					new_dict['minute'],
					new_dict['second'],
					new_dict['microsecond'],
					new_dict['nanosecond'],
				   )
		return t
	
	@property
	def total_seconds(self):
		seconds = int((self - ptptime.utcfromtimestamp(0)).total_seconds())
		if isinstance(self.leapyear, int):
			seconds += self.leapyear
		elif self.leapyear:
			seconds += getLeapYear(self)
		return seconds
	
	@property
	def ptp(self):
		ptp     = (self.total_seconds << 32) | ((self.microsecond) * 1000 + self.nanosecond)
		return ptp
	
	@property
	def iena(self):
		t = ptptime(self.year,1,1,0,0,0,0,)
		total_seconds = self.total_seconds - t.total_seconds
		microseconds  = self.microsecond - t.microsecond
		return ((total_seconds * 1000000) + microseconds)
		
	@property
	def sbi(self):
		dow            = self.weekday()
		doy            = self.timetuple().tm_yday
		time_micro     = self.microsecond%10000
		a = digitSplit(time_micro,4)
		sbi_time_micro = intTobcdConvert({12: a[3], 8: a[2], 4: a[1], 0: a[0],})
		time_lo        = self.second*100 + self.microsecond/10000
		a = digitSplit(self.microsecond,2)
		b = digitSplit(self.second,2)
		sbi_time_lo    = intTobcdConvert({12: b[1], 8: b[0], 4: a[1], 0: a[0],})
		time_hi        = self.hour*100 + self.minute
		a = digitSplit(self.minute,2)
		b = digitSplit(self.hour,2)
		sbi_time_hi    = intTobcdConvert({13: dow, 11: b[1], 7: b[0], 4: a[1], 0: a[0],})
		a = digitSplit(doy,4)
		sbi_doy        = intTobcdConvert({12: a[3], 8: a[2], 4: a[1], 0: a[0],})
		sbi_days       = int((self - ptptime.utcfromtimestamp(0)).total_seconds()/(3600*24))

		sbi = 0
		sbi |= (sbi_time_micro & 0xffff)       # time_micro
		sbi |= (sbi_time_lo    & 0xffff) << 16 # time_lo
		sbi |= (sbi_time_hi    & 0xffff) << 32 # time_hi
		sbi |= (sbi_doy        & 0xffff) << 48 # DayOfYr : 001-365/366
		sbi |= (sbi_days       & 0xffff) << 64 # UxDay
		return sbi

	
	def printPTP(self):
		print("0x{0:016x}".format(self.ptp))
	
	def printIENA(self):
		print("0x{0:012x}".format(self.iena))

	def printSBI(self):
		print("0x{0:020x}".format(self.sbi))

def utcfromtimestamp(i):
	x = timedelta(seconds=i)
	return x

def timefromptp(p, leapyear=0):
	total_seconds = (p >> 32)
	t = datetime.datetime.utcfromtimestamp(total_seconds)
	
	if leapyear <= -1:
		total_seconds -= getLeapYear(t)
	else:
		total_seconds -= leapyear
	x = p & 0xffffffff
	#seconds = seconds + x/1000000000.0
	u = int(x/1000)
	t = ptptime.utcfromtimestamp(total_seconds)
	t = t.replace(microsecond=u)
	t.nanosecond = int(x % 1000)
	t.leapyear = leapyear
	return t

def timefromsbi(s, leapyear=False):
	micro   = bcdTointConvert( s        & 0xffffff)
	seconds = bcdTointConvert((s >> 24) & 0xff)
	minutes = bcdTointConvert((s >> 32) & 0x7f)
	hours   = bcdTointConvert((s >> 39) & 0x3f)
	dow     = bcdTointConvert((s >> 45) & 0x7)
	doy     = bcdTointConvert((s >> 48) & 0xffff)
	
	total_seconds = (((s >> 64)*24 + hours)*60 + minutes)*60 + seconds + micro/1000000.0
	t = ptptime.utcfromtimestamp(total_seconds)
	t.nanosecond = 0
	t.leapyear = leapyear
	return t

def timefromiena(i, year=1970):
	t = ptptime.utcfromtimestamp(i/1000000.0+(year-1970)*0x01e13380)
	return t
