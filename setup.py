from setuptools import setup, find_packages

setup(
    name='visible-to-sqlite',
    author='Avner Shanan',
    version='0.1.0',
    description="Convert exported CSV from Visible app to a SQLite DB",
    license="Apache License, Version 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'visible-to-sqlite = visible_to_sqlite.cli:cli',
        ],
    },
)