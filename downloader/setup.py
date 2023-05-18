from setuptools import setup, find_packages


setup(
    name="drs-downloader",
    version="0.0.1",
    long_description_content_type='text/markdown',
    description="Download file data and register metadata with Data Repository Service (DRS) web services",  # noqa
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    packages=find_packages(),
    install_requires=[
        "minio",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'drs-downloader=downloader.main:main'
        ],
    }
)
