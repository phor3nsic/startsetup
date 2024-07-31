from setuptools import setup, find_packages

setup(
    name='startsetup',
    version='0.1',
    packages=find_packages(),
    install_requires=[], 
    entry_points={
        'console_scripts': [
            'startsetup=startsetup.main:main',
        ],
    },
    author='Walleson Rodrigues',
    author_email='phorensic@pm.me',
    description='Start your setup.py enviroment',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/phor3nsic/startsetup',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
