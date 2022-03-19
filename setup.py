import setuptools

setuptools.setup(
	name='apple-health-exporter',
	version='1.0.0',
	author='Milind Ganjoo',
	author_email='milind.ganjoo@gmail.com',
	description='Python script to export Apple Health dump file to a data frame for analysis.',
	long_description="""
# Apple Health Data Exporter

This Python 3 script takes a dump of Apple Health data (the `export.zip` file
generated through an Apple Health data export) and saves a subset of fields and
records to a [feather](https://github.com/wesm/feather) file. This can then be
read by both Python and R.
	""",
	long_description_content_type="text/markdown",
	url='https://github.com/mganjoo/apple-health-exporter',
	project_urls = {
		"Bug Tracker": "https://github.com/mganjoo/apple-health-exporter/issues"
	},
	license='MIT',
	packages=['apple_health_exporter'],
	package_dir={'.':''},
	scripts=['apple_health_exporter/export.py'],
	install_requires=['numpy','pandas','pyarrow','python-dateutil','pytz','six'.'lxml'],
)




