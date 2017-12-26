# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.networking.firewall.addr.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import VapiInterface, ApiInterfaceStub
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import UnionValidator, HasFieldsOfValidator
from vmware.vapi.exception import CoreException
import com.vmware.vapi.std.errors_client


class Inbound(VapiInterface):
    """
    ``Inbound`` class provides methods Operations for Firewall rules.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InboundStub)

    class FirewallRulePolicy(Enum):
        """
        ``Inbound.FirewallRulePolicy`` class Defines firewall rule policies

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        deny = None
        """
        Deny packet with correpsonding address.

        """
        allow = None
        """
        Allow packet with corresponding address.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`FirewallRulePolicy` instance.
            """
            Enum.__init__(string)

    FirewallRulePolicy._set_values([
        FirewallRulePolicy('deny'),
        FirewallRulePolicy('allow'),
    ])
    FirewallRulePolicy._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.networking.firewall.addr.inbound.firewall_rule_policy',
        FirewallRulePolicy))


    class FirewallAddressRule(VapiStruct):
        """
        ``Inbound.FirewallAddressRule`` class Structure that defines a single
        address-based firewall rule.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     address=None,
                     prefix=None,
                     policy=None,
                     interface_name=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: IPv4 or IPv6 address.
            :type  prefix: :class:`long`
            :param prefix: CIDR prefix used to mask address. For example, an IPv4 prefix of 24
                ignores the low-order 8 bits of address.
            :type  policy: :class:`Inbound.FirewallRulePolicy`
            :param policy: The allow or deny policy of this rule.
            :type  interface_name: :class:`str`
            :param interface_name: The interface to which this rule applies. An empty string or
                "\\\\*" indicates that the rule applies to all interfaces.
            """
            self.address = address
            self.prefix = prefix
            self.policy = policy
            self.interface_name = interface_name
            VapiStruct.__init__(self)

    FirewallAddressRule._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.firewall.addr.inbound.firewall_address_rule', {
            'address': type.StringType(),
            'prefix': type.IntegerType(),
            'policy': type.ReferenceType(sys.modules[__name__], 'Inbound.FirewallRulePolicy'),
            'interface_name': type.StringType(),
        },
        FirewallAddressRule,
        False,
        None))


    class DeleteFirewallRule(VapiStruct):
        """
        ``Inbound.DeleteFirewallRule`` class Structure that defines
        networking.firewall.addr.inbound.delete api input argument

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     position=None,
                     all=None,
                    ):
            """
            :type  position: :class:`long`
            :param position: Position before which to insert the rule (zero-based). If you try
                to insert the rule in a position whose number is greater than the
                number of rules, the firewall rule is inserted at the end of the
                list.
            :type  all: :class:`bool`
            :param all: Delete all firewall rules. Set all argument to "true" to delete all
                rules or set the all argument to "false" to delete a single rule.
            """
            self.position = position
            self.all = all
            VapiStruct.__init__(self)

    DeleteFirewallRule._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.firewall.addr.inbound.delete_firewall_rule', {
            'position': type.IntegerType(),
            'all': type.BooleanType(),
        },
        DeleteFirewallRule,
        False,
        None))



    def add(self,
            pos,
            rule,
            ):
        """
        Add a firewall rule to allow or deny traffic from incoming IP address.

        :type  pos: :class:`long`
        :param pos: Position before which to insert the rule (zero-based). If you try
            to insert the rule in a position whose number is greater than the
            number of rules, the firewall rule is inserted at the end of the
            list.
        :type  rule: :class:`Inbound.FirewallAddressRule`
        :param rule: Firewall IP-based rule.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('add',
                            {
                            'pos': pos,
                            'rule': rule,
                            })

    def set(self,
            rules,
            ):
        """
        Set list of inbound IP addresses to allow or deny by firewall. This
        replaces all existing rules. Firewall rules have no impact on closed
        ports because these ports are closed for all traffic.

        :type  rules: :class:`list` of :class:`Inbound.FirewallAddressRule`
        :param rules: List of address-based firewall rules.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'rules': rules,
                            })

    def list(self):
        """
        Get ordered list of inbound IP addresses that are allowed or denied by
        firewall.


        :rtype: :class:`list` of :class:`Inbound.FirewallAddressRule`
        :return: List of address-based firewall rules.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def delete(self,
               config,
               ):
        """
        Delete specific rule at a given position or delete all rules.

        :type  config: :class:`Inbound.DeleteFirewallRule`
        :param config: Delete a firewall rule
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('delete',
                            {
                            'config': config,
                            })

class _InboundStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'pos': type.IntegerType(),
            'rule': type.ReferenceType(sys.modules[__name__], 'Inbound.FirewallAddressRule'),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        add_input_validator_list = [
        ]
        add_output_validator_list = [
        ]

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'rules': type.ListType(type.ReferenceType(sys.modules[__name__], 'Inbound.FirewallAddressRule')),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        set_input_validator_list = [
        ]
        set_output_validator_list = [
        ]

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        list_input_validator_list = [
        ]
        list_output_validator_list = [
        ]

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Inbound.DeleteFirewallRule'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        delete_input_validator_list = [
        ]
        delete_output_validator_list = [
        ]

        operations = {
            'add': {
                'input_type': add_input_type,
                'output_type': type.VoidType(),
                'errors': add_error_dict,
                'input_validator_list': add_input_validator_list,
                'output_validator_list': add_output_validator_list,
            },
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_validator_list': set_input_validator_list,
                'output_validator_list': set_output_validator_list,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Inbound.FirewallAddressRule')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_validator_list': delete_input_validator_list,
                'output_validator_list': delete_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.networking.firewall.addr.inbound',
                                  config=config,
                                  operations=operations)

