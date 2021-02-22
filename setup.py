from setuptools import setup

setup(
    name="dbikes_scraper",
    version="0.2",
    description="Data scraper for dublin bikes API",
    author="Conor Kiy",
    author_email="conorkiy@gmail.com",
    licence = "GPL3",
    install_requires=['requests','sqlalchemy','mysqlclient'],
    packages=['dbikesScraper'],
    entry_points={
        'console_scripts':['dbikes_scraper=dbikesScraper.main:main']
        }
    )
