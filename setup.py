from setuptools import find_packages, setup


def get_requirements(path: str) -> list:
    """
        return list of requirements
    """
    with open(path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="Machine_Learning_Project",
    version="0.0.1",
    author="Rushikesh",
    author_email="alvis.jackson29@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('reqs.txt')

)
