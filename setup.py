from setuptools import setup

if __name__ == '__main__':
  setup(
    name='wonder',
    version='1.0.0',
    author='Tadahiro Yamamura',
    description='Python CLI tool sample.',
    url='https://github.com/TadahiroYamamura/python-cli-tool-sample',
    license='MIT',
    install_requires=['click'],
    packages=['wonder'],
    entry_points={
      'console_scripts': ['wonder = wonder.main:wonder']
    }
  )
