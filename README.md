# Index
- [Description](#description)
- [Requirements](#requirements)
- [Steps](#steps)
  - [1. Create a Python3 venv](#1-create-a-python3-venv)
  - [2. Update pip](#2-update-pip)
  - [3. Install required Python3 dependencies](#3-install-required-python3-dependencies)
  - [4. Run the script by specifying a Markdown file](#4-run-the-script-by-specifying-a-markdown-file)

# Description
Generate a Markdown index from any Markdown file.


# Requirements
- `python` >= 3.8


# Steps

## 1. Create a Python3 venv
```bash
python3 -m venv venv_markdown_index_generator
```

Do not forget to source it with the command below:
```bash
. venv_markdown_index_generator/bin/activate
```


## 2. Update pip
```bash
pip3 install --upgrade pip
```


## 3. Install required Python3 dependencies
```bash
pip3 install -r pip3_requirements.txt
```

## 4. Run the script by specifying a Markdown file
```bash
python3 markdown_index_generator.py ./README.md
```

The output should look like this:

```
- [Description](#description)
- [Requirements](#requirements)
- [Steps](#steps)
  - [1. Create a Python3 venv](#1-create-a-python3-venv)
  - [2. Update pip](#2-update-pip)
  - [3. Install required Python3 dependencies](#3-install-required-python3-dependencies)
  - [4. Run the script by specifying a Markdown file](#4-run-the-script-by-specifying-a-markdown-file)
```

