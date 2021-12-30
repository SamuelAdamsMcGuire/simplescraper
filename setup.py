from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="samssimplescraper",  
    version="0.1.2",
    description="tool to help scrape sitemaps and the links they scrape",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Samuel McGuire",
    author_email="samuelmcguire@engineer.com",
    packages=["samssimplescraper"], 
    url="https://github.com/samueladamsmcguire/simplescraper", 
    license="MIT",
    install_requires=['beautifulsoup4', 
                        'tqdm'
                        ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)
