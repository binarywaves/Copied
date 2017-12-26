# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.networking.
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


class Interfaces(VapiInterface):
    """
    ``Interfaces`` class provides methods Provides information about network
    interface.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InterfacesStub)

    class InterfaceStatus(Enum):
        """
        ``Interfaces.InterfaceStatus`` class Defines interface status

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        down = None
        """
        The interface is down.

        """
        up = None
        """
        The interface is up.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`InterfaceStatus` instance.
            """
            Enum.__init__(string)

    InterfaceStatus._set_values([
        InterfaceStatus('down'),
        InterfaceStatus('up'),
    ])
    InterfaceStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.interfaces.interface_status',
        InterfaceStatus))


    class InterfaceInfo(VapiStruct):
        """
        ``Interfaces.InterfaceInfo`` class Structure that defines properties and
        status of a network interface.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     name=None,
                     status=None,
                     mac=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Interface name, for example, "nic0", "nic1".
            :type  status: :class:`Interfaces.InterfaceStatus`
            :param status: Interface status.
            :type  mac: :class:`str`
            :param mac: MAC address. For example 00:0C:29:94:BB:5A.
            """
            self.name = name
            self.status = status
            self.mac = mac
            VapiStruct.__init__(self)

    InterfaceInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.interface_info', {
            'name': type.StringType(),
            'status': type.ReferenceType(sys.modules[__name__], 'Interfaces.InterfaceStatus'),
            'mac': type.StringType(),
        },
        InterfaceInfo,
        False,
        None))



    def list(self):
        """
        Get list of available network interfaces, including those that are not
        yet configured.


        :rtype: :class:`list` of :class:`Interfaces.InterfaceInfo`
        :return: List of InterfaceInfo structures.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            interface_name,
            ):
        """
        Get information about a particular network interface.

        :type  interface_name: :class:`str`
        :param interface_name: Network interface, for example, "nic0".
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.networking.interfaces``.
        :rtype: :class:`Interfaces.InterfaceInfo`
        :return: Network interface information.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'interface_name': interface_name,
                            })

class _InterfacesStub(ApiInterfaceStub):
    def __init__(self, config):
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'interface_name': type.IdType(resource_types='com.vmware.appliance.networking.interfaces'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        get_input_validator_list = [
        ]
        get_output_validator_list = [
        ]

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Interfaces.InterfaceInfo')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Interfaces.InterfaceInfo'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.networking.interfaces',
                                  config=config,
                                  operations=operations)

