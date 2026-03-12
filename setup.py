from setuptools import setup, find_packages




setup(
    name="drink-quality-prediction",  # project name
    version="0.0.0",
    author="Shivansh Vyas",
    author_email="shivanshvyas1729@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "python-box==6.0.2",
    "pyYAML",
    "tqdm",
    "ensure==1.0.2",
    "joblib",
    "types-PyYAML",
    "Flask",
    "Flask-Cors",
]
      
)