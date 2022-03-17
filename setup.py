import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='Apple Health Exporter',
    version='1.0.0',
    author='Milind Ganjoo',
    author_email='milind.ganjoo@gmail.com',
    description='Python script to export Apple Health dump file to a data frame for analysis.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mganjoo/apple-health-exporter',
    project_urls = {
        "Bug Tracker": "https://github.com/mganjoo/apple-health-exporter/issues"
    },
    license='MIT',
    packages=['apple-health-exporter'],
    install_requires=['numpy','pandas','pyarrow','python-dateutil','pytz','six'],
)




