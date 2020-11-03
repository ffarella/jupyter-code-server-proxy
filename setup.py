import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-code-server-proxy",
    version='0.1.0',
    url="https://github.com/ffarella/jupyter-code-server-proxy",
    author="ffarella",
    description="",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'code-server'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-code-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'code-server = jupyter_code_server_proxy:setup_code_server',
        ]
    },
    package_data={
        'jupyter_code_server_proxy': ['icons/*'],
    },
)
