from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='cd4db',  # Required
    version='1.0.0',  # Required
    description='Для сборки и деплоя кода DWH',  # Optional
    author='Evgenii Prusov',  # Optional
    author_email='prusove@gmail.com',  # Optional
    packages=find_packages(where='.'),  # Required
    python_requires='>=3.10, <4',
    entry_points={  # Optional
        'console_scripts': [
            'build=cd4db.build:main',
            'deploy=cd4db.deploy:main'
        ],
    },
)