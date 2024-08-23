from setuptools import find_packages, setup
from typing import List

HYPEN_e='-e .'

def get_requirements(file_path:str)->List[str]:
    '''This Function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]

        if HYPEN_e in requirements:
            requirements.remove(HYPEN_e)
    return requirements



setup(
name='MLProject',
version='0.0.1',
author='Komal',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn'] WHat if you have 100s fo such packages?
install_requires=get_requirements('requirements.txt')


)