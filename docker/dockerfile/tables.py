from django.utils.http import urlencode
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy
from django.template import defaultfilters as filters
from horizon.utils.memoized import memoized  # noqa

from horizon import tables
from django import template
from openstack_dashboard import api

from docker import Client
import os

# class Build(tables.LinkAction):
#     name = "create"
#     verbose_name = _("Build")
#     url = "horizon:docker:dockerfile:build"
#     classes = ("ajax-modal",)
#     icon = "plus"

class Build(tables.BatchAction):
    name = 'build'

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Build",
            u"Build",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Success Build",
            u"Success Build",
            count
        )
    def action(self, request, datum_id):
        print 'duc'
        print os.path.dirname(os.path.realpath(__file__))

        cli = Client(base_url='unix://var/run/docker.sock')
        response = [line for line in
                    cli.build(path=os.path.dirname(os.path.realpath(__file__))+'/file', rm=True, tag='vanduc/test1')]
        print response


class CreateDockerfile(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Dockerfile")
    url = "horizon:docker:dockerfile:create"
    classes = ("ajax-modal",)
    icon = "plus"
    # policy_rules = (("network", "create_network"),)
class CreateNetwork(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Network")
    url = "horizon:sks:network:create"
    classes = ("ajax-modal",)
    icon = "plus"
    # policy_rules = (("network", "create_network"),)


class DockerFilter(tables.FilterAction):
    name = 'docker_filter'
class DockerfileTable(tables.DataTable):

    name = tables.Column("name",
                         verbose_name=_(" Name"),
                         truncate=40,
                         )

    data = tables.Column("data",verbose_name=_(" Data"),)

    class Meta(object):
        verbose_name = _("Dockerfile")
        name = "dockerfile"
        table_actions = (DockerFilter, CreateDockerfile,)
        row_actions = (Build,)

    def __init__(self, request, *args, **kwargs):
        super(DockerfileTable, self).__init__(request, *args, **kwargs)


    class Meta(object):
        verbose_name = _("Dockerfile")
        name = "dockerfile"
        table_actions = (DockerFilter, CreateDockerfile,)
        row_actions = (Build,)


