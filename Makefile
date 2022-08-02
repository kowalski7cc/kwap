init:
	pip install -r requirements.txt
dist:
	python -m build
install:
	pip install .
run:
	python -m kwap
uninstall:
	pip uninstall kwap