'''
Created on Aug 5, 2018

@author: aph17
'''

class Automobile(object):
    '''
    classdocs
    '''


    def __init__(self, year, brand, model):
        '''
        Constructor
        '''
        self.year = year
        self.brand = brand
        self.model = model
        
    def describe_myself(self):
        print ('This is my car')
        print ("This is a" +" " + str(self.year) + self.brand + self.model)
        