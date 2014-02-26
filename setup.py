from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

		setup(name='hellosign-python-sdk',
			version='0.1',
			description='An API wrapper written in Python to use with HelloSign\'s API (http://www.hellosign.com)',
			long_description=readme(),
			classifiers=[
			'Development Status :: 3 - Alpha',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 2.7',
			'Topic :: Text Processing :: Linguistic',
			],

			keywords='funniest joke comedy flying circus',
			url='https://github.com/minhdanh/hellosign-python-sdk',
			author='Minh Danh',
			author_email='minhdanh@siliconstraits.vn',
			license='MIT',
			packages=['hellosign-python-sdk'],
			install_requires=[
			'markdown',
			],
			test_suite='nose.collector',
			tests_require=['nose'],

			zip_safe=False)
