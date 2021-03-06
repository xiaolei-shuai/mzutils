import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mzutils',
    version='0.1305',
    author="Mohan Zhang",
    author_email="mohan.zhang.mz@gmail.com",
    description="A Mohan Zhang's utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mohan-Zhang-u/mzutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy'
    ]
    # std lib: 'os','shutil','time','codecs'
)
