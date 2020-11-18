import click
import os
from one.one import cli
from one.docker.container import Container
from one.docker.image import Image
from one.utils.environment.aws import EnvironmentAws
from one.__init__ import CLI_ROOT
from one.utils.config import get_config_value

container = Container()
image = Image()
environment = EnvironmentAws()
AWS_IMAGE = image.get_image('aws')
KUBE_TOOLS_IMAGE = 'dnxsolutions/docker-kube-tools:0.1.0'


def __init__():
    cli.add_command(kubectl)
    cli.add_command(helm)
    cli.add_command(kube_bash)


def get_kube_config(aws_default_region, cluster_name, envs):
    kubeconfig = get_config_value('plugins.kube.parameters.kubeconfig', '') or '/work/.kube-config'
    command = 'eks --region %s update-kubeconfig --name %s --kubeconfig %s' % (aws_default_region, cluster_name, kubeconfig)
    container.create(
        image=AWS_IMAGE,
        command=command,
        volumes=['.:/work'],
        environment=envs
    )


@click.command(name='kubectl', help='Kubectl wrap command entry.')
@click.argument('args', nargs=-1)
@click.option('-n', '--cluster-name', 'cluster_name', default=None, type=str, help='AWS EKS cluster name.')
@click.option('-w', '--workspace', default=None, type=str, help='Workspace to use.')
@click.option('-r', '--aws-role', 'aws_role', default=None, type=str, help='AWS role to use.')
@click.option('-R', '--aws-default-region', 'aws_default_region', default=None, type=str, help='AWS default region to use.')
def kubectl(args, cluster_name, workspace, aws_role, aws_default_region):
    cluster_name = cluster_name or get_config_value('plugins.kube.parameters.cluster_name')
    aws_default_region = aws_default_region or get_config_value('plugins.kube.parameters.aws_default_region')
    envs = environment.build(workspace, aws_role).get_env()
    envs['KUBECONFIG'] = get_config_value('plugins.kube.parameters.kubeconfig', '') or '/work/.kube-config'

    get_kube_config(aws_default_region, cluster_name, envs)
    entrypoint = 'kubectl'

    command = ''
    for arg in args:
        command += '%s ' % (arg)

    container.create(
        image=KUBE_TOOLS_IMAGE,
        command=command,
        entrypoint=entrypoint,
        volumes=['.:/work'],
        environment=envs
    )


@click.command(name='helm', help='Helm wrap command entry.')
@click.argument('args', nargs=-1)
@click.option('-n', '--cluster-name', 'cluster_name', default=None, type=str, help='AWS EKS cluster name.')
@click.option('-w', '--workspace', default=None, type=str, help='Workspace to use.')
@click.option('-r', '--aws-role', 'aws_role', default=None, type=str, help='AWS role to use.')
@click.option('-R', '--aws-default-region', 'aws_default_region', default=None, type=str, help='AWS default region to use.')
def helm(args, cluster_name, workspace, aws_role, aws_default_region):
    cluster_name = cluster_name or get_config_value('plugins.kube.parameters.cluster_name')
    aws_default_region = aws_default_region or get_config_value('plugins.kube.parameters.aws_default_region')
    envs = environment.build(workspace, aws_role).get_env()
    envs['KUBECONFIG'] = get_config_value('plugins.kube.parameters.kubeconfig', '') or '/work/.kube-config'

    get_kube_config(aws_default_region, cluster_name, envs)
    entrypoint = 'helm'

    command = ''
    for arg in args:
        command += '%s ' % (arg)

    container.create(
        image=KUBE_TOOLS_IMAGE,
        command=command,
        entrypoint=entrypoint,
        volumes=['.:/work'],
        environment=envs
    )


@click.command(name='kube-bash', help='Bash entry to EKS environment.')
@click.option('-n', '--cluster-name', 'cluster_name', default=None, type=str, help='AWS EKS cluster name.')
@click.option('-w', '--workspace', default=None, type=str, help='Workspace to use.')
@click.option('-r', '--aws-role', 'aws_role', default=None, type=str, help='AWS role to use.')
@click.option('-R', '--aws-default-region', 'aws_default_region', default=None, type=str, help='AWS default region to use.')
def kube_bash(cluster_name, workspace, aws_role, aws_default_region):
    cluster_name = cluster_name or get_config_value('plugins.kube.parameters.cluster_name')
    aws_default_region = aws_default_region or get_config_value('plugins.kube.parameters.aws_default_region')
    envs = environment.build(workspace, aws_role).get_env()
    envs['KUBECONFIG'] = get_config_value('plugins.kube.parameters.kubeconfig', '') or '/work/.kube-config'

    get_kube_config(aws_default_region, cluster_name, envs)
    entrypoint = '/bin/bash'

    container.create(
        image=KUBE_TOOLS_IMAGE,
        entrypoint=entrypoint,
        ports=['8001:8001'],
        volumes=['.:/work'],
        environment=envs
    )