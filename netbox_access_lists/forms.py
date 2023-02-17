from netbox.forms import NetBoxModelForm
from .models import AccessList, AccessListRule

from ipam.models import Prefix
from utilities.forms.fields import CommentField, DynamicModelChoiceField



class AccessListForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = AccessList
        fields = ('name', 'default_action', 'comments', 'tags')


class AccessListRuleForm(NetBoxModelForm):

    class Meta:
        model = AccessListRule
        fields = (
            'access_list', 'index', 'description', 'source_prefix', 'source_ports', 'destination_prefix',
            'destination_ports', 'protocol', 'action', 'tags',
        )
    
    access_list = DynamicModelChoiceField(
        queryset=AccessList.objects.all()
    )
    source_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all()
    )
    destination_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all()
    )