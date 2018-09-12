from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr_inventory',
    version='0.1.0',
    description='Human Resources inventory software test',
    long_description=readme,
    author='Hako',
    author_email='hamakohako@yahoo.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={'console_scripts': 'hr=hr.cli:main'}
)
