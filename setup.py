# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup

setup(
        name='vihaclient',     # 包名字
        version='0.0.2',   # 包版本
        description='Client for Home Assistant',   # 简单描述
        author='ChenJiashu',  # 作者
        author_email='tech_support@aiblockly.com',  # 作者邮箱
        url='https://www.aiblockly.com',      # 包的主页
        packages=['vihaclient','vihaclient.Core','vihaclient.Utils'],                 # 包
        install_requires=["pyyaml_include >=1.2","requests"]
)