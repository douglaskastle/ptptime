# -*- coding: utf-8 -*-
import units.database as database
import os
import sys
import shutil
import datetime
import unittest

def checkUnit(unit, c, verified=0, magnitude=0):
	c['verified']  = verified
	c['magnitude'] = magnitude
	for k in c.keys():
		ret_val = getattr(unit, k)
		if not c[k] == ret_val:
			assert False, "Wrong value returned: {0} : {1}".format(c[k], ret_val)

class TestPtptime(unittest.TestCase):
	
	def setUp(self):
		self.workdir = "./nose_temp"
		os.mkdir(self.workdir)

	def tearDown(self):
		shutil.rmtree(self.workdir)

	def test_b(self):
		assert 'b' == 'b'

# 	def testFileCreation(self):
# 		workdir = self.workdir
# 		dbname = 'units'
# 		dbfile = '{0}/{1}_{2}.sqlite'.format(workdir, dbname, sys.version_info[0])
# 		if os.path.isfile(dbfile):
# 			assert False, "File present: {0}".format(dbfile)
# 	
# 		session = database.setupDB(workdir, dbname)
# 		session.close()
# 
# 		if not os.path.isfile(dbfile):
# 			assert False, "File missing: {0}".format(dbfile)
# 
# 	def testUnitAdd(self):
# 		workdir = self.workdir
# 		dbname = 'units'
# 		dbfile = '{0}/{1}_{2}.sqlite'.format(workdir, dbname, sys.version_info[0])
# 		session = database.setupDB(workdir, dbname)
# 		session.close()
# 		
# 		res = session.query(database.Units).all()
# 		if not 0 == len(res):
# 			assert False, "Incorrect number of values returned: {0}".format(res)
# 	
# 		c = {}
# 		c['device'] = '10.149.8.49'
# 		c['amount'] = 19.0
# 		c['unit'] = 'C'
# 		c['datetime'] = datetime.datetime.now()
# 	
# 		database.addUnit(session, c)
# 
# 		res = session.query(database.Units).all()
# 		if not 1 == len(res):
# 			assert False, "Incorrect number of values returned: {0}".format(res)
# 	
# 		unit = res[0]
# 		checkUnit(unit, c)
# 			
# 		# Remove the unit we just added
# 		database.removeUnit(session, unit)
# 
# 		# Database should now be empty.
# 		res = session.query(database.Units).all()
# 		if not 0 == len(res):
# 			assert False, "Incorrect number of values returned: {0}".format(res)
# 
# 		c['datetime'] = datetime.datetime.now()
# 		database.addUnit(session, c)
# 		c['datetime'] = datetime.datetime.now()
# 		database.addUnit(session, c)
# 		
# 		res = session.query(database.Units).all()
# 		if not 2 == len(res):
# 			assert False, "Incorrect number of values returned: {0}".format(res)
# 
# 		database.removeUnit(session, res)
# 
# 		res = session.query(database.Units).all()
# 		if not 0 == len(res):
# 			assert False, "Incorrect number of values returned: {0}".format(res)
# 
# 		c['datetime'] = datetime.datetime.now()
# 		database.addUnit(session, c)
# 		# We fetch now to use later
# 		res = session.query(database.Units).all()
# 
# 		# This code should trigger an exception
# 		self.assertRaises(Exception, database.removeUnit, session, 5)
# 
# 		# This code effectively does the above, just not as tidy
# 		# Keep here as an example, for now
# 		exception_check = False
# 		try:
# 			database.removeUnit(session, 5)
# 		except Exception:
# 			exception_check = True
# 		assert exception_check, "Exception was not raised as expected"
# 
# 		database.removeUnit(session, res[0])
# 		
# 		# This code should trigger an exception as we attepmt
# 		# to delete a value that was there but is now gone
# 		self.assertRaises(Exception, database.removeUnit, session, res[0])
# 
# 		c['datetime'] = datetime.datetime.now()
# 		database.addUnit(session, c)
# 	
# 		# This code should trigger an exception as we attepmt
# 		# to write the same value twice
# 		self.assertRaises(Exception, database.addUnit, session, c)
# 	
# 	def testUnitDeltaTrue(self):
# 		workdir = self.workdir
# 		dbname = 'units'
# 		dbfile = '{0}/{1}_{2}.sqlite'.format(workdir, dbname, sys.version_info[0])
# 		session = database.setupDB(workdir, dbname, delta=True)
# 		session.close()
# 		
# 		d = '10.149.8.49'
# 		t = datetime.datetime.now()
# 		
# 		c = []
# 		c.append({'device': d, 'amount': 19.0, 'unit': 'C',  'datetime': t})
# 		c.append({'device': d, 'amount': 50.0, 'unit': 'Hz', 'datetime': t})
# 		c.append({'device': d, 'amount': 19.0, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=1)})
# 		c.append({'device': d, 'amount': 51.0, 'unit': 'Hz', 'datetime': t + datetime.timedelta(seconds=1)})
# 		c.append({'device': d, 'amount': 51.0, 'unit': 'Hz', 'datetime': t + datetime.timedelta(seconds=2)})
# 		c.append({'device': d, 'amount': 19.3, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=3)})
# 		c.append({'device': d, 'amount': 19.1, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=2)})
# 		c.append({'device': d, 'amount': 52.0, 'unit': 'Hz', 'datetime': t + datetime.timedelta(seconds=3)})
# 		c.append({'device': d, 'amount': 19.3, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=4)})
# 		
# 		database.addUnit(session, c[0])
# 		database.addUnit(session, c[1])
# 		database.addUnit(session, c[2])
# 		database.addUnit(session, c[3])
# 		database.addUnit(session, c[4])
# 		database.addUnit(session, c[5])
# 		database.addUnit(session, c[6])
# 		database.addUnit(session, c[7])
# 		database.addUnit(session, c[8])
# 		
# 		res = session.query(database.Units).filter(database.Units.unit=='C').all()
# 		res = sorted(res, key=lambda u: u.datetime)
# 
# 		checkUnit(res[0], c[0])
# 		checkUnit(res[1], c[6])
# 		checkUnit(res[2], c[5])
# 
# 		res = session.query(database.Units).filter(database.Units.unit=='Hz').all()
# 		res = sorted(res, key=lambda u: u.datetime)
# 
# 		checkUnit(res[0], c[1])
# 		checkUnit(res[1], c[3])
# 		checkUnit(res[2], c[7])
# 
# 	def testUnitDeltaFalse(self):
# 		workdir = self.workdir
# 		dbname = 'units'
# 		dbfile = '{0}/{1}_{2}.sqlite'.format(workdir, dbname, sys.version_info[0])
# 		session = database.setupDB(workdir, dbname, delta=False)
# 		session.close()
# 		
# 		d = '10.149.8.49'
# 		t = datetime.datetime.now()
# 		
# 		c = []
# 		c.append({'device': d, 'amount': 19.0, 'unit': 'C',  'datetime': t})
# 		c.append({'device': d, 'amount': 50.0, 'unit': 'Hz', 'datetime': t})
# 		c.append({'device': d, 'amount': 19.0, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=1)})
# 		c.append({'device': d, 'amount': 51.0, 'unit': 'Hz', 'datetime': t + datetime.timedelta(seconds=1)})
# 		c.append({'device': d, 'amount': 51.0, 'unit': 'Hz', 'datetime': t + datetime.timedelta(seconds=2)})
# 		c.append({'device': d, 'amount': 19.3, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=3)})
# 		c.append({'device': d, 'amount': 19.1, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=2)})
# 		c.append({'device': d, 'amount': 52.0, 'unit': 'Hz', 'datetime': t + datetime.timedelta(seconds=3)})
# 		c.append({'device': d, 'amount': 19.3, 'unit': 'C',  'datetime': t + datetime.timedelta(seconds=4)})
# 		
# 		database.addUnit(session, c[0])
# 		database.addUnit(session, c[1])
# 		database.addUnit(session, c[2])
# 		database.addUnit(session, c[3])
# 		database.addUnit(session, c[4])
# 		database.addUnit(session, c[5])
# 		database.addUnit(session, c[6])
# 		database.addUnit(session, c[7])
# 		database.addUnit(session, c[8])
# 		
# 		res = session.query(database.Units).filter(database.Units.unit=='C').all()
# 		res = sorted(res, key=lambda u: u.datetime)
# 
# 		checkUnit(res[0], c[0])
# 		checkUnit(res[1], c[2])
# 		checkUnit(res[2], c[6])
# 		checkUnit(res[3], c[5])
# 		checkUnit(res[4], c[8])
# 
# 		res = session.query(database.Units).filter(database.Units.unit=='Hz').all()
# 		res = sorted(res, key=lambda u: u.datetime)
# 
# 		checkUnit(res[0], c[1])
# 		checkUnit(res[1], c[3])
# 		checkUnit(res[2], c[4])
# 		checkUnit(res[3], c[7])
# 
# 	def testUpdateVerify(self):
# 		workdir = self.workdir
# 		dbname = 'units'
# 		dbfile = '{0}/{1}_{2}.sqlite'.format(workdir, dbname, sys.version_info[0])
# 		session = database.setupDB(workdir, dbname)
# 		session.close()
# 		
# 		c = {}
# 		c['device'] = '10.149.8.49'
# 		c['amount'] = 19.0
# 		c['unit'] = 'C'
# 		c['datetime'] = datetime.datetime.now()
# 		
# 		database.addUnit(session, c)
# 
# 		u = session.query(database.Units).all()[0]
# 		checkUnit(u, c, verified=0)
# 		
# 		database.unitVerified(session, u)
# 		u = None
# 		
# 		u = session.query(database.Units).all()[0]
# 		checkUnit(u, c, verified=1)
# 
# 		d = {}
# 		d['device'] = '10.149.8.49'
# 		d['amount'] = 19.0
# 		d['unit'] = 'C'
# 		d['datetime'] = datetime.datetime.now()
# 		database.addUnit(session, d)
# 		
# 		res0 = database.getByVerified(session)
# 		if not 1 == len(res0):
# 			assert False, "Incorrect number of values returned: {0}".format(res0)
# 		u = res0[0]
# 		checkUnit(u, d, verified=0)
# 		
# 		res1 = session.query(database.Units).all()
# 		if not 2 == len(res1):
# 			assert False, "Incorrect number of values returned: {0}".format(res1)
# 		checkUnit(res1[0], c, verified=1)
# 		checkUnit(res1[1], d, verified=0)
# 		
# 		res0 = database.getByVerified(session, verified=1)
# 		if not 1 == len(res0):
# 			assert False, "Incorrect number of values returned: {0}".format(res0)
# 		u = res0[0]
# 		checkUnit(u, c, verified=1)
# 		
# 		database.removeUnit(session, res0)
# 		
# 		res0 = session.query(database.Units).all()
# 		if not 1 == len(res0):
# 			assert False, "Incorrect number of values returned: {0}".format(res0)
# 		checkUnit(res0[0], d, verified=0)
# 
# # # def testUnitEnum():
# # # 	global workdir
# # # 	dbname = 'units'
# # # 	dbfile = '{0}/{1}_{2}.sqlite'.format(workdir, dbname, sys.version_info[0])
# # # 	session = database.setupDB(workdir, dbname)
# # # 	session.close()
# # # 
# # # 	c = {}
# # # 	c['device'] = '10.149.8.49'
# # # 	c['amount'] = 19.0
# # # 	c['unit'] = 'C'
# # # 	c['datetime'] = datetime.datetime.now()
# # # 	u = database.addUnit(session, c)
# # # 	
# # # 	c['unit'] = 'Hz'
# # # 	u = database.addUnit(session, c)
# # # 	
# # # 	c['unit'] = 'elephant'
# # # 	# This code should trigger an exception as we attepmt
# # # 	# to write a value with a unknown unit
# # # 	exception_check = False
# # # 	try:
# # # 		u = database.addUnit(session, c)
# # # 	except Exception:
# # # 		exception_check = True
# # # 	assert exception_check, "Exception was not raised as expected"
# # # 
# # # testUnitEnum.setUp = setup_test
# # # testUnitEnum.tearDown = cleanup_after_test
