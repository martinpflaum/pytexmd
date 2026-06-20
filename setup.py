from setuptools import setup, find_packages
import os

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    install_requires = f.read().splitlines()

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytexmd',
    version='1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Martin Pflaum',
    author_email='contact@martinpflaum.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.14',
    entry_points={
        'console_scripts': [
            'pytexmd=pytexmd.cli:main',
        ],
    },
)
