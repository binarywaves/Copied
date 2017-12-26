# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.iso.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.iso_client`` module provides classes and classes that
will let its client mount or unmount an ISO image on a virtual machine as a
CD-ROM.

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


class Image(VapiInterface):
    """
    Provides an interface to mount and unmount an ISO image on a virtual
    machine. 
    
    This is an API that will let its client mount or unmount an ISO image on a
    virtual machine as a CD-ROM. 
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ImageStub)


    def mount(self,
              library_item,
              vm,
              ):
        """
        Mounts an ISO image from a content library on a virtual machine.

        :type  library_item: :class:`str`
        :param library_item: The identifier of the library item having the ISO image to mount on
            the virtual machine.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  vm: :class:`str`
        :param vm: The identifier of the virtual machine where the specified ISO image
            will be mounted.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`str`
        :return: The identifier of the newly created virtual CD-ROM backed by the
            specified ISO image.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If either ``vm`` or the ``library_item`` is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If no .iso file is present on the library item.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            When the operation is not allowed on the virtual machine in its
            current state.
        """
        return self._invoke('mount',
                            {
                            'library_item': library_item,
                            'vm': vm,
                            })

    def unmount(self,
                vm,
                cdrom,
                ):
        """
        Unmounts a previously mounted CD-ROM using an ISO image as a backing.

        :type  vm: :class:`str`
        :param vm: The identifier of the virtual machine from which to unmount the
            virtual CD-ROM.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  cdrom: :class:`str`
        :param cdrom: The device identifier of the CD-ROM.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the virtual machine identified by ``vm`` is not found or the
            ``cdrom`` does not identify a virtual CD-ROM in the virtual
            machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            When the operation is not allowed on the virtual machine in its
            current state.
        """
        return self._invoke('unmount',
                            {
                            'vm': vm,
                            'cdrom': cdrom,
                            })

class _ImageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for mount operation
        mount_input_type = type.StructType('operation-input', {
            'library_item': type.IdType(resource_types='com.vmware.content.library.Item'),
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        mount_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'ResourceInaccessible'),

        }
        mount_input_validator_list = [
        ]
        mount_output_validator_list = [
        ]

        # properties for unmount operation
        unmount_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
        })
        unmount_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotAllowedInCurrentState'),

        }
        unmount_input_validator_list = [
        ]
        unmount_output_validator_list = [
        ]

        operations = {
            'mount': {
                'input_type': mount_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
                'errors': mount_error_dict,
                'input_validator_list': mount_input_validator_list,
                'output_validator_list': mount_output_validator_list,
            },
            'unmount': {
                'input_type': unmount_input_type,
                'output_type': type.VoidType(),
                'errors': unmount_error_dict,
                'input_validator_list': unmount_input_validator_list,
                'output_validator_list': unmount_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.vcenter.iso.image',
                                  config=config,
                                  operations=operations)

