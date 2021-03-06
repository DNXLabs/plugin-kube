# plugin-kube

This is a one-cli plugin that adds Kubernetes tools alias to the CLI.

![Build](https://github.com/DNXLabs/plugin-kube/workflows/Build/badge.svg)
[![PyPI](https://badge.fury.io/py/one-cli-plugin-kube.svg)](https://pypi.python.org/pypi/one-cli-plugin-kube/)
[![LICENSE](https://img.shields.io/github/license/DNXLabs/plugin-kube)](https://github.com/DNXLabs/plugin-kube/blob/master/LICENSE)

## Configuration

```yaml
# one.yaml
required_version: ">= 0.7.1"

plugins:
  kube:
    package: one-cli-plugin-kube==0.5.2
    module: 'plugin_kube'
    parameters:
      cluster_name: <redact>
      aws_default_region: <redact>
      aws_assume_role: # Optional: default to false
      kubeconfig: # Optional: Override default kubeconfig path
```

## Usage

```bash
one kubectl ...
one helm ...
one kube-bash
```

## Development

#### Dependencies

- Python 3

#### Python Virtual Environment

```bash
# Create environment
python3 -m venv env

# To activate the environment
source env/bin/activate

# When you finish you can exit typing
deactivate
```

#### Install dependencies

```bash
pip3 install --editable .
```

## Author

Managed by [DNX Solutions](https://github.com/DNXLabs).

## License

Apache 2 Licensed. See [LICENSE](https://github.com/DNXLabs/plugin-kube/blob/master/LICENSE) for full details.