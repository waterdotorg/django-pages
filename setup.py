from setuptools import setup, find_packages

setup(
    name='django-pages',
    version=__import__('pages').__version__,
    author='Water.org',
    author_email='dev@water.org',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/waterdotorg/django-pages/',
    license='GPL',
    description='An alternative to Django flatpages without the sites '
                'requirement, but with some newer features',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GPL License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.md').read(),
)
