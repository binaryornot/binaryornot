from invoke import task, run

@task
def clean():
    run("rm -rf docs/_build")

@task('clean')
def build():
    run("sphinx-build docs docs/_build")
