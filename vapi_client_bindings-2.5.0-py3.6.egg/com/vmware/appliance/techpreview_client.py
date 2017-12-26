# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.
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


class Ntp(VapiInterface):
    """
    ``Ntp`` class provides methods Gets NTP configuration status and tests
    connection to ntp servers.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NtpStub)

    class NTPStatus(Enum):
        """
        ``Ntp.NTPStatus`` class Defines NTP status

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        Down = None
        """
        NTP daemon is not running.

        """
        Unknown = None
        """
        Cannot retrieve NTP daemon status.

        """
        Up = None
        """
        NTP daemon is running.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`NTPStatus` instance.
            """
            Enum.__init__(string)

    NTPStatus._set_values([
        NTPStatus('Down'),
        NTPStatus('Unknown'),
        NTPStatus('Up'),
    ])
    NTPStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.ntp.NTP_status',
        NTPStatus))


    class TestStatus(Enum):
        """
        ``Ntp.TestStatus`` class Health indicator

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        In case data has more than one test, this indicates not all tests were
        successful

        """
        green = None
        """
        All tests were successful for given data

        """
        red = None
        """
        All tests failed for given data

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`TestStatus` instance.
            """
            Enum.__init__(string)

    TestStatus._set_values([
        TestStatus('orange'),
        TestStatus('green'),
        TestStatus('red'),
    ])
    TestStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.ntp.test_status',
        TestStatus))


    class MessageStatus(Enum):
        """
        ``Ntp.MessageStatus`` class Individual test result

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        failure = None
        """
        message indicates the test failed.

        """
        success = None
        """
        message indicates that the test was successful.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`MessageStatus` instance.
            """
            Enum.__init__(string)

    MessageStatus._set_values([
        MessageStatus('failure'),
        MessageStatus('success'),
    ])
    MessageStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.ntp.message_status',
        MessageStatus))


    class NTPConfig(VapiStruct):
        """
        ``Ntp.NTPConfig`` class Structure defining the NTP configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     status=None,
                     servers=None,
                    ):
            """
            :type  status: :class:`Ntp.NTPStatus`
            :param status: NTP daemon running status
            :type  servers: :class:`list` of :class:`str`
            :param servers: List of NTP servers.
            """
            self.status = status
            self.servers = servers
            VapiStruct.__init__(self)

    NTPConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.ntp.NTP_config', {
            'status': type.ReferenceType(sys.modules[__name__], 'Ntp.NTPStatus'),
            'servers': type.ListType(type.StringType()),
        },
        NTPConfig,
        False,
        None))


    class Message(VapiStruct):
        """
        ``Ntp.Message`` class Test result and message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     message=None,
                     result=None,
                    ):
            """
            :type  message: :class:`str`
            :param message: message
            :type  result: :class:`Ntp.MessageStatus`
            :param result: result of the test
            """
            self.message = message
            self.result = result
            VapiStruct.__init__(self)

    Message._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.ntp.message', {
            'message': type.StringType(),
            'result': type.ReferenceType(sys.modules[__name__], 'Ntp.MessageStatus'),
        },
        Message,
        False,
        None))


    class TestStatusInfo(VapiStruct):
        """
        ``Ntp.TestStatusInfo`` class Overall test result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Ntp.TestStatus`
            :param status: Overall status of tests run.
            :type  messages: :class:`list` of :class:`Ntp.Message`
            :param messages: messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    TestStatusInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.ntp.test_status_info', {
            'status': type.ReferenceType(sys.modules[__name__], 'Ntp.TestStatus'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ntp.Message')),
        },
        TestStatusInfo,
        False,
        None))



    def test(self,
             servers,
             ):
        """
        Test the connection to a list of ntp servers.

        :type  servers: :class:`list` of :class:`str`
        :param servers: List of host names or IP addresses of NTP servers.
        :rtype: :class:`Ntp.TestStatusInfo`
        :return: NTP connection status
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('test',
                            {
                            'servers': servers,
                            })

    def get(self):
        """
        Get the NTP configuration status. If you run the 'timesync.get'
        command, you can retrieve the current time synchronization method (NTP-
        or VMware Tools-based). The 'ntp' command always returns the NTP server
        information, even when the time synchronization mode is not set to NTP.
        If the time synchronization mode is not NTP-based, the NTP server
        status is displayed as down.


        :rtype: :class:`Ntp.NTPConfig`
        :return: NTP config
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

class Services(VapiInterface):
    """
    ``Services`` class provides methods Manages services.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServicesStub)

    class ServiceOps(Enum):
        """
        ``Services.ServiceOps`` class Defines service operations

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        control = None
        """
        The service accepts arbitrary commands and arguments.

        """
        status = None
        """
        The service status can be generated.

        """
        stop = None
        """
        The service can be stopped.

        """
        restart = None
        """
        The service can be started or restarted.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ServiceOps` instance.
            """
            Enum.__init__(string)

    ServiceOps._set_values([
        ServiceOps('control'),
        ServiceOps('status'),
        ServiceOps('stop'),
        ServiceOps('restart'),
    ])
    ServiceOps._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.services.service_ops',
        ServiceOps))


    class ServiceInfo(VapiStruct):
        """
        ``Services.ServiceInfo`` class Structure that describes a service and the
        operations you can perform on a service.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     name=None,
                     description=None,
                     operations=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the service, for example, "vmware-vpxd". This name is
                unique per machine.
            :type  description: :class:`str`
            :param description: A description of the service. The description can be empty.
            :type  operations: :class:`list` of :class:`Services.ServiceOps`
            :param operations: The operations encoded in an array, supported by the service.
            """
            self.name = name
            self.description = description
            self.operations = operations
            VapiStruct.__init__(self)

    ServiceInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.services.service_info', {
            'name': type.StringType(),
            'description': type.StringType(),
            'operations': type.ListType(type.ReferenceType(sys.modules[__name__], 'Services.ServiceOps')),
        },
        ServiceInfo,
        False,
        None))



    def control(self,
                args,
                name,
                timeout,
                ):
        """
        Manage a service with arbitrary command and arguments.

        :type  args: :class:`list` of :class:`str`
        :param args: Array of arguments.
        :type  name: :class:`str`
        :param name: Name of the service.
        :type  timeout: :class:`long`
        :param timeout: Timeout in seconds. Zero (0) means no timeout.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('control',
                            {
                            'args': args,
                            'name': name,
                            'timeout': timeout,
                            })

    def list(self):
        """
        Get a list of all known services.


        :rtype: :class:`list` of :class:`Services.ServiceInfo`
        :return: List of services.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def stop(self,
             name,
             timeout,
             ):
        """
        Stop a service

        :type  name: :class:`str`
        :param name: Name of service.
        :type  timeout: :class:`long`
        :param timeout: Timeout in seconds. Zero (0) means no timeout.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('stop',
                            {
                            'name': name,
                            'timeout': timeout,
                            })

    def restart(self,
                name,
                timeout,
                ):
        """
        start or restart a service

        :type  name: :class:`str`
        :param name: Name of the service to start or restart.
        :type  timeout: :class:`long`
        :param timeout: Timeout in seconds. Zero (0) means no timeout.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('restart',
                            {
                            'name': name,
                            'timeout': timeout,
                            })

class Shutdown(VapiInterface):
    """
    ``Shutdown`` class provides methods Performs reboot/shutdow operations on
    appliance.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ShutdownStub)

    class ShutdownGetConfig(VapiStruct):
        """
        ``Shutdown.ShutdownGetConfig`` class Structure that defines shutdown
        configuration returned by Shutdown.get operation

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     shutdown_time=None,
                     action=None,
                     reason=None,
                    ):
            """
            :type  shutdown_time: :class:`str`
            :param shutdown_time: (UTC) time of shutdown represented in "YYYY-MM-DD HH:MM:SS" format.
            :type  action: :class:`str`
            :param action: Contains a string that describes the pending shutdown operation.
                The string values for pending operations can be 'poweroff',
                'reboot' or ''
            :type  reason: :class:`str`
            :param reason: This will contain string explaining the reason behind the shutdown
                action
            """
            self.shutdown_time = shutdown_time
            self.action = action
            self.reason = reason
            VapiStruct.__init__(self)

    ShutdownGetConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.shutdown.shutdown_get_config', {
            'shutdown_time': type.StringType(),
            'action': type.StringType(),
            'reason': type.StringType(),
        },
        ShutdownGetConfig,
        False,
        None))


    class ShutdownConfig(VapiStruct):
        """
        ``Shutdown.ShutdownConfig`` class Structure that defines shutdown
        configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     delay=None,
                     reason=None,
                    ):
            """
            :type  delay: :class:`long`
            :param delay: Delay interval in minutes (optional). if you do not specify delay,
                then the shutdown starts immediately.
            :type  reason: :class:`str`
            :param reason: Reason for performing shutdown (required).
            """
            self.delay = delay
            self.reason = reason
            VapiStruct.__init__(self)

    ShutdownConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.shutdown.shutdown_config', {
            'delay': type.IntegerType(),
            'reason': type.StringType(),
        },
        ShutdownConfig,
        False,
        None))



    def cancel(self):
        """
        Cancel pending shutdown action.


        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('cancel', None)

    def poweroff(self,
                 config,
                 ):
        """
        Power off the appliance.

        :type  config: :class:`Shutdown.ShutdownConfig`
        :param config: Configuration of poweroff action
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('poweroff',
                            {
                            'config': config,
                            })

    def reboot(self,
               config,
               ):
        """
        Reboot the appliance.

        :type  config: :class:`Shutdown.ShutdownConfig`
        :param config: Configuration of reboot action
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('reboot',
                            {
                            'config': config,
                            })

    def get(self):
        """
        Get details about the pending shutdown action.


        :rtype: :class:`Shutdown.ShutdownGetConfig`
        :return: Configuration of pending shutdown action.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

class Timesync(VapiInterface):
    """
    ``Timesync`` class provides methods Performs time synchronization
    configuration.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TimesyncStub)

    class TimeSyncMode(Enum):
        """
        ``Timesync.TimeSyncMode`` class Defines different timsync modes

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        Disabled = None
        """
        Time synchronization is disabled.

        """
        NTP = None
        """
        NTP-based time synchronization.

        """
        host = None
        """
        VMware Tool-based time synchronization.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`TimeSyncMode` instance.
            """
            Enum.__init__(string)

    TimeSyncMode._set_values([
        TimeSyncMode('Disabled'),
        TimeSyncMode('NTP'),
        TimeSyncMode('host'),
    ])
    TimeSyncMode._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.timesync.time_sync_mode',
        TimeSyncMode))


    class TimeSyncConfig(VapiStruct):
        """
        ``Timesync.TimeSyncConfig`` class Structure defining time synchronization
        configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     mode=None,
                    ):
            """
            :type  mode: :class:`Timesync.TimeSyncMode`
            :param mode: Time synchronization mode. Mode can have one of the TimeSyncMode
                enumeration values.
            """
            self.mode = mode
            VapiStruct.__init__(self)

    TimeSyncConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.timesync.time_sync_config', {
            'mode': type.ReferenceType(sys.modules[__name__], 'Timesync.TimeSyncMode'),
        },
        TimeSyncConfig,
        False,
        None))



    def set(self,
            config,
            ):
        """
        Set time synchronization configuration.

        :type  config: :class:`Timesync.TimeSyncConfig`
        :param config: Time synchronization configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def get(self):
        """
        Get time synchronization configuration.


        :rtype: :class:`Timesync.TimeSyncConfig`
        :return: Time synchronization configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

class _NtpStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'servers': type.ListType(type.StringType()),
        })
        test_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        test_input_validator_list = [
        ]
        test_output_validator_list = [
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
            'test': {
                'input_type': test_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Ntp.TestStatusInfo'),
                'errors': test_error_dict,
                'input_validator_list': test_input_validator_list,
                'output_validator_list': test_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Ntp.NTPConfig'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.ntp',
                                  config=config,
                                  operations=operations)
class _ServicesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for control operation
        control_input_type = type.StructType('operation-input', {
            'args': type.ListType(type.StringType()),
            'name': type.StringType(),
            'timeout': type.IntegerType(),
        })
        control_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        control_input_validator_list = [
        ]
        control_output_validator_list = [
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

        # properties for stop operation
        stop_input_type = type.StructType('operation-input', {
            'name': type.StringType(),
            'timeout': type.IntegerType(),
        })
        stop_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        stop_input_validator_list = [
        ]
        stop_output_validator_list = [
        ]

        # properties for restart operation
        restart_input_type = type.StructType('operation-input', {
            'name': type.StringType(),
            'timeout': type.IntegerType(),
        })
        restart_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        restart_input_validator_list = [
        ]
        restart_output_validator_list = [
        ]

        operations = {
            'control': {
                'input_type': control_input_type,
                'output_type': type.VoidType(),
                'errors': control_error_dict,
                'input_validator_list': control_input_validator_list,
                'output_validator_list': control_output_validator_list,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Services.ServiceInfo')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'stop': {
                'input_type': stop_input_type,
                'output_type': type.VoidType(),
                'errors': stop_error_dict,
                'input_validator_list': stop_input_validator_list,
                'output_validator_list': stop_output_validator_list,
            },
            'restart': {
                'input_type': restart_input_type,
                'output_type': type.VoidType(),
                'errors': restart_error_dict,
                'input_validator_list': restart_input_validator_list,
                'output_validator_list': restart_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.services',
                                  config=config,
                                  operations=operations)
class _ShutdownStub(ApiInterfaceStub):
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

        # properties for poweroff operation
        poweroff_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Shutdown.ShutdownConfig'),
        })
        poweroff_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        poweroff_input_validator_list = [
        ]
        poweroff_output_validator_list = [
        ]

        # properties for reboot operation
        reboot_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Shutdown.ShutdownConfig'),
        })
        reboot_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        reboot_input_validator_list = [
        ]
        reboot_output_validator_list = [
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
                'output_type': type.VoidType(),
                'errors': cancel_error_dict,
                'input_validator_list': cancel_input_validator_list,
                'output_validator_list': cancel_output_validator_list,
            },
            'poweroff': {
                'input_type': poweroff_input_type,
                'output_type': type.VoidType(),
                'errors': poweroff_error_dict,
                'input_validator_list': poweroff_input_validator_list,
                'output_validator_list': poweroff_output_validator_list,
            },
            'reboot': {
                'input_type': reboot_input_type,
                'output_type': type.VoidType(),
                'errors': reboot_error_dict,
                'input_validator_list': reboot_input_validator_list,
                'output_validator_list': reboot_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Shutdown.ShutdownGetConfig'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.shutdown',
                                  config=config,
                                  operations=operations)
class _TimesyncStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Timesync.TimeSyncConfig'),
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
                'output_type': type.ReferenceType(sys.modules[__name__], 'Timesync.TimeSyncConfig'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.timesync',
                                  config=config,
                                  operations=operations)

