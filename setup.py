from setuptools import setup

setup(
    name='ssd-tensorflow',
    version='0.0.1',
    description='TensorFlow implementation of SSD networks',
    long_description=open('README.md', 'rb').read().decode('utf-8')
    author='Paul B.'
    author_email='paulb@example.com'
    url='https://github.com/balancap/SSD-Tensorflow',
    packages=['nets', 'preprocessing', 'notebooks'],
    install_requires=[
        'tensorflow>=0.12',
        'numpy>=1.11.0',
        'matplotlib>=2.2.0',
    ],
    license='',
)
