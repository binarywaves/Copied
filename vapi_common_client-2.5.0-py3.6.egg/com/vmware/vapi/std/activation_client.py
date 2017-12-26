# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.std.activation.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.std.activation_client`` module provides classes that
TODO.

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


class ActivationManager(VapiInterface):
    """
    **WARNING:** Use only as a sample. The API is experimental and subject to
    change in future versions. 
    
     Activation tracking/management service. 
    
     An activation describes a method invocation in the runtime.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ActivationManagerStub)


    def cancel(self,
               activation_id,
               ):
        """
        Asks for cancellation of a running activation. Whether or not the
        cancellation request will have any effect depends on the implementation
        of the method that has to be canceled.

        :type  activation_id: :class:`str`
        :param activation_id: activation identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            there is no activation with the specified id
        """
        return self._invoke('cancel',
                            {
                            'activation_id': activation_id,
                            })

class _ActivationManagerStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'activation_id': type.StringType(),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotFound'),

        }
        cancel_input_validator_list = [
        ]
        cancel_output_validator_list = [
        ]

        operations = {
            'cancel': {
                'input_type': cancel_input_type,
                'output_type': type.VoidType(),
                'errors': cancel_error_dict,
                'input_validator_list': cancel_input_validator_list,
                'output_validator_list': cancel_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.vapi.std.activation.activation_manager',
                                  config=config,
                                  operations=operations)

