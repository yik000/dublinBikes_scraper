from setuptools import setup

setup(
    name="dbikesScraper",
    version="0.1",
    description="Data scraper for dublin bikes API",
    author="Conor Kiy",
    author_email="conorkiy@gmail.com",
    install_requires=[],
    packages=['dbikesScraper'],
    entry_points={
        'console_scripts':['dbikesScraper=dbikesScraper.main:main']
        }
    )