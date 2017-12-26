# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.system.
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


class Update(VapiInterface):
    """
    ``Update`` class provides methods Performs update repository configuration.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpdateStub)

    class AutoUpdateNotification(Enum):
        """
        ``Update.AutoUpdateNotification`` class Defines state for automatic update
        notification

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        disabled = None
        """
        Automatic update notification is disabled. Disable periodically query the
        configured url for updates.

        """
        enabled = None
        """
        Automatic update notification is enabled. Enable periodically query the
        configured url for updates.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`AutoUpdateNotification` instance.
            """
            Enum.__init__(string)

    AutoUpdateNotification._set_values([
        AutoUpdateNotification('disabled'),
        AutoUpdateNotification('enabled'),
    ])
    AutoUpdateNotification._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.system.update.auto_update_notification',
        AutoUpdateNotification))


    class UpdateDay(Enum):
        """
        ``Update.UpdateDay`` class Defines days to query for updates

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        Monday = None
        """
        query for updates on Monday

        """
        Tuesday = None
        """
        query for updates on Tuesday

        """
        Friday = None
        """
        query for updates on Friday

        """
        Wednesday = None
        """
        query for updates on Wednesday

        """
        Thursday = None
        """
        query for updates on Thursday

        """
        Saturday = None
        """
        query for updates on Saturday

        """
        Sunday = None
        """
        query for updates on Sunday

        """
        Everyday = None
        """
        query for updates everyday

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`UpdateDay` instance.
            """
            Enum.__init__(string)

    UpdateDay._set_values([
        UpdateDay('Monday'),
        UpdateDay('Tuesday'),
        UpdateDay('Friday'),
        UpdateDay('Wednesday'),
        UpdateDay('Thursday'),
        UpdateDay('Saturday'),
        UpdateDay('Sunday'),
        UpdateDay('Everyday'),
    ])
    UpdateDay._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.system.update.update_day',
        UpdateDay))


    class UpdateStructSet(VapiStruct):
        """
        ``Update.UpdateStructSet`` class Structure to set url update repository.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     current_url=None,
                     check_updates=None,
                     time=None,
                     day=None,
                     username=None,
                     password=None,
                    ):
            """
            :type  current_url: :class:`str`
            :param current_url: Current appliance update repository URL. Enter "default" to reset
                the url to the default url.
            :type  check_updates: :class:`Update.AutoUpdateNotification`
            :param check_updates: Check for update at the pre-configured repository URL.
            :type  time: :class:`str`
            :param time: time to query for updates Format: HH:MM:SS Military (24 hour) Time
                Format
            :type  day: :class:`Update.UpdateDay`
            :param day: day to query for updates
            :type  username: :class:`str`
            :param username: username for the url update repository
            :type  password: :class:`str`
            :param password: password for the url update repository
            """
            self.current_url = current_url
            self.check_updates = check_updates
            self.time = time
            self.day = day
            self.username = username
            self.password = password
            VapiStruct.__init__(self, {
                                'current_URL': 'current_url',
                                })

    UpdateStructSet._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.system.update.update_struct_set', {
            'current_URL': type.StringType(),
            'check_updates': type.ReferenceType(sys.modules[__name__], 'Update.AutoUpdateNotification'),
            'time': type.StringType(),
            'day': type.ReferenceType(sys.modules[__name__], 'Update.UpdateDay'),
            'username': type.StringType(),
            'password': type.SecretType(),
        },
        UpdateStructSet,
        False,
        None))


    class UpdateStructGet(VapiStruct):
        """
        ``Update.UpdateStructGet`` class Structure to get url update repository.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     current_url=None,
                     default_url=None,
                     check_updates=None,
                     time=None,
                     day=None,
                     latest_update_install_time=None,
                     latest_update_query_time=None,
                     username=None,
                     password=None,
                    ):
            """
            :type  current_url: :class:`str`
            :param current_url: Current appliance update repository URL.
            :type  default_url: :class:`str`
            :param default_url: Default appliance update repository URL.
            :type  check_updates: :class:`Update.AutoUpdateNotification`
            :param check_updates: Check for update at the pre-configured repository URL.
            :type  time: :class:`str`
            :param time: time to query for updates Format: HH:MM:SS Military (24 hour) Time
                Format
            :type  day: :class:`Update.UpdateDay`
            :param day: day to query for updates
            :type  latest_update_install_time: :class:`str`
            :param latest_update_install_time: timestamp of latest update installation
            :type  latest_update_query_time: :class:`str`
            :param latest_update_query_time: timestamp of latest query to update repository
            :type  username: :class:`str`
            :param username: username for the url update repository
            :type  password: :class:`str`
            :param password: password for the url update repository
            """
            self.current_url = current_url
            self.default_url = default_url
            self.check_updates = check_updates
            self.time = time
            self.day = day
            self.latest_update_install_time = latest_update_install_time
            self.latest_update_query_time = latest_update_query_time
            self.username = username
            self.password = password
            VapiStruct.__init__(self, {
                                'current_URL': 'current_url',
                                'default_URL': 'default_url',
                                })

    UpdateStructGet._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.system.update.update_struct_get', {
            'current_URL': type.StringType(),
            'default_URL': type.StringType(),
            'check_updates': type.ReferenceType(sys.modules[__name__], 'Update.AutoUpdateNotification'),
            'time': type.StringType(),
            'day': type.ReferenceType(sys.modules[__name__], 'Update.UpdateDay'),
            'latest_update_install_time': type.StringType(),
            'latest_update_query_time': type.StringType(),
            'username': type.StringType(),
            'password': type.StringType(),
        },
        UpdateStructGet,
        False,
        None))



    def set(self,
            config,
            ):
        """
        Set update repository configuration.

        :type  config: :class:`Update.UpdateStructSet`
        :param config: update related configuration
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def get(self):
        """
        Get update repository configuration.


        :rtype: :class:`Update.UpdateStructGet`
        :return: update related configuration
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

class _UpdateStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Update.UpdateStructSet'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        set_input_validator_list = [
        ]
        set_output_validator_list = [
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
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_validator_list': set_input_validator_list,
                'output_validator_list': set_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Update.UpdateStructGet'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.system.update',
                                  config=config,
                                  operations=operations)

