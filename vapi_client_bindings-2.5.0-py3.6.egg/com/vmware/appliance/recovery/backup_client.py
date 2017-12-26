# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.backup.
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
    ``Job`` class provides methods Performs backup restore operations
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
        'com.vmware.appliance.recovery.backup.job.return_status',
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
        'com.vmware.appliance.recovery.backup.job.location_type',
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
        'com.vmware.appliance.recovery.backup.job.backup_restore_process_state',
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
        'com.vmware.appliance.recovery.backup.job.localizable_message', {
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
        'com.vmware.appliance.recovery.backup.job.return_result', {
            'status': type.ReferenceType(sys.modules[__name__], 'Job.ReturnStatus'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Job.LocalizableMessage')),
        },
        ReturnResult,
        False,
        None))


    class BackupRequest(VapiStruct):
        """
        ``Job.BackupRequest`` class Structure representing requested backup piece

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     parts=None,
                     backup_password=None,
                     location_type=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                     comment=None,
                    ):
            """
            :type  parts: :class:`list` of :class:`str`
            :param parts: a list of optional parts. Run backup parts APIs to get list of
                optional parts and description
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: a password for a backup piece The backupPassword must adhere to the
                following password requirements: At least 8 characters, cannot be
                more than 20 characters in length. At least 1 uppercase letter. At
                least 1 lowercase letter. At least 1 numeric digit. At least 1
                special character (i.e. any character not in [0-9,a-z,A-Z]). Only
                visible ASCII characters (for example, no space).
                backupPassword If no password then the piece will not be encrypted
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
            :type  comment: :class:`str` or ``None``
            :param comment: Custom comment
                comment an optional comment
            """
            self.parts = parts
            self.backup_password = backup_password
            self.location_type = location_type
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            self.comment = comment
            VapiStruct.__init__(self)

    BackupRequest._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.backup_request', {
            'parts': type.ListType(type.StringType()),
            'backup_password': type.OptionalType(type.SecretType()),
            'location_type': type.ReferenceType(sys.modules[__name__], 'Job.LocationType'),
            'location': type.StringType(),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
            'comment': type.OptionalType(type.StringType()),
        },
        BackupRequest,
        False,
        None))


    class BackupJobStatus(VapiStruct):
        """
        ``Job.BackupJobStatus`` class Structure representing backup restore status

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     id=None,
                     state=None,
                     messages=None,
                     progress=None,
                     start_time=None,
                     end_time=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: TimeStamp based ID
            :type  state: :class:`Job.BackupRestoreProcessState`
            :param state: process state
            :type  messages: :class:`list` of :class:`Job.LocalizableMessage`
            :param messages: list of messages
            :type  progress: :class:`long`
            :param progress: percentage complete
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when this backup was started.
            :type  end_time: :class:`datetime.datetime` or ``None``
            :param end_time: Time when this backup was finished.
                endTime End time is None till backup is finished.
            """
            self.id = id
            self.state = state
            self.messages = messages
            self.progress = progress
            self.start_time = start_time
            self.end_time = end_time
            VapiStruct.__init__(self)

    BackupJobStatus._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.backup_job_status', {
            'id': type.StringType(),
            'state': type.ReferenceType(sys.modules[__name__], 'Job.BackupRestoreProcessState'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Job.LocalizableMessage')),
            'progress': type.IntegerType(),
            'start_time': type.DateTimeType(),
            'end_time': type.OptionalType(type.DateTimeType()),
        },
        BackupJobStatus,
        False,
        None))



    def cancel(self,
               id,
               ):
        """
        Cancel the backup job

        :type  id: :class:`str`
        :param id: ID (ID of job)
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.job``.
        :rtype: :class:`Job.ReturnResult`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            ID is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('cancel',
                            {
                            'id': id,
                            })

    def create(self,
               piece,
               ):
        """
        Initiate backup.

        :type  piece: :class:`Job.BackupRequest`
        :param piece: BackupRequest Structure
        :rtype: :class:`Job.BackupJobStatus`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.FeatureInUse` 
            A backup or restore is already in progress
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('create',
                            {
                            'piece': piece,
                            })

    def list(self):
        """
        Get list of backup jobs


        :rtype: :class:`list` of :class:`str`
        :return: list of BackupJob IDs
            The return value will contain identifiers for the resource type:
            ``com.vmware.appliance.recovery.backup.job``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            id,
            ):
        """
        See backup job progress/result.

        :type  id: :class:`str`
        :param id: ID (ID of job)
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.job``.
        :rtype: :class:`Job.BackupJobStatus`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            ID is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'id': id,
                            })

class Parts(VapiInterface):
    """
    ``Parts`` class provides methods Provides list of parts optional for the
    backup
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PartsStub)

    class LocalizableMessage(VapiStruct):
        """
        ``Parts.LocalizableMessage`` class Structure representing message

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
        'com.vmware.appliance.recovery.backup.parts.localizable_message', {
            'id': type.StringType(),
            'default_message': type.StringType(),
            'args': type.ListType(type.StringType()),
        },
        LocalizableMessage,
        False,
        None))


    class Part(VapiStruct):
        """
        ``Parts.Part`` class Structure representing backup restore part

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     id=None,
                     name=None,
                     description=None,
                     selected_by_default=None,
                     optional=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: part ID
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.parts``. When methods return
                a value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.parts``.
            :type  name: :class:`Parts.LocalizableMessage`
            :param name: part name id in message bundle
            :type  description: :class:`Parts.LocalizableMessage`
            :param description: part description id in message bundle
            :type  selected_by_default: :class:`bool`
            :param selected_by_default: Is part selected by default in UI
            :type  optional: :class:`bool`
            :param optional: Estimated size of this piece
            """
            self.id = id
            self.name = name
            self.description = description
            self.selected_by_default = selected_by_default
            self.optional = optional
            VapiStruct.__init__(self)

    Part._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.parts.part', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.parts'),
            'name': type.ReferenceType(sys.modules[__name__], 'Parts.LocalizableMessage'),
            'description': type.ReferenceType(sys.modules[__name__], 'Parts.LocalizableMessage'),
            'selected_by_default': type.BooleanType(),
            'optional': type.BooleanType(),
        },
        Part,
        False,
        None))



    def list(self):
        """
        Get a list of the backup parts


        :rtype: :class:`list` of :class:`Parts.Part`
        :return: list of parts
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            id,
            ):
        """
        Get size of the optional part

        :type  id: :class:`str`
        :param id: part id
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.parts``.
        :rtype: :class:`long`
        :return: int size
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'id': id,
                            })

class _JobStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.job'),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        cancel_input_validator_list = [
        ]
        cancel_output_validator_list = [
        ]

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'piece': type.ReferenceType(sys.modules[__name__], 'Job.BackupRequest'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.feature_in_use':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'FeatureInUse'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        create_input_validator_list = [
        ]
        create_output_validator_list = [
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.job'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'NotFound'),
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
                'output_type': type.ReferenceType(sys.modules[__name__], 'Job.BackupJobStatus'),
                'errors': create_error_dict,
                'input_validator_list': create_input_validator_list,
                'output_validator_list': create_output_validator_list,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Job.BackupJobStatus'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.recovery.backup.job',
                                  config=config,
                                  operations=operations)
class _PartsStub(ApiInterfaceStub):
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
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.parts'),
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
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Parts.Part')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.IntegerType(),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.recovery.backup.parts',
                                  config=config,
                                  operations=operations)

