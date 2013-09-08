from invoke import task, run

@task
def clean_docs():
    run("rm -rf docs/_build")

@task('clean_docs')
def docs():
    run("sphinx-build docs docs/_build")
    run("open docs/_build/index.html")
