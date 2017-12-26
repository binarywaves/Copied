# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.ntp.
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


class Server(VapiInterface):
    """
    ``Server`` class provides methods Performs NTP configuration.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServerStub)


    def add(self,
            servers,
            ):
        """
        Add NTP servers. This command adds NTP servers to the configuration. If
        the time synchronization is NTP-based, then NTP daemon is restarted to
        reload the new NTP servers. Otherwise, this command just adds servers
        to the NTP configuration.

        :type  servers: :class:`list` of :class:`str`
        :param servers: List of host names or IP addresses of NTP servers.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('add',
                            {
                            'servers': servers,
                            })

    def set(self,
            servers,
            ):
        """
        Set NTP servers. This command deletes old NTP servers from the
        configuration and sets the input NTP servers in the configuration. If
        the time synchronization is NTP-based, the NTP daemon is restarted to
        reload the new NTP configuration. Otherwise, this command just replaces
        servers in the NTP configuration.

        :type  servers: :class:`list` of :class:`str`
        :param servers: List of host names or ip addresses of ntp servers.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'servers': servers,
                            })

    def delete(self,
               servers,
               ):
        """
        Delete NTP servers. This command deletes NTP servers from the
        configuration. If the time synchronization mode is NTP-based, the NTP
        daemon is restarted to reload the new NTP configuration. Otherwise,
        this command just deletes servers from the NTP configuration.

        :type  servers: :class:`list` of :class:`str`
        :param servers: List of host name or ip addresses of ntp servers.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('delete',
                            {
                            'servers': servers,
                            })

class _ServerStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'servers': type.ListType(type.StringType()),
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
            'servers': type.ListType(type.StringType()),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        set_input_validator_list = [
        ]
        set_output_validator_list = [
        ]

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'servers': type.ListType(type.StringType()),
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_validator_list': delete_input_validator_list,
                'output_validator_list': delete_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.ntp.server',
                                  config=config,
                                  operations=operations)

