import unittest
import python_repos
class StatusCodeTestCase(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(python_repos.r.status_code, 200)
        
    def test_total_repositories(self):
        self.assertLessEqual(python_repos.response_dict['total_count'], 3350000)

    def test_number_of_items(self):
        self.assertEqual(len(python_repos.repo_dicts), 30)

unittest.main()