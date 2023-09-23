import setuptools
#
# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='functions',
    version='0.0.3',
    author='Kushal Hedaoo',
    author_email='kushalhedaoo29@gmail.com',
    description='Simple functioning calculator',

    url='https://github.com/mike-huls/toolbox',

    license='MIT',
    packages=['functions'],
    install_requires=['numpy','pandas'],
)
