import os

def create_project_structure(
        project_name, 
        requirements_file=None, 
        author_name=None, 
        author_email=None, 
        github_user=None
        ):
    
    # Meke the folders
    os.makedirs(f"{project_name}/{project_name}", exist_ok=True)
    
    # Make README.md
    with open(f"{project_name}/README.md", 'w') as f:
        install = f"""\n\n### Install

- via pipx:

```sh
pipx install git+https://github.com/{github_user}/{project_name}
```
- via pip:

```sh
pip install git+https://github.com/{github_user}/{project_name}
```
"""
        f.write(f"# {project_name}\n\nDescription of project{project_name}.{install}")
    
    # Make setup.py
    setup_content = f"""from setuptools import setup, find_packages

setup(
    name='{project_name}',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # requirements.txt
    entry_points={{
        'console_scripts': [
            '{project_name}={project_name}.main:main',
        ],
    }},
    author='{author_name}',
    author_email='{author_email}',
    description='Description of {project_name}.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/{github_user}/{project_name}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
"""
    with open(f"{project_name}/setup.py", 'w') as f:
        f.write(setup_content)
    
    # Make requirements.txt if have
    if requirements_file:
        with open(requirements_file, 'r') as rf:
            requirements = rf.read()
        with open(f"{project_name}/requirements.txt", 'w') as f:
            f.write(requirements)
    else:
        open(f"{project_name}/requirements.txt", 'w').close()

    # Make __init__.py
    open(f"{project_name}/{project_name}/__init__.py", 'w').close()
    
    # Make main.py
    main_content = """def main():
    print("Hello, World!")

if __name__ == '__main__':
    main()
"""
    with open(f"{project_name}/{project_name}/main.py", 'w') as f:
        f.write(main_content)
    
    # Make .gitignore
    gitignore_content = f"""*venv*
venv/*
build/*
*build*
*{project_name}.egg-info*
{project_name}.egg-info/*
"""
    with open(f"{project_name}/.gitignore", 'w') as f:
        f.write(gitignore_content)

    print(f"Project {project_name} generated with sucess!")

def main():
    project_name = input("Insert the name of project: ")
    requirements_file = input("If have a requirements.txt, insert the path of file  (leave blank if there is none): ")
    github_user = input("Insert the Github user: ")
    author_name = input("Insert name of author: ")
    author_email = input("Insert email of author: ")

    requirements_file = requirements_file if requirements_file else None
    github_user = github_user if github_user else "your_user"
    author_name = author_name if author_name else "Your Name"
    author_email = author_email if author_email else "your_email@exemple.com"
    create_project_structure(
        project_name, 
        requirements_file, 
        author_name, 
        author_email,
        github_user
        )

if __name__ == '__main__':
    main()