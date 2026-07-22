from setuptools import setup, find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))

# get the dependencies
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' in x]

setup(
    name='pyinquirer-revived',
    version='1.0.6',
    description=(
          'A Python module for collection of common interactive command line user interfaces,'
          ' based on Inquirer.js'
    ),
    license='MIT',
    url='https://github.com/someone-cloud/PyInquirer/',
    python_requires=">=3.8",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: '
        'Libraries :: Application Frameworks',
    ],
    keywords='click, prompt-toolkit, cli, command-line, commandline, command-line-interface, python-inquiry, inquirer',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Zafrul Razeem',
    download_url='https://github.com/someone-cloud/PyInquirer/archive/1.0.4.tar.gz',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='someone-cloud@users.noreply.github.com',
)
