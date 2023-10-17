.PHONY: install test clean

# Install each package. You'll need to add a similar line for each package.
install:
	python -m task_scheduling.graph_gen

# Run tests
test:
    python -m unittest discover -s . -p 'test_*.py'

# Clean the project directory (optional)
clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +