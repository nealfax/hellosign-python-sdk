from setuptools import setup
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                'hellosign_python_sdk'))


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hellosign-python-sdk',
      version='0.1.4',
      description="An API wrapper written in Python to interact with \
            HelloSign's API (http://www.hellosign.com)",
      long_description=readme(),
      classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Topic :: Text Processing :: Linguistic',
      ],
      keywords='hellosign python sdk',
      url='https://github.com/minhdanh/hellosign-python-sdk',
      author='Minh Danh',
      author_email='minhdanh@siliconstraits.vn',
      license='MIT',
      packages=['hellosign_python_sdk'],
      install_requires=[
      'requests'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
