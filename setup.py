import setuptools

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='abb_robotraconteur_driver2',
    version='0.1.0',
    description='ABB Robot Raconteur Driver v2',
    url='https://github.com/johnwason/abb_robotraconteur_driver2',
    packages=setuptools.find_packages("src"),
    package_dir={"" :"src"},
    install_requires=[
        'RobotRaconteur',
        'RobotRaconteurCompanion',
        'robotraconteur_abstract_robot',
        'numpy',
        'abb_robot_client',
        'abb_motion_program_exec'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)