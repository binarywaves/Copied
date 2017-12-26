# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.restore.
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


class Job(VapiInterface):
    """
    ``Job`` class provides methods Performs restore operations
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _JobStub)

    class ReturnStatus(Enum):
        """
        ``Job.ReturnStatus`` class Defines the state of precheck

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FAIL = None
        """
        Check failed

        """
        WARNING = None
        """
        Passed with warnings

        """
        OK = None
        """
        Check passed

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ReturnStatus` instance.
            """
            Enum.__init__(string)

    ReturnStatus._set_values([
        ReturnStatus('FAIL'),
        ReturnStatus('WARNING'),
        ReturnStatus('OK'),
    ])
    ReturnStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.restore.job.return_status',
        ReturnStatus))


    class LocationType(Enum):
        """
        ``Job.LocationType`` class Defines type of all locations for backup/restore

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FTPS = None
        """
        Destination is FTPS server

        """
        HTTP = None
        """
        Destination is HTTP server

        """
        SCP = None
        """
        Destination is SSH server

        """
        HTTPS = None
        """
        Destination is HTTPS server

        """
        FTP = None
        """
        Destination is FTP server

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`LocationType` instance.
            """
            Enum.__init__(string)

    LocationType._set_values([
        LocationType('FTPS'),
        LocationType('HTTP'),
        LocationType('SCP'),
        LocationType('HTTPS'),
        LocationType('FTP'),
    ])
    LocationType._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.restore.job.location_type',
        LocationType))


    class BackupRestoreProcessState(Enum):
        """
        ``Job.BackupRestoreProcessState`` class Defines state of backup/restore
        process

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FAILED = None
        """
        Failed

        """
        INPROGRESS = None
        """
        In progress

        """
        NONE = None
        """
        Not started

        """
        SUCCEEDED = None
        """
        Completed successfully

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackupRestoreProcessState` instance.
            """
            Enum.__init__(string)

    BackupRestoreProcessState._set_values([
        BackupRestoreProcessState('FAILED'),
        BackupRestoreProcessState('INPROGRESS'),
        BackupRestoreProcessState('NONE'),
        BackupRestoreProcessState('SUCCEEDED'),
    ])
    BackupRestoreProcessState._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.restore.job.backup_restore_process_state',
        BackupRestoreProcessState))


    class LocalizableMessage(VapiStruct):
        """
        ``Job.LocalizableMessage`` class Structure representing message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     id=None,
                     default_message=None,
                     args=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: id in message bundle
            :type  default_message: :class:`str`
            :param default_message: text in english
            :type  args: :class:`list` of :class:`str`
            :param args: nested data
            """
            self.id = id
            self.default_message = default_message
            self.args = args
            VapiStruct.__init__(self)

    LocalizableMessage._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.job.localizable_message', {
            'id': type.StringType(),
            'default_message': type.StringType(),
            'args': type.ListType(type.StringType()),
        },
        LocalizableMessage,
        False,
        None))


    class ReturnResult(VapiStruct):
        """
        ``Job.ReturnResult`` class Structure representing precheck result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Job.ReturnStatus`
            :param status: Check status
            :type  messages: :class:`list` of :class:`Job.LocalizableMessage`
            :param messages: List of messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    ReturnResult._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.job.return_result', {
            'status': type.ReferenceType(sys.modules[__name__], 'Job.ReturnStatus'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Job.LocalizableMessage')),
        },
        ReturnResult,
        False,
        None))


    class RestoreRequest(VapiStruct):
        """
        ``Job.RestoreRequest`` class Structure representing requested restore piece

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     backup_password=None,
                     location_type=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                    ):
            """
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: a password for a backup piece
                backupPassword If no password then the piece will not be decrypted
            :type  location_type: :class:`Job.LocationType`
            :param location_type: a type of location
            :type  location: :class:`str`
            :param location: path or url
            :type  location_user: :class:`str` or ``None``
            :param location_user: username for location
                locationUser User name for this location if login is required.
            :type  location_password: :class:`str` or ``None``
            :param location_password: password for location
                locationPassword Password for the specified user if login is
                required at this location.
            """
            self.backup_password = backup_password
            self.location_type = location_type
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            VapiStruct.__init__(self)

    RestoreRequest._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.job.restore_request', {
            'backup_password': type.OptionalType(type.SecretType()),
            'location_type': type.ReferenceType(sys.modules[__name__], 'Job.LocationType'),
            'location': type.StringType(),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
        },
        RestoreRequest,
        False,
        None))


    class RestoreJobStatus(VapiStruct):
        """
        ``Job.RestoreJobStatus`` class Structure representing backup restore status

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     state=None,
                     messages=None,
                     progress=None,
                    ):
            """
            :type  state: :class:`Job.BackupRestoreProcessState`
            :param state: process state
            :type  messages: :class:`list` of :class:`Job.LocalizableMessage`
            :param messages: list of messages
            :type  progress: :class:`long`
            :param progress: percentage complete
            """
            self.state = state
            self.messages = messages
            self.progress = progress
            VapiStruct.__init__(self)

    RestoreJobStatus._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.job.restore_job_status', {
            'state': type.ReferenceType(sys.modules[__name__], 'Job.BackupRestoreProcessState'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Job.LocalizableMessage')),
            'progress': type.IntegerType(),
        },
        RestoreJobStatus,
        False,
        None))



    def cancel(self):
        """
        Cancel the backup job


        :rtype: :class:`Job.ReturnResult`
        :return: RestoreJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('cancel', None)

    def create(self,
               piece,
               ):
        """
        Initiate restore.

        :type  piece: :class:`Job.RestoreRequest`
        :param piece: RestoreRequest Structure
        :rtype: :class:`Job.RestoreJobStatus`
        :return: RestoreJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.FeatureInUse` 
            A backup or restore is already in progress
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            Restore is allowed only after deployment and before firstboot
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('create',
                            {
                            'piece': piece,
                            })

    def get(self):
        """
        See restore job progress/result.


        :rtype: :class:`Job.RestoreJobStatus`
        :return: RestoreJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

class _JobStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {})
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        cancel_input_validator_list = [
        ]
        cancel_output_validator_list = [
        ]

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'piece': type.ReferenceType(sys.modules[__name__], 'Job.RestoreRequest'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.feature_in_use':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'FeatureInUse'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        create_input_validator_list = [
        ]
        create_output_validator_list = [
        ]

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        get_input_validator_list = [
        ]
        get_output_validator_list = [
        ]

        operations = {
            'cancel': {
                'input_type': cancel_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Job.ReturnResult'),
                'errors': cancel_error_dict,
                'input_validator_list': cancel_input_validator_list,
                'output_validator_list': cancel_output_validator_list,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Job.RestoreJobStatus'),
                'errors': create_error_dict,
                'input_validator_list': create_input_validator_list,
                'output_validator_list': create_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Job.RestoreJobStatus'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.recovery.restore.job',
                                  config=config,
                                  operations=operations)

