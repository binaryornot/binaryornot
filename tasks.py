from invoke import task, run


@task
def clean_docs():
    run("rm -rf docs/_build")
    run("rm -rf docs/binaryornot.rst")
    run("rm -rf docs/modules.rst")


@task('clean_docs')
def docs():
    run("sphinx-apidoc -o docs/ binaryornot/")
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


@task
def clean_build():
    run("rm -fr build/")
    run("rm -fr dist/")
    run("rm -fr *.egg-info")


@task
def clean_pyc():
    run("find . -name '*.pyc' -exec rm -f {} +")
    run("find . -name '*.pyo' -exec rm -f {} +")
    run("find . -name '*~' -exec rm -f {} +")


@task('clean_build', 'clean_pyc')
def sdist():
    run("python setup.py sdist")
    run("ls -l dist")


@task('sdist')
def release():
    run("python setup.py upload")
