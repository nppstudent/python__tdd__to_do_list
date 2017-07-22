from django.test import TestCase

class DummyTest( TestCase ):
	def test_fail_always( self ):
		self.assertEqual( 1 + 1, 3 )
