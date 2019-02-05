import setuptools

with open("README.md", "r") as file_header:
    long_description = file_header.read()

setuptools.setup(
    name='k2-connect-python',
    version='0.0.1',
    author='Philip Wafula',
    author_email='philipwafula2@gmail.com',
    description='A python SDK to connect to Kopo Kopo',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ThePhilosopherCodes/k2-connect-python',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)