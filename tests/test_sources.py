import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('Daily Nation','Nation news','Kipchoge breaks his own record','dailynation.co.ke','general','Kenya','eng')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'Daily Nation')
        self.assertEquals(self.new_source.name,'Nation news')
        self.assertEquals(self.new_source.description,'Kipchoge breaks his own record')
        self.assertEquals(self.new_source.url,'dailynation.co.ke')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'Kenya')
        self.assertEquals(self.new_source.language,'eng')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','lg','Apple manages to grow its business even as iPhone sales decline 12%','Libra is a great idea. But Facebook has to get out of the way','lg.com','lg.com/lg.jpg','2019-06-23')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'lg')
        self.assertEquals(self.new_article.title,'Apple manages to grow its business even as iPhone sales decline 12%')
        self.assertEquals(self.new_article.description,'Libra is a great idea. But Facebook has to get out of the way')
        self.assertEquals(self.new_article.url,'lg.com')
        self.assertEquals(self.new_article.image,'lg.com/lg.jpg')
        self.assertEquals(self.new_article.date,'2019-06-23')
