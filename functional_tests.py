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
		self.browser.implicitly_wait( 3 ) # Gives 3 seconds for content to load before starting to fail tests!

	def tearDown( self ):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later( self ):
		# User comes visit our homepage
		self.browser.get( 'http://localhost:8000' )

		# She notices the page's title mentionning to-do lists
		self.assertIn( 'To-Do lists', self.browser.title )

		self.fail( 'This test is not entirely written yet!' )

		# She is invited to enter a to-do item right away

		# She types "Buy peacock feathers" into a text box

		# When she hits enter, the page updates, and now comports a list with one item: "1: Buy peacock feathers"

		# There is still a text box inviting her to enter another item. She enters "Use peacock feather to make a fly"

		# The page updates and now comports a list with two items: "1: Buy peacock feathers" and "2: Use peacock feather to make a fly"

		# She wonders whether the site will remember her list. She then notices that the page displays a special URL for her to access her to-do list.

		# She visits that URL. Her list is still there.

if __name__ == '__main__':
	unittest.main()
