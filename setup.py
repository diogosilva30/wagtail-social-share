import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wagtail-social-share",
    version="0.1.4",
    author="Diogo Silva",
    author_email="diogosilv30@gmail.com",
    description="Auto-share Wagtail Pages on Social Medias",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/spamz23/wagtail-social-share",
    install_requires=open("requirements.txt").readlines(),
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
