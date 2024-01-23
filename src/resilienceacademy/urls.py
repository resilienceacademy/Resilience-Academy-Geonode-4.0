# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import url
from django.views.generic import TemplateView
from geonode.urls import urlpatterns

urlpatterns = [
    url(r'^contact-us/$',
        TemplateView.as_view(template_name='contact_us.html'),
        name='contact-us'),
    url(r'^term-of-use/$',
        TemplateView.as_view(
            template_name='terms_use.html'),
        name='term-of-use'),
    url(r'^get-started/$',
        TemplateView.as_view(template_name='get_started.html'),
        name='get-started'),
    url(r'^crd-team/$',
        TemplateView.as_view(template_name='crd_team.html'),
        name='crd-team'),
    url(r'^tools-page/$',
        TemplateView.as_view(template_name='tools.html'),
        name='tools-page'),
] + urlpatterns
