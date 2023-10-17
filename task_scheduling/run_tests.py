# run_tests.py
import unittest

def run():
    # Create a test loader
    loader = unittest.TestLoader()
    
    # Find all tests in the 'tests' directory under the 'task_scheduling' package
    test_suite = loader.discover(start_dir='tests', pattern='test_*.py', top_level_dir='.')
    
    # Run the collected tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

if __name__ == "__main__":
    run()
