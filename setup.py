import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='html_from_epub',
    version='0.2.0',
    author='Casper Lehmann',
    author_email='casperlehmann@gmail.com',
    description='Extract html library from Epub file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/casperlehmann/html-from-epub',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'EbookLib',
    ],
    scripts =['bin/html-from-epub'],
)
