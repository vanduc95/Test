# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
"""
import logging
import netaddr
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

LOG = logging.getLogger(__name__)

from horizon import exceptions
from horizon import forms
from horizon import messages
from openstack_dashboard import api
from openstack_dashboard import policy

class CreateDockerfileForm(forms.SelfHandlingForm):
    dockerfile_name = forms.CharField(max_length=255,
                                   label=_("Dockerfile Name"),
                                   required=True)
    dockerfile_file = forms.FileField(label=_("Dockerfile File"),
                                 help_text=_("A local dockerfile to upload."),
                                 widget=forms.FileInput(),
                                 required=False)
    docker_file_edit = forms.CharField(label=_("Dockerfile edit"),
                                 help_text=_("A local dockerfile to upload."),
        widget=forms.Textarea(),required=True)

    def __init__(self, request, *args, **kwargs):
        super(CreateDockerfileForm, self).__init__(request, *args, **kwargs)

    def clean(self):
        cleaned_data = super(CreateDockerfileForm, self).clean()
        return cleaned_data

    def format_status_message(self, message):
        # name = self.context.get('net_name') or self.context.get('net_id', '')
        return message

    def handle(self, request, data):
        text = data["docker_file_edit"]
        name = data['dockerfile_name']
        # conn = sqlite3.connect('test.db')
        # print "Opened database successfully";
        # conn.execute("INSERT INTO DOCKERFILE (NAME,CONTENT) VALUES ("+name+','+text+")");
        # conn.commit()
        # print "Records created successfully";
        # conn.close()
        return True

    def get_success_url(self):
        return reverse("horizon:docker:dockerfile:index")

    def get_failure_url(self):
        return reverse("horizon:docker:dockerfile:index")
