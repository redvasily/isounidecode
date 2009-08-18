from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
   os.chdir(root_dir)

package = 'isounidecode'

for dirpath, dirnames, filenames in os.walk(package):
   # Ignore dirnames that start with '.'
   for i, dirname in enumerate(dirnames):
       if dirname.startswith('.'): del dirnames[i]
   if '__init__.py' in filenames:
       pkg = dirpath.replace(os.path.sep, '.')
       if os.path.altsep:
           pkg = pkg.replace(os.path.altsep, '.')
       packages.append(pkg)
   elif filenames:
       prefix = dirpath[len(package) + 1:] # Strip package prefix
       for f in filenames:
           data_files.append(os.path.join(prefix, f))

setup(name='isounidecode',
    version='0.2',
    description='Conversion and transliteration of unicode into ascii or iso-8859-1',
    author='Vasily Sulatskov',
    author_email='redvasily@gmail.com',
    url='http://github.com/redvasily/isounidecode/tree/master',
    download_url='http://cloud.github.com/downloads/redvasily/isounidecode/isounidecode-0.2.tar.gz',
    package_dir={
        package: package,
    },
    packages=packages,
    package_data={
        package: data_files
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Text Processing',
 
    ],
)
