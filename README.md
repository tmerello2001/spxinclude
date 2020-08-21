# spxinclude

Include directives for sphinx

## Install

### From repo
 1. `git clone https://github.com/tmerello2001/spxinclude.git`
 2. `pip install .`

### Using pip

Add the following line to your requirements file
```
git+https://github.com/tmerello2001/spxinclude.git@master
```

## Usage

### gitremote

Add the extension to `config.py`
```python
extensions = [
	'spxinclude.gitremote'
]
```

Use `.. git-remote-include::` directive to include remote files from repos

```
.. git-remote-include:: {repo (ssh or https)},&{branch},&{file to include}
```
For example
```
.. git-remote-include:: https://github.com/tmerello2001/spxinclude.git,&master,&README.md
```
