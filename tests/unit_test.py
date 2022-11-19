#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import test_case
import floyd_recursive
import floyd_imperative

#Perform unit test for comparing the result between recursive and imperative versions of Floyd's algorithm

class Test_recursive(unittest.TestCase):
      
    def test1(self):
        
        self.assertEqual(floyd_recursive.floyd(test_case.test1), floyd_imperative.floyd(test_case.test1))
                
    def test2(self):
    
        self.assertEqual(floyd_recursive.floyd(test_case.test2), floyd_imperative.floyd(test_case.test2))
               
    def test3(self):
    
        self.assertEqual(floyd_recursive.floyd(test_case.test3), floyd_imperative.floyd(test_case.test3))
               
    def test4(self):
    
        self.assertEqual(floyd_recursive.floyd(test_case.test4), floyd_imperative.floyd(test_case.test4))
                
    def test5(self):
    
        self.assertEqual(floyd_recursive.floyd(test_case.test5), floyd_imperative.floyd(test_case.test5))
        
    def test6(self):
    
        self.assertEqual(floyd_recursive.floyd(test_case.test6), floyd_imperative.floyd(test_case.test6))
                
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:





# In[ ]:




