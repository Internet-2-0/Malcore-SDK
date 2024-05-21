from setuptools import find_packages, setup

from msdk.lib.settings import MSDK_VERSION


setup(
    name="msdk",
    packages=find_packages(),
    version=MSDK_VERSION,
    description="SDK for Malcore API",
    author="Thomas Perkins",
    author_email="contact@malcore.io",
    install_requires=["requests==2.32.0"],
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Internet-2-0/Malcore-SDK"
)
