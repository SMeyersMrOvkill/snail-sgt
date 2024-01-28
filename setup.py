from setuptools import setup

setup(
    name="snail-sgt",
    version="1.0",
    description="A package for communicating with Microsoft Phi 2 over the Together Computer Serverless Inferene API.",
    author="Samuel L Meyers",
    author_email="sam@samuellmeyers.com",
    url="https://github.com/SMeyersMrOvkill/snail-sgt",
    packages=["snail_sgt"],
    install_requires=["requests"],
)
