from time import sleep   #Import statement bringing in a function from the time module allowing the pausing of a program.
from selenium import webdriver #Import statement bringing in the module facilitating the webscraping

'''The overall goal of this webscraping program was to download excel files containing health data for the years 2014-2018 for all fifty states. It is composed of two functions.
The first creates a list of lists containing the lower case version of the state names found in state_names and the html anchors used to find the xpaths for each excel download.
The second function uses the created list of lists to find the link to these files and clicks that link to download the files. In addition,this program is designed to be run from the command line.
'''

state_names = [ 'Alabama', 'Alaska' ,'Arizona', 'Arkansas', 'California' , 'Colorado', 'Connecticut' ,'Delaware' , 'Florida' , 'Georgia', 'Hawaii','Idaho','Illinois',
'Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri',
'Montana', 'Nebraska', 'Nevada', 'New-Hampshire', 'New-Jersey' , 'New-Mexico' ,'New-York' ,'North-Carolina', 'North-Dakota', 'Ohio',
'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode-Island', 'South-Carolina', 'South-Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
'Virginia', 'Washington', 'West-Virginia', 'Wisconsin', 'Wyoming'] # Here is a list of the fifty state names to be used in the html anchors and website URL. 

xpath_list = [] #This is the master list which will contain a list of every state's lower case name and html anchors for that state's Excel files 

def xpath_collection():

	'''
	This function creates a list of lists containing the lower case version of the state names found in state_names and the html anchors used to find the xpaths for each excel download.

	Here is an example sublist: [alabama, '//a[@title="2018 County Health Rankings Alabama Data - v3.xls"]', '//a[@title="2017 County Health Rankings Alabama Data - v2.xls"]',
	'//a[@title="2016 County Health Rankings Alabama Data - v3.xls"]', '//a[@title="2015 County Health Rankings Alabama Data - v3.xls"]','//a[@title="2014 County Health Rankings Alabama Data - v6.xls"]' ]

	The first string is inputed into driver.get() in the second function to open the webpage containing the data. The next five strings are then used to find the xpaths to the download buttons for 
	each Excel sheet. After being found, these buttons are then clicked.
	'''

	global xpath_list

	for state in state_names:

		lower_state=state.lower() #Notice that the state names are made lowercase, such as "alabama" from "Alabama". This is because the URLs for each state's data requires this string to be lower case.

		state = state.replace("-"," ") #Notice that any dashes in the state names are removed, such as "New Mexico" from "New-Mexico". This is because the URLs for each state's data requires dashes
		# while the html anchors do not.


		data_link = [lower_state,'//a[@title="2018 County Health Rankings {} Data - v3.xls"]'.format(state)
		  ,'//a[@title="2017 County Health Rankings {} Data - v2.xls"]'.format(state)
		  ,'//a[@title="2016 County Health Rankings {} Data - v3.xls"]'.format(state)
		  ,'//a[@title="2015 County Health Rankings {} Data - v3.xls"]'.format(state)
		  ,'//a[@title="2014 County Health Rankings {} Data - v6.xls"]'.format(state)]

		xpath_list.append(data_link) # Here we are appending the new created sublist to the master list, xpath_list.


def data_collection():

	''' 
	This function uses the list of lists created in the previous function to find the xpaths leading to the download buttons. These buttons are then clicked to download the desired Excel sheets.
	'''

	driver = webdriver.Firefox() # Opens a Firefox browser page

	for ind, data in enumerate(xpath_list): #enumerate() provides the individual lists and their indexes 

		 driver.get('https://www.countyhealthrankings.org/app/{}/2019/downloads'.format(data[0])) #Opens the specific webpage for each state's data

		 download = driver.find_element_by_xpath(data[1]) #Uses the html tag in the sublist to find the download button for each Excel file
		 download.click() # This presses the download button

		 if ind == 0:  #This if statement pauses the for loop on its first iteration for five seconds. This pause is used to click a popup that comes up after the first download button is pressed.
		 	sleep(5)	

		 download = driver.find_element_by_xpath(data[2])
		 download.click()

		 download = driver.find_element_by_xpath(data[3])
		 download.click()

		 download = driver.find_element_by_xpath(data[4])
		 download.click()

		 download = driver.find_element_by_xpath(data[5])
		 download.click()

	driver.close()	#Closes the Firefox browser 


if __name__ == '__main__': #This statement allows the program to be used from the command line. 

	xpath_collection()
	data_collection()
	