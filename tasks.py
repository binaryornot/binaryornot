from invoke import task, run

@task
def clean_docs():
    run("rm -rf docs/_build")

@task('clean_docs')
def docs():
    run("sphinx-build docs docs/_build")
    run("open docs/_build/index.html")

@task
def flake8():
    run("flake8 binaryornot tests")

@task
def autopep8():
    run("autopep8 --in-place --aggressive -r binaryornot")
    run("autopep8 --in-place --aggressive -r tests")

@task
def test():
    run("python setup.py test")

@task
def coverage():
	run("coverage run --source binaryornot setup.py test")
	run("coverage report -m")
	run("coverage html")
	run("open htmlcov/index.html")
