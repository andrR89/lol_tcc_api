import pip
from paver.easy import *
from paver.setuputils import setup
from pkg_resources import iter_entry_points
from pip.req import parse_requirements


install_reqs = parse_requirements('requirements-dev.txt', session=pip.download.PipSession())
requirements = [str(ir.req) for ir in install_reqs]

setup(
    name='security-financial-platform',
    packages=[
        'config'
        'controller',
        'domain'
    ],
    install_requires=requirements,
    dependency_links=[
    ],
    version='0.0.1',
    url='http://www.nexxera.com/',
    author='wellington.nukamoto',
    author_email='wellington.nukamoto@nexxera.com'
)

for entry_point in iter_entry_points(group='nexxera.setuputils', name=None):
    entry_point.load()()

@task
def default():
    """
    Run coverage, flake8, pep8, pylint, radon [cc | raw | mi].
    """
    call_task('clean')
    call_task('coverage')
    call_task('flake8')
    call_task('pep8')
    call_task('pylint')
    sh('paver radon -c cc')
    sh('paver radon -c raw')
    sh('paver radon -c mi')
