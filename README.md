# Taskify
Used to make writing python tasks easier so that you can focus on getting stuff done. Taskify takes care of implementation boiler-plate and provides a more generic
interface for performing tasks.

## Installation
```bash
$ pip install taskify
```

## Usage
```python
# run.py

from taskify.config import configBuilder
from taskify.dev-tool import build, clean, run

# Configure taskify
config = configBuilder.container('docker')
                      .devTool('dotnet')
                      .buildAndSet()

# need to choose a dev-tool provider in taskify.conf
#   ex: dotnet
build('/path/to/foobar.csproj')
run('/path/to/foobar.csproj')
```

```python
# build-and-publish-docker.py

from taskify.config import configBuilder
from taskify.container import build, push, tag

# Configure taskify
config = configBuilder.container('docker')
                      .devTool('dotnet')
                      .buildAndSet()

# need to choose a container provider in taskify.conf
#   ex: docker
build('/path/to/source/Dockerfile')
tag('image1', 'registry.domain.com/image1:latest')
push('registry.domain.com/image1:latest')
```
