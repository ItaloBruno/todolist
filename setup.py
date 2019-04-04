"""
    Neste arquivo temos todas informações relacionadas com esta API
"""

from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api Python Flask todolist'
__long_description__ = 'Esta é uma API de uma aplicação todolist feita com o framework web Python chamado Flask'

__author__ = 'Italo Bruno'
__author_email__ = 'italo.silva@alunos.ifce.edu.br'

setup(
    name='api-todolist',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    # license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/ItaloBruno/todolist.git',
    keywords='API, Flask, MongoDB',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # 'Intended Audience :: Developers',
        # 'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'License :: OSI Approved :: MIT License',
    ],
)