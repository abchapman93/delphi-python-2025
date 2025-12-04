from setuptools import setup, find_packages
import os


# function to recursively get files for resourcee
def package_files(directory):
   paths = []
   for (p, directories, filenames) in os.walk(directory):
      for filename in filenames:
         paths.append(os.path.join("..", p, filename))
   return paths



setup(
   name='uu_delphi_python_dec25',
   version='0.3',
   description='Python package to help with DELPHI Cecember 2025 Python workshop.',
   author='Alec Chapman',
   author_email='abchapman93@gmail.com',
   packages=["uu_delphi_python_dec25", "uu_delphi_python_dec25.quizzes"],  #same as name
   package_dir={"uu_delphi_python_dec25": "uu_delphi_python_dec25",
                "uu_delphi_python_dec25.quizzes": "uu_delphi_python_dec25/quizzes"},
   install_requires=['jupyter', 'numpy', 'pandas'], #external packages as dependencies
)