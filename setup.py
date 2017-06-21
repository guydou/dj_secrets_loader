from setuptools import setup

setup(
    name='dj-secrets-loader',
    version='0.0.5',
    url='https://github.com/guydou/dj_secrets_loader',
    license='BSD',
    author='Guy Doulberg',
    author_email='guydou@gmail.com',
    description='Load docker based secrets to settings',
    long_description=__doc__,
    py_modules=['dj_secrets_loader'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
