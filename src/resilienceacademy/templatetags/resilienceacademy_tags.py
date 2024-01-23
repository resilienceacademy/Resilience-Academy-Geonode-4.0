from django import template
from geonode.base.models import Configuration
from geonode_mapstore_client.templatetags.get_menu_json import _is_mobile_device

register = template.Library()

@register.simple_tag(takes_context=True)
def get_custom_base_right_topbar_menu(context):

    is_mobile = _is_mobile_device(context)

    if is_mobile:
        return []

    home = {
        "type": "link",
        "href": "/",
        "label": "Home"
    }
    resources = {
        "label": "Resources",
        "type": "dropdown",
        "items": [
            {
                "type": "link",
                "href": "https://crd-userguide.readthedocs.io/en/latest/",
                "label": "Training",
                "target": "blank"
            },
            {
                "type": "link",
                "href": "/tools-page",
                "label": "Tools"
            }
        ]
    }
    user = context.get('request').user
    about = {
            "label": "Community",
            "type": "dropdown",
            "items": [
                {
                    "type": "link",
                    "href": "/people/",
                    "label": "Registered Members"
                },
                {
                    "type": "link",
                    "href": "/groups/categories",
                    "label": "Community Groups"
                }
            ]
        }
    if user.is_authenticated and not Configuration.load().read_only:
        about['items'].extend([
            {
                "type": "divider"
            },
            {
                "type": "link",
                "href": "/invitations/geonode-send-invite/",
                "label": "Invite users"
            },
            {
                "type": "link",
                "href": "/admin/people/profile/add/",
                "label": "Add user"
            } if user.is_superuser else None,
            {
                "type": "link",
                "href": "/groups/create/",
                "label": "Create group"
            }if user.is_superuser else None,
        ])
    return [home, resources, about]
