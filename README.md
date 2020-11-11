# plugin-kube

This is a one-cli plugin that adds Kubernetes tools alias to the CLI.


## Configuration

```yaml
# one.yaml
plugins:
  kube:
    source: https://github.com/DNXLabs/plugin-kube/archive/master.tar.gz
    parameters:
      cluster_name: <redact>
      aws_default_region: <redact>
```

## Usage

```bash
one kubectl ...
one helm ...
one kube-bash
```

## Author

Managed by [DNX Solutions](https://github.com/DNXLabs).

## License

Apache 2 Licensed. See [LICENSE](https://github.com/DNXLabs/plugin-kube/blob/master/LICENSE) for full details.