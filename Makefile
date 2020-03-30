deploy-pypi:
	twine check dist/*
	rm -rf dist
	python setup.py sdist
	twine upload dist/*
