from setuptools import setup, find_packages


VERSION = "0.0.1"


# Runtime dependencies. See requirements.txt for development dependencies.
DEPENDENCIES = [
    "psycopg2-binary",
    "SQLAlchemy"
]


setup(
    name='data_scrapper',
    version=VERSION,
    description='Collect ohlcv data',
    author='Dragos Iacomi',
    author_email='biofreack@gmail.com',
    url='github.com',
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    keywords=[],
    classifiers=[],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "datascr = data_scrapper.__main__:main",
        ],
    }
)

