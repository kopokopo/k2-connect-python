import setuptools

with open("README.md", "r") as file_header:
    long_description = file_header.read()

setuptools.setup(
    name='k2-connect',
    version='0.0.1.dev1',
    author='Philip Wafula',
    author_email='philipwafula2@gmail.com',
    description='A python SDK to connect to Kopo Kopo',
    long_description=long_description,
    python_requires='>=3',
    long_description_content_type='text/markdown',
    url='https://github.com/ThePhilosopherCodes/k2-connect-python',
    license='MIT',
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)