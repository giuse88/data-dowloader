.PHONY: test test-register test-release register release

test:
	@python3 -m unittest discover -s ./duka/tests -p "test_*"

test-register:
	python setup.py register -r pypitest

test-release: test-register
	python setup.py sdist upload -r pypitest

register:
	python setup.py register -r pypi

release: register
	python setup.py sdist upload -r pypi
