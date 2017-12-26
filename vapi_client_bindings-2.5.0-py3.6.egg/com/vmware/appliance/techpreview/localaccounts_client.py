# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.localaccounts.
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


class User(VapiInterface):
    """
    ``User`` class provides methods Perform operations on local user account.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UserStub)

    class UserAccountStatus(Enum):
        """
        ``User.UserAccountStatus`` class Defines status of user accounts

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
        The user account is disabled.

        """
        enabled = None
        """
        The user account is enabled.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`UserAccountStatus` instance.
            """
            Enum.__init__(string)

    UserAccountStatus._set_values([
        UserAccountStatus('disabled'),
        UserAccountStatus('enabled'),
    ])
    UserAccountStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.localaccounts.user.user_account_status',
        UserAccountStatus))


    class UserPasswordStatus(Enum):
        """
        ``User.UserPasswordStatus`` class Defines state of user password

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        notset = None
        """
        No password has been set

        """
        expired = None
        """
        The password has expired.

        """
        valid = None
        """
        The password is still valid.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`UserPasswordStatus` instance.
            """
            Enum.__init__(string)

    UserPasswordStatus._set_values([
        UserPasswordStatus('notset'),
        UserPasswordStatus('expired'),
        UserPasswordStatus('valid'),
    ])
    UserPasswordStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.localaccounts.user.user_password_status',
        UserPasswordStatus))


    class UserRole(Enum):
        """
        ``User.UserRole`` class Defines user roles for appliance

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        admin = None
        """
        Able to configure the appliance.

        """
        operator = None
        """
        Able to read the appliance configuration.

        """
        superAdmin = None
        """
        Able to configure the appliance, manage local accounts and use the BASH
        shell

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`UserRole` instance.
            """
            Enum.__init__(string)

    UserRole._set_values([
        UserRole('admin'),
        UserRole('operator'),
        UserRole('superAdmin'),
    ])
    UserRole._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.localaccounts.user.user_role',
        UserRole))


    class UserConfigGet(VapiStruct):
        """
        ``User.UserConfigGet`` class Structure defines a user configuration for
        user.get API.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     username=None,
                     role=None,
                     fullname=None,
                     status=None,
                     passwordstatus=None,
                     email=None,
                    ):
            """
            :type  username: :class:`str`
            :param username: User login name
            :type  role: :class:`User.UserRole`
            :param role: User roles
            :type  fullname: :class:`str`
            :param fullname: User full name
            :type  status: :class:`User.UserAccountStatus`
            :param status: Shows whether the user account is enabled or disabled.
            :type  passwordstatus: :class:`User.UserPasswordStatus`
            :param passwordstatus: Shows whether the user account is still valid or expired.
            :type  email: :class:`str`
            :param email: Email address of the local account.
            """
            self.username = username
            self.role = role
            self.fullname = fullname
            self.status = status
            self.passwordstatus = passwordstatus
            self.email = email
            VapiStruct.__init__(self)

    UserConfigGet._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.localaccounts.user.user_config_get', {
            'username': type.StringType(),
            'role': type.ReferenceType(sys.modules[__name__], 'User.UserRole'),
            'fullname': type.StringType(),
            'status': type.ReferenceType(sys.modules[__name__], 'User.UserAccountStatus'),
            'passwordstatus': type.ReferenceType(sys.modules[__name__], 'User.UserPasswordStatus'),
            'email': type.StringType(),
        },
        UserConfigGet,
        False,
        None))


    class UserConfig(VapiStruct):
        """
        ``User.UserConfig`` class Structure that defines a new user configuration
        for CLI.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     username=None,
                     role=None,
                     fullname=None,
                     status=None,
                     email=None,
                    ):
            """
            :type  username: :class:`str`
            :param username: User login name
            :type  role: :class:`User.UserRole`
            :param role: User roles
            :type  fullname: :class:`str`
            :param fullname: User full name
            :type  status: :class:`User.UserAccountStatus`
            :param status: Enabled status of the local account
            :type  email: :class:`str`
            :param email: email of the local account
            """
            self.username = username
            self.role = role
            self.fullname = fullname
            self.status = status
            self.email = email
            VapiStruct.__init__(self)

    UserConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.localaccounts.user.user_config', {
            'username': type.StringType(),
            'role': type.ReferenceType(sys.modules[__name__], 'User.UserRole'),
            'fullname': type.StringType(),
            'status': type.ReferenceType(sys.modules[__name__], 'User.UserAccountStatus'),
            'email': type.StringType(),
        },
        UserConfig,
        False,
        None))


    class NewUserConfig(VapiStruct):
        """
        ``User.NewUserConfig`` class Structure that defines a new user
        configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     username=None,
                     role=None,
                     password=None,
                     fullname=None,
                     email=None,
                    ):
            """
            :type  username: :class:`str`
            :param username: User login name
            :type  role: :class:`User.UserRole` or ``None``
            :param role: User roles. The default role is operator.
                role Default role is operator
            :type  password: :class:`str`
            :param password: User login password In Interactive mode, provide --password as part
                of the command, and enter the value on the prompt. When accessed
                remotely, provide --password value as part the command.
            :type  fullname: :class:`str` or ``None``
            :param fullname: User full name
                fullname Optional full name for a person
            :type  email: :class:`str` or ``None``
            :param email: Email address of the local account.
                email Optional email
            """
            self.username = username
            self.role = role
            self.password = password
            self.fullname = fullname
            self.email = email
            VapiStruct.__init__(self)

    NewUserConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.localaccounts.user.new_user_config', {
            'username': type.StringType(),
            'role': type.OptionalType(type.ReferenceType(sys.modules[__name__], 'User.UserRole')),
            'password': type.SecretType(),
            'fullname': type.OptionalType(type.StringType()),
            'email': type.OptionalType(type.StringType()),
        },
        NewUserConfig,
        False,
        None))



    def delete(self,
               username,
               ):
        """
        Delete a local user account.

        :type  username: :class:`str`
        :param username: User login name.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('delete',
                            {
                            'username': username,
                            })

    def add(self,
            config,
            ):
        """
        Create a new local user account.

        :type  config: :class:`User.NewUserConfig`
        :param config: User configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('add',
                            {
                            'config': config,
                            })

    def set(self,
            config,
            ):
        """
        Update local user account properties role, full name, enabled status
        and password

        :type  config: :class:`User.UserConfig`
        :param config: User configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def list(self):
        """
        List of local accounts


        :rtype: :class:`list` of :class:`User.UserConfigGet`
        :return: User configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            username,
            ):
        """
        Get the local user account information.

        :type  username: :class:`str`
        :param username: User login name.
        :rtype: :class:`User.UserConfigGet`
        :return: local user account information
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'username': username,
                            })

class _UserStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'username': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        delete_input_validator_list = [
        ]
        delete_output_validator_list = [
        ]

        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'User.NewUserConfig'),
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
            'config': type.ReferenceType(sys.modules[__name__], 'User.UserConfig'),
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'username': type.StringType(),
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_validator_list': delete_input_validator_list,
                'output_validator_list': delete_output_validator_list,
            },
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
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'User.UserConfigGet')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'User.UserConfigGet'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.localaccounts.user',
                                  config=config,
                                  operations=operations)

