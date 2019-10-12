import unittest
from models import sources,articles

Sources = sources.Sources
articles = articles.Articles

class SourcesTest(unittest.TestCase):
    
    '''
    Test class to tedt the behaviour of the news class
    
    '''
    def setUp(self):
        
        '''
        Set up method that will run before every Test
        
        '''
        
        self.new_sources = Sources('nbc-news','NBC NEWS','Eliud Kipchoge breaks a record','nbcnews.com','general','USA','eng')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))
        
        
        
        
if __name__ == '__main__':
    unittest.main()
        
    
    

