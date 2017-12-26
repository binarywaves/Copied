# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.vcenter.
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


class Activation(VapiInterface):
    """
    The ``Activation`` class provides methods for tasks cancelation.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ActivationStub)


    def cancel(self,
               activation_id,
               ):
        """
        Sends a request to cancel the task associated with the provided
        ``activation_id``.

        :type  activation_id: :class:`str`
        :param activation_id: the ``activation_id`` associated with a vCenter Server task to be
            canceled.
            The parameter must be an identifier for the resource type:
            ``com.vmware.Activation``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a vCenter Server task with the given ``activation_id`` was not
            found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the vCenter Server task associated with the given
            ``activation_id`` is not cancelable.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if the user is not authorized to cancel the task.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the task cancelation cannot be performed due to vCenter server
            is unreachable or it is not properly configured.
        """
        return self._invoke('cancel',
                            {
                            'activation_id': activation_id,
                            })

class _ActivationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'activation_id': type.IdType(resource_types='com.vmware.Activation'),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'ServiceUnavailable'),

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
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.vapi.vcenter.activation',
                                  config=config,
                                  operations=operations)

