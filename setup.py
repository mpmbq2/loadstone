from setuptools import setup

version = '0.0.1'

setup(
    name='loadstone',
    version=version,
    description='cli to setup PySpark + Jupyter on a EC2 cluster with Spark setup by flintrock',
    long_description='See https://github.com/mpmbq2/loadstone',
    author='jwittenbach',
    author_email='mpmbq2@gmail.com',
    url='https://github.com/mpmbq2/loadstone',
    install_requires=open('requirements.txt').read().split('\n'),
    entry_points='''
        [console_scripts]
        loadstone=loadstone:cli
        '''
)
