from setuptools import setup, find_packages

setup(
    include_package_data=True,
    name='mandrill_tornado',
    author="Aaron France",
    author_email="aaron.l.france@gmail.com",
    version='1.8.44',
    description="Async client for Mandrill",
    packages=find_packages(),
)
