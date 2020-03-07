import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="defKey",
    version="1.0.1",
    author="Riley/a11ce",
    author_email="a11ce@protonmail.com",
    description="Non-blocking keybinds using threads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a11ce/defKey",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)