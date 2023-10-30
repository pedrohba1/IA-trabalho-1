.PHONY: install test clean

# Install each package. You'll need to add a similar line for each package.
install:
	pip install -r requirements.txt
# Run tests
# test:
# 	python -m unittest discover -s ./tests -p 'test_*.py' -v

test-scheduler: 
	python -m unittest discover -s ./tests/task_scheduling  -p 'test_*.py' -v

test-sudoku:
	python -m unittest discover -s ./tests/sudoku  -p 'test_*.py' -v
	


# Clean the project directory (optional)
clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
