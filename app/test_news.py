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
        
    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_sources.id,'nbc-news')
        self.assertEqual(self.new_sources.name,'NBC NEWS')
        self.assertEqual(self.new_sources.description,'Eliud Kipchoge breaks a record')
        self.assertEqual(self.new_sources.url,'nbcnews.com')
        self.assertEqual(self.new_sources.category,'general')
        self.assertEqual(self.new_sources.country,'USA')
        self.assertEqual(self.new_sources.language,'eng')
        
        
        
        
if __name__ == '__main__':
    unittest.main()
        
    
    

