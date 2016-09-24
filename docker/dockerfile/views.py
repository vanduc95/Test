# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from __future__ import division
from horizon import views
import datetime
import json
import time
import openstack_dashboard.dashboards.docker.dockerfile.docker_api as docker_api
import django.views
from django.http import HttpResponse  # noqa
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from docutils.nodes import table
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from openstack_dashboard.dashboards.docker.network import forms as network_forms

from horizon import exceptions
from horizon import forms
from horizon import tabs
from horizon.utils import memoized
from openstack_dashboard.dashboards.docker.dockerfile import forms as docker_form


from openstack_dashboard import api
from openstack_dashboard.utils import filters

from horizon import views
from horizon import  tables
from openstack_dashboard import api
from openstack_dashboard.dashboards.docker.dockerfile import tables as dockerfile_table
from django.utils.translation import ugettext_lazy as _
from horizon import exceptions



# class IndexView(views.APIView):
#     # A very simple class-based view...
#     template_name = 'docker/dockerfile/index.html'
#
#     def get_data(self, request, context, *args, **kwargs):
#         # Add data to the context here...
#         return context

class Dockerfile():
    def __init__(self, id, name, data):
        self.id = id
        self.data = data
        self.name = name


class IndexView(tables.DataTableView):
    table_class = dockerfile_table.DockerfileTable
    template_name = 'docker/dockerfile/index.html'
    page_title = _("Dockerfile")

    def get_data(self):
        return [Dockerfile('1', 'file1', 'FROM ubuntu:14.04\nRUN apt-get update'),
                Dockerfile('2', 'file2', 'FROM ubuntu:14.04\nRUN apt-get update'),
                Dockerfile('3', 'file3', 'FROM ubuntu:14.04\nRUN apt-get update'),
                Dockerfile('4', 'file4', 'FROM ubuntu:14.04\nRUN apt-get update'),
                Dockerfile('5', 'file5', 'FROM ubuntu:14.04\nRUN apt-get update'),
                Dockerfile('6', 'file6', 'FROM ubuntu:14.04\nRUN apt-get update'),
                ]


class CreateView(forms.ModalFormView):
    form_class = docker_form.CreateDockerfileForm
    form_id = "Upload docker file"
    modal_header = _("Create A Dockerfile")
    submit_label = _("Create Dockerfile")
    submit_url = reverse_lazy("horizon:docker:dockerfile:create")
    template_name = 'docker/dockerfile/create.html'
    context_object_name = 'image'
    success_url = reverse_lazy("horizon:docker:dockerfile:index")
    page_title = _("Create dockerfile")

    def get_initial(self):
        initial = {}
        return initial


class CreateNetworkView(forms.ModalFormView):
    form_class = network_forms.CreateNetworkForm
    form_id = "create_docker_form"
    modal_header = _("Create A Network")
    submit_label = _("Create Network")
    submit_url = reverse_lazy('horizon:sks:network:create')
    template_name = 'sks/network/create.html'
    context_object_name = 'image'
    success_url = reverse_lazy("horizon:sks:network:index")
    page_title = _("Create A Network")

    def get_initial(self):
        initial = {}
        for name in [
            'name',
            'description',
            'image_url',
            'source_type',
            'architecture',
            'disk_format',
            'minimum_disk',
            'minimum_ram'
        ]:
            tmp = self.request.GET.get(name)
            if tmp:
                initial[name] = tmp
        return initial