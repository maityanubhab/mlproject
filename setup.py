from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(  
name = "mlproject",
version = "0.0.1",
author = "maityanubhab",
author_email = "maityanubhab39@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)


"""code explanation
1 `from setuptools import find_packages, setup`: This line imports 
    the `find_packages` and `setup` functions from the `setuptools` package.

2 `HYPEN_E_DOT = '-e .'`: This is a constant that defines the string "-e .".

3 `def get_requirements(file_path:str)->List[str]:`: This is a function 
    that takes a file path as input and returns a list of requirements. It
     reads the requirements from the specified file, removes any trailing newline 
     characters, and removes the "-e ." string if it is present in the requirements list.

4 `setup(`: This line starts the setup function call to define the Python package.

5 `name` = `"mlproject",`: This line sets the name of the package.

6 `version = "0.0.1",`: This line sets the version number of the package.

7 `author = "maityanubhab",`: This line sets the author name of the package.

8 `author_email = "maityanubhab39@gmail.com",`: This line sets the email address of the author.

9 `packages = find_packages(),`: This line uses the `find_packages` function to 
    automatically discover all packages that need to be included in the distribution.
     It searches for all packages in the current directory and its subdirectories that 
     contain an `__init__.py` file.

10 `install_requires = get_requirements('requirements.txt')`: This line specifies 
    the package's dependencies. It uses the `get_requirements` function to read 
    the dependencies from the `requirements.txt` file and returns them as a list.

)`: This line ends the setup function call."""