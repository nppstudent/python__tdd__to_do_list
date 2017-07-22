"""
This is our first test!
It can be used to test if the web server provided by Django is up and running on http://localhost:8000.

It requires that you have the selenium python package installed:
	sudo pip3 install --upgrade selenium
And the geckodriver in your PATH.

In order to have this test pass, you need to install Django:
	sudo pip3 install django
Then create a Django project:
	django-admin.py startproject my_project
Then go to the project's directory:
	cd my_project
Then start Django's web server:
	python3 manage.py runserver
Then run this test!
"""
from selenium import webdriver
import unittest

class NewVisitorTest( unittest.TestCase ):
	def setUp( self ):
		self.browser = webdriver.Firefox()
		self.browser.implicitely_wait( 3 ) # Gives 3 seconds for content to load before starting to fail tests!

	def tearDown( self ):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later( self ):		
		self.browser.get( 'http://localhost:8000' )

		self.assertIn( 'To-Do', self.browser.title )

		self.fail( 'This test is not entirely written yet!' )

if __name__ == '__main__':
	unittest.main()
