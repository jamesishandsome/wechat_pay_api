from setuptools import setup, find_packages

setup(
    name = 'wechat_mini_pay',
    version = '0.0.1',
    keywords='wechat pay',
    description = 'a library for wechat mini program pay',
    license = 'MIT License',
    url = 'https://github.com/jamesishandsome/wechat_pay_api',
    author = 'James Hu',
    author_email = 'me@jameshu.me',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)