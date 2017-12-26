# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.networking.
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


class Ipv4(VapiInterface):
    """
    ``Ipv4`` class provides methods Performs IPV4 network configuration for
    interfaces.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _Ipv4Stub)

    class IPv4Mode(Enum):
        """
        ``Ipv4.IPv4Mode`` class Defines different ipv4 modes

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        dhcp = None
        """
        IPv4 address is automatically assigned by a DHCP server.

        """
        is_static = None
        """
        IPv4 address is static.

        """
        unconfigured = None
        """
        The IPv4 protocol is not configured.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IPv4Mode` instance.
            """
            Enum.__init__(string)

    IPv4Mode._set_values([
        IPv4Mode('dhcp'),
        IPv4Mode('is_static'),
        IPv4Mode('unconfigured'),
    ])
    IPv4Mode._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.networking.ipv4.I_pv4_mode',
        IPv4Mode))


    class IPv4Config(VapiStruct):
        """
        ``Ipv4.IPv4Config`` class Structure that defines the IPv4 configuration
        state of a network interface.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     interface_name=None,
                     mode=None,
                     address=None,
                     prefix=None,
                     default_gateway=None,
                    ):
            """
            :type  interface_name: :class:`str`
            :param interface_name: Interface name, for example, "nic0", "nic1".
            :type  mode: :class:`Ipv4.IPv4Mode`
            :param mode: Address assignment mode.
            :type  address: :class:`str`
            :param address: IPv4 address, for example, "10.20.80.191". Set this argument to an
                empty string "", if the mode is "unconfigured" or "dhcp".
            :type  prefix: :class:`long`
            :param prefix: IPv4 CIDR prefix, for example , 24. See
                http://www.oav.net/mirrors/cidr.html for netmask-to-prefix
                conversion. Set this argument to 0 if the mode is "unconfigured" or
                "dhcp".
            :type  default_gateway: :class:`str`
            :param default_gateway: IPv4 address of the default gateway. This default gateway value is
                used if the mode argument is set to "static" This configures the
                global default gateway on the appliance with the specified gateway
                address and interface. This gateway replaces the existing default
                gateway configured on the appliance. However, if the gateway
                address is link-local, then it is added for that interface. This
                does not support configuration of multiple global default gateways
                through different interfaces.
            """
            self.interface_name = interface_name
            self.mode = mode
            self.address = address
            self.prefix = prefix
            self.default_gateway = default_gateway
            VapiStruct.__init__(self)

    IPv4Config._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.ipv4.I_pv4_config', {
            'interface_name': type.StringType(),
            'mode': type.ReferenceType(sys.modules[__name__], 'Ipv4.IPv4Mode'),
            'address': type.StringType(),
            'prefix': type.IntegerType(),
            'default_gateway': type.StringType(),
        },
        IPv4Config,
        False,
        None))


    class IPv4ConfigReadOnly(VapiStruct):
        """
        ``Ipv4.IPv4ConfigReadOnly`` class Structure that defines the IPv4
        configuration state of a network interface.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     interface_name=None,
                     mode=None,
                     address=None,
                     prefix=None,
                     default_gateway=None,
                     updateable=None,
                    ):
            """
            :type  interface_name: :class:`str`
            :param interface_name: Interface name, for example, "nic0", "nic1".
            :type  mode: :class:`Ipv4.IPv4Mode`
            :param mode: Address assignment mode.
            :type  address: :class:`str`
            :param address: IPv4 address, for example, "10.20.80.191". Set this argument to an
                empty string "", if the mode is "unconfigured" or "dhcp".
            :type  prefix: :class:`long`
            :param prefix: IPv4 CIDR prefix, for example , 24. See
                http://www.oav.net/mirrors/cidr.html for netmask-to-prefix
                conversion. Set this argument to 0 if the mode is "unconfigured" or
                "dhcp".
            :type  default_gateway: :class:`str`
            :param default_gateway: IPv4 address of the default gateway. This default gateway value is
                used if the mode argument is set to "static" This configures the
                global default gateway on the appliance with the specified gateway
                address and interface. This gateway replaces the existing default
                gateway configured on the appliance. However, if the gateway
                address is link-local, then it is added for that interface. This
                does not support configuration of multiple global default gateways
                through different interfaces.
            :type  updateable: :class:`bool`
            :param updateable: This indicates if the network configuration can be updated for the
                interface.
            """
            self.interface_name = interface_name
            self.mode = mode
            self.address = address
            self.prefix = prefix
            self.default_gateway = default_gateway
            self.updateable = updateable
            VapiStruct.__init__(self)

    IPv4ConfigReadOnly._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.ipv4.I_pv4_config_read_only', {
            'interface_name': type.StringType(),
            'mode': type.ReferenceType(sys.modules[__name__], 'Ipv4.IPv4Mode'),
            'address': type.StringType(),
            'prefix': type.IntegerType(),
            'default_gateway': type.StringType(),
            'updateable': type.BooleanType(),
        },
        IPv4ConfigReadOnly,
        False,
        None))



    def renew(self,
              interfaces,
              ):
        """
        Renew IPv4 network configuration on interfaces. If the interface is
        configured to use DHCP for IP address assignment, the lease of the
        interface is renewed.

        :type  interfaces: :class:`list` of :class:`str`
        :param interfaces: Interfaces to renew.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('renew',
                            {
                            'interfaces': interfaces,
                            })

    def set(self,
            config,
            ):
        """
        Set IPv4 network configuration.

        :type  config: :class:`list` of :class:`Ipv4.IPv4Config`
        :param config: List of IPv4 configurations.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def list(self):
        """
        Get IPv4 network configuration for all configured interfaces.


        :rtype: :class:`list` of :class:`Ipv4.IPv4ConfigReadOnly`
        :return: IPv4 configuration for each interface.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            interfaces,
            ):
        """
        Get IPv4 network configuration for interfaces.

        :type  interfaces: :class:`list` of :class:`str`
        :param interfaces: Network interfaces to query, for example, "nic0".
        :rtype: :class:`list` of :class:`Ipv4.IPv4ConfigReadOnly`
        :return: IPv4 configuration for each queried interface.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'interfaces': interfaces,
                            })

class Ipv6(VapiInterface):
    """
    ``Ipv6`` class provides methods Performs IPV4 network configuration for
    interfaces.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _Ipv6Stub)

    class IPv6AddressOrigin(Enum):
        """
        ``Ipv6.IPv6AddressOrigin`` class Defines IPV6 address origin values

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        dhcp = None
        """
        The IPv6 address is assigned by a DHCP server. See RFC 4293.

        """
        random = None
        """
        The IPv6 address is assigned randomly by the system. See RFC 4293.

        """
        manual = None
        """
        The IPv6 address was manually configured to a specified address, for,
        example, by user configuration. See RFC 4293.

        """
        other = None
        """
        The IPv6 address is assigned by a mechanism other than manual, DHCP, SLAAC,
        or random. See RFC 4293.

        """
        linklayer = None
        """
        The IPv6 address is assigned by IPv6 Stateless Address Auto-configuration
        (SLAAC). See RFC 4293.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IPv6AddressOrigin` instance.
            """
            Enum.__init__(string)

    IPv6AddressOrigin._set_values([
        IPv6AddressOrigin('dhcp'),
        IPv6AddressOrigin('random'),
        IPv6AddressOrigin('manual'),
        IPv6AddressOrigin('other'),
        IPv6AddressOrigin('linklayer'),
    ])
    IPv6AddressOrigin._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.networking.ipv6.I_pv6_address_origin',
        IPv6AddressOrigin))


    class IPv6AddressStatus(Enum):
        """
        ``Ipv6.IPv6AddressStatus`` class Defines IPV6 address status values

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        tentative = None
        """
        This IPv6 address is in the process of being verified as unique. Do not use
        addresses in this state for general communication. You can use them to
        determine the uniqueness of the address. See RFC 4293.

        """
        unknown = None
        """
        The status of this address cannot be determined. See RFC 4293.

        """
        inaccessible = None
        """
        This IPv6 address is inaccessible because the interface to which this
        address is assigned is not operational. See RFC 4293.

        """
        invalid = None
        """
        This IPv6 address is not a valid address. It should not appear as the
        destination or source address of a packet. See RFC 4293.

        """
        duplicate = None
        """
        This IPv6 address is not unique on the link. Do use this IPv6 address. See
        RFC 4293.

        """
        preferred = None
        """
        This is a valid IPv6 address that can appear as the destination or source
        address of a packet. See RFC 4293.

        """
        deprecated = None
        """
        This is a valid but deprecated IPv6 address. Do not use this IPv6 address
        as a source address in new communications, although packets addressed to
        such an address are processed as expected. See RFC 4293.

        """
        optimistic = None
        """
        This IPv6 address is available for use, subject to restrictions, while its
        uniqueness on a link is being verified. See RFC 4293.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IPv6AddressStatus` instance.
            """
            Enum.__init__(string)

    IPv6AddressStatus._set_values([
        IPv6AddressStatus('tentative'),
        IPv6AddressStatus('unknown'),
        IPv6AddressStatus('inaccessible'),
        IPv6AddressStatus('invalid'),
        IPv6AddressStatus('duplicate'),
        IPv6AddressStatus('preferred'),
        IPv6AddressStatus('deprecated'),
        IPv6AddressStatus('optimistic'),
    ])
    IPv6AddressStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.networking.ipv6.I_pv6_address_status',
        IPv6AddressStatus))


    class IPv6AddressReadOnly(VapiStruct):
        """
        ``Ipv6.IPv6AddressReadOnly`` class Structure that you can use to get
        information about an IPv6 address along with its origin and status.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     address=None,
                     prefix=None,
                     origin=None,
                     status=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: IPv6 address, for example, fc00:10:20:83:20c:29ff:fe94:bb5a.
            :type  prefix: :class:`long`
            :param prefix: IPv6 CIDR prefix, for example, 64.
            :type  origin: :class:`Ipv6.IPv6AddressOrigin`
            :param origin: Origin of the IPv6 address. For more information, see RFC 4293.
            :type  status: :class:`Ipv6.IPv6AddressStatus`
            :param status: Status of the IPv6 address. For more information, see RFC 4293.
            """
            self.address = address
            self.prefix = prefix
            self.origin = origin
            self.status = status
            VapiStruct.__init__(self)

    IPv6AddressReadOnly._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.ipv6.I_pv6_address_read_only', {
            'address': type.StringType(),
            'prefix': type.IntegerType(),
            'origin': type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6AddressOrigin'),
            'status': type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6AddressStatus'),
        },
        IPv6AddressReadOnly,
        False,
        None))


    class IPv6ConfigReadOnly(VapiStruct):
        """
        ``Ipv6.IPv6ConfigReadOnly`` class Structure that defines an existing IPv6
        configuration on a particular interface. This structure is read only.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     interface_name=None,
                     dhcp=None,
                     autoconf=None,
                     addresses=None,
                     default_gateway=None,
                     updateable=None,
                    ):
            """
            :type  interface_name: :class:`str`
            :param interface_name: Network interface, for example, "nic0" queried.
            :type  dhcp: :class:`bool`
            :param dhcp: Address assigned by a DHCP server.
            :type  autoconf: :class:`bool`
            :param autoconf: Address is assigned by Stateless Address Autoconfiguration (SLAAC).
            :type  addresses: :class:`list` of :class:`Ipv6.IPv6AddressReadOnly`
            :param addresses: A list of all addresses assigned to this interface. The origin
                field of each address determines how the address was assigned, for
                example, statically, by DHCP, SLAAC.
            :type  default_gateway: :class:`str`
            :param default_gateway: Default gateway. This configures the global IPv6 default gateway on
                the appliance with the specified gateway address and interface.
                This gateway replaces the existing default gateway configured on
                the appliance. However, if the gateway address is link-local, then
                it is added for that interface. This does not support configuration
                of multiple global default gateways through different interfaces.
            :type  updateable: :class:`bool`
            :param updateable: This indicates if the network configuration can be updated for the
                interface.
            """
            self.interface_name = interface_name
            self.dhcp = dhcp
            self.autoconf = autoconf
            self.addresses = addresses
            self.default_gateway = default_gateway
            self.updateable = updateable
            VapiStruct.__init__(self)

    IPv6ConfigReadOnly._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.ipv6.I_pv6_config_read_only', {
            'interface_name': type.StringType(),
            'dhcp': type.BooleanType(),
            'autoconf': type.BooleanType(),
            'addresses': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6AddressReadOnly')),
            'default_gateway': type.StringType(),
            'updateable': type.BooleanType(),
        },
        IPv6ConfigReadOnly,
        False,
        None))


    class IPv6Address(VapiStruct):
        """
        ``Ipv6.IPv6Address`` class Structure used to name an IPv6 address.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     address=None,
                     prefix=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: IPv6 address, for example, fc00:10:20:83:20c:29ff:fe94:bb5a.
            :type  prefix: :class:`long`
            :param prefix: IPv6 CIDR prefix, for example, 64.
            """
            self.address = address
            self.prefix = prefix
            VapiStruct.__init__(self)

    IPv6Address._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.ipv6.I_pv6_address', {
            'address': type.StringType(),
            'prefix': type.IntegerType(),
        },
        IPv6Address,
        False,
        None))


    class IPv6Config(VapiStruct):
        """
        ``Ipv6.IPv6Config`` class Structure that you can use to configure IPv6 on a
        particular interface. Because IPv6 permits multiple addresses per
        interface, addresses can be assigned by DHCP, SLAAC, and can also be
        statically assigned.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     interface_name=None,
                     dhcp=None,
                     autoconf=None,
                     addresses=None,
                     default_gateway=None,
                    ):
            """
            :type  interface_name: :class:`str`
            :param interface_name: Network interface, for example, "nic0" to configure.
            :type  dhcp: :class:`bool`
            :param dhcp: Address assigned by a DHCP server.
            :type  autoconf: :class:`bool`
            :param autoconf: Address is assigned by Stateless Address Autoconfiguration (SLAAC).
            :type  addresses: :class:`list` of :class:`Ipv6.IPv6Address`
            :param addresses: A list of addresses to be statically assigned.
            :type  default_gateway: :class:`str`
            :param default_gateway: Default gateway for static IP address assignment. This configures
                the global IPv6 default gateway on the appliance with the specified
                gateway address and interface. This gateway replaces the existing
                default gateway configured on the appliance. However, if the
                gateway address is link-local, then it is added for that interface.
                This does not support configuration of multiple global default
                gateways through different interfaces.
            """
            self.interface_name = interface_name
            self.dhcp = dhcp
            self.autoconf = autoconf
            self.addresses = addresses
            self.default_gateway = default_gateway
            VapiStruct.__init__(self)

    IPv6Config._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.ipv6.I_pv6_config', {
            'interface_name': type.StringType(),
            'dhcp': type.BooleanType(),
            'autoconf': type.BooleanType(),
            'addresses': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6Address')),
            'default_gateway': type.StringType(),
        },
        IPv6Config,
        False,
        None))



    def set(self,
            config,
            ):
        """
        Set IPv6 network configuration.

        :type  config: :class:`list` of :class:`Ipv6.IPv6Config`
        :param config: IPv6 configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def list(self):
        """
        Get IPv6 network configuration for all configured interfaces.


        :rtype: :class:`list` of :class:`Ipv6.IPv6ConfigReadOnly`
        :return: IPv6 configuration for each interface.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            interfaces,
            ):
        """
        Get IPv6 network configuration for interfaces.

        :type  interfaces: :class:`list` of :class:`str`
        :param interfaces: Network interfaces to query, for example, "nic0".
        :rtype: :class:`list` of :class:`Ipv6.IPv6ConfigReadOnly`
        :return: IPv6 configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'interfaces': interfaces,
                            })

class Proxy(VapiInterface):
    """
    ``Proxy`` class provides methods Proxy configuration.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProxyStub)

    class ProxyProtocol(Enum):
        """
        ``Proxy.ProxyProtocol`` class Defines different proxy protocols

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        ftp = None
        """
        proxy configuration for ftp.

        """
        http = None
        """
        proxy configuration for http.

        """
        https = None
        """
        proxy configuration for https.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ProxyProtocol` instance.
            """
            Enum.__init__(string)

    ProxyProtocol._set_values([
        ProxyProtocol('ftp'),
        ProxyProtocol('http'),
        ProxyProtocol('https'),
    ])
    ProxyProtocol._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.networking.proxy.proxy_protocol',
        ProxyProtocol))


    class TestStatus(Enum):
        """
        ``Proxy.TestStatus`` class Health indicator

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
        'com.vmware.appliance.techpreview.networking.proxy.test_status',
        TestStatus))


    class MessageStatus(Enum):
        """
        ``Proxy.MessageStatus`` class Individual test result

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
        'com.vmware.appliance.techpreview.networking.proxy.message_status',
        MessageStatus))


    class ProxyStatus(Enum):
        """
        ``Proxy.ProxyStatus`` class Defines state of proxy

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
        proxy configuration is disabled

        """
        enabled = None
        """
        proxy configuration is enabled

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ProxyStatus` instance.
            """
            Enum.__init__(string)

    ProxyStatus._set_values([
        ProxyStatus('disabled'),
        ProxyStatus('enabled'),
    ])
    ProxyStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.networking.proxy.proxy_status',
        ProxyStatus))


    class Message(VapiStruct):
        """
        ``Proxy.Message`` class Test result and message

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
            :type  result: :class:`Proxy.MessageStatus`
            :param result: result of the test
            """
            self.message = message
            self.result = result
            VapiStruct.__init__(self)

    Message._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.proxy.message', {
            'message': type.StringType(),
            'result': type.ReferenceType(sys.modules[__name__], 'Proxy.MessageStatus'),
        },
        Message,
        False,
        None))


    class TestStatusInfo(VapiStruct):
        """
        ``Proxy.TestStatusInfo`` class Overall test result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Proxy.TestStatus`
            :param status: Overall status of tests run.
            :type  messages: :class:`list` of :class:`Proxy.Message`
            :param messages: messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    TestStatusInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.proxy.test_status_info', {
            'status': type.ReferenceType(sys.modules[__name__], 'Proxy.TestStatus'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Proxy.Message')),
        },
        TestStatusInfo,
        False,
        None))


    class ProxyConfigTest(VapiStruct):
        """
        ``Proxy.ProxyConfigTest`` class Structure that defines proxy configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     protocol=None,
                     server=None,
                     port=None,
                     username=None,
                     password=None,
                     testhost=None,
                    ):
            """
            :type  protocol: :class:`Proxy.ProxyProtocol`
            :param protocol: protocol being configured.
            :type  server: :class:`str`
            :param server: hostname or ip of proxy server
            :type  port: :class:`long`
            :param port: port to connect to the proxy server on. A value of -1 indicates
                that the default port is being used.
            :type  username: :class:`str`
            :param username: username for proxy server.
            :type  password: :class:`str`
            :param password: password for proxy server.
            :type  testhost: :class:`str`
            :param testhost: Verify that a hostname (www.vmware.com) or IPv4 or Ipv6 address of
                the testhost is accessible through proxy.
            """
            self.protocol = protocol
            self.server = server
            self.port = port
            self.username = username
            self.password = password
            self.testhost = testhost
            VapiStruct.__init__(self)

    ProxyConfigTest._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.proxy.proxy_config_test', {
            'protocol': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyProtocol'),
            'server': type.StringType(),
            'port': type.IntegerType(),
            'username': type.StringType(),
            'password': type.SecretType(),
            'testhost': type.StringType(),
        },
        ProxyConfigTest,
        False,
        None))


    class ProxyConfig(VapiStruct):
        """
        ``Proxy.ProxyConfig`` class Structure that defines proxy configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     protocol=None,
                     server=None,
                     port=None,
                     username=None,
                     password=None,
                    ):
            """
            :type  protocol: :class:`Proxy.ProxyProtocol`
            :param protocol: protocol being configured.
            :type  server: :class:`str`
            :param server: hostname or ip of proxy server
            :type  port: :class:`long`
            :param port: port to connect to the proxy server on. A value of -1 indicates
                that the default port is being used.
            :type  username: :class:`str`
            :param username: username for proxy server.
            :type  password: :class:`str`
            :param password: password for proxy server.
            """
            self.protocol = protocol
            self.server = server
            self.port = port
            self.username = username
            self.password = password
            VapiStruct.__init__(self)

    ProxyConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.proxy.proxy_config', {
            'protocol': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyProtocol'),
            'server': type.StringType(),
            'port': type.IntegerType(),
            'username': type.StringType(),
            'password': type.SecretType(),
        },
        ProxyConfig,
        False,
        None))


    class ProxyConfigMultiple(VapiStruct):
        """
        ``Proxy.ProxyConfigMultiple`` class Structure representing multiple proxy
        configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     status=None,
                     configlist=None,
                    ):
            """
            :type  status: :class:`Proxy.ProxyStatus`
            :param status: proxy enabled or disabled This sets whether the proxy configuration
                is used.
            :type  configlist: :class:`list` of :class:`Proxy.ProxyConfig`
            :param configlist: List of proxy configuration.
            """
            self.status = status
            self.configlist = configlist
            VapiStruct.__init__(self)

    ProxyConfigMultiple._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.proxy.proxy_config_multiple', {
            'status': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyStatus'),
            'configlist': type.ListType(type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyConfig')),
        },
        ProxyConfigMultiple,
        False,
        None))



    def test(self,
             config,
             ):
        """
        Test a Proxy configuration by testing the connection to the proxy
        server and test host.

        :type  config: :class:`Proxy.ProxyConfigTest`
        :param config: Proxy configuration to test
        :rtype: :class:`Proxy.TestStatusInfo`
        :return: Status of proxy settings.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('test',
                            {
                            'config': config,
                            })

    def set(self,
            config,
            ):
        """
        Set Proxy configuration. In order for this configuration to take effect
        a logout is required.

        :type  config: :class:`Proxy.ProxyConfigMultiple`
        :param config: List of Proxy configurations to be set.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def delete(self,
               protocol,
               ):
        """
        Delete a Proxy configuration for a specific protocol.

        :type  protocol: :class:`Proxy.ProxyProtocol`
        :param protocol: Protocol to delete proxy of.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('delete',
                            {
                            'protocol': protocol,
                            })

    def get(self):
        """
        Get proxy configuration for all protocols.


        :rtype: :class:`Proxy.ProxyConfigMultiple`
        :return: proxy configuration for all protocols.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

class Routes(VapiInterface):
    """
    ``Routes`` class provides methods Performs networking routes operations.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RoutesStub)

    class TestStatus(Enum):
        """
        ``Routes.TestStatus`` class Health indicator

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
        'com.vmware.appliance.techpreview.networking.routes.test_status',
        TestStatus))


    class MessageStatus(Enum):
        """
        ``Routes.MessageStatus`` class Individual test result

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
        'com.vmware.appliance.techpreview.networking.routes.message_status',
        MessageStatus))


    class RouteReadOnly(VapiStruct):
        """
        ``Routes.RouteReadOnly`` class Structure that describes how routing is
        performed for a particular destination and prefix. A destination/prefix of
        0.0.0.0/0 ( for IPv4) or ::/0 (for IPv6) refers to the default gateway.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     destination=None,
                     prefix=None,
                     gateway=None,
                     interface_name=None,
                     is_static=None,
                    ):
            """
            :type  destination: :class:`str`
            :param destination: Destination address that defines this route.
            :type  prefix: :class:`long`
            :param prefix: Destination CIDR prefix that defines this route. See
                http://www.oav.net/mirrors/cidr.html for netmask-to-prefix
                conversion.
            :type  gateway: :class:`str`
            :param gateway: Gateway address.
            :type  interface_name: :class:`str`
            :param interface_name: Output device interface, for example, "nic0".
            :type  is_static: :class:`bool`
            :param is_static: Static provides information about installation of the route. True
                indicates the route was installed by the administrator. False
                indicates the route was autoconfigured
            """
            self.destination = destination
            self.prefix = prefix
            self.gateway = gateway
            self.interface_name = interface_name
            self.is_static = is_static
            VapiStruct.__init__(self)

    RouteReadOnly._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.routes.route_read_only', {
            'destination': type.StringType(),
            'prefix': type.IntegerType(),
            'gateway': type.StringType(),
            'interface_name': type.StringType(),
            'is_static': type.BooleanType(),
        },
        RouteReadOnly,
        False,
        None))


    class Route(VapiStruct):
        """
        ``Routes.Route`` class Structure that describes how routing is performed
        for a particular destination and prefix. A destination/prefix of 0.0.0.0/0
        ( for IPv4) or ::/0 (for IPv6) refers to the default gateway.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     destination=None,
                     prefix=None,
                     gateway=None,
                     interface_name=None,
                    ):
            """
            :type  destination: :class:`str`
            :param destination: Destination address that defines this route.
            :type  prefix: :class:`long`
            :param prefix: Destination CIDR prefix that defines this route. See
                http://www.oav.net/mirrors/cidr.html for netmask-to-prefix
                conversion.
            :type  gateway: :class:`str`
            :param gateway: Gateway address.
            :type  interface_name: :class:`str`
            :param interface_name: Output device interface, for example, "nic0".
            """
            self.destination = destination
            self.prefix = prefix
            self.gateway = gateway
            self.interface_name = interface_name
            VapiStruct.__init__(self)

    Route._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.routes.route', {
            'destination': type.StringType(),
            'prefix': type.IntegerType(),
            'gateway': type.StringType(),
            'interface_name': type.StringType(),
        },
        Route,
        False,
        None))


    class Message(VapiStruct):
        """
        ``Routes.Message`` class Test result and message

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
            :type  result: :class:`Routes.MessageStatus`
            :param result: result of the test
            """
            self.message = message
            self.result = result
            VapiStruct.__init__(self)

    Message._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.routes.message', {
            'message': type.StringType(),
            'result': type.ReferenceType(sys.modules[__name__], 'Routes.MessageStatus'),
        },
        Message,
        False,
        None))


    class TestStatusInfo(VapiStruct):
        """
        ``Routes.TestStatusInfo`` class Overall test result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Routes.TestStatus`
            :param status: Overall status of tests run.
            :type  messages: :class:`list` of :class:`Routes.Message`
            :param messages: messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    TestStatusInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.networking.routes.test_status_info', {
            'status': type.ReferenceType(sys.modules[__name__], 'Routes.TestStatus'),
            'messages': type.ListType(type.ReferenceType(sys.modules[__name__], 'Routes.Message')),
        },
        TestStatusInfo,
        False,
        None))



    def test(self,
             gateways,
             ):
        """
        Test connection to a list of gateways

        :type  gateways: :class:`list` of :class:`str`
        :param gateways: list of gateways.
        :rtype: :class:`Routes.TestStatusInfo`
        :return: connection status
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('test',
                            {
                            'gateways': gateways,
                            })

    def add(self,
            route,
            ):
        """
        Set static routing rules. A destination of 0.0.0.0 and prefix 0 (for
        IPv4) or destination of :: and prefix 0 (for IPv6) refers to the
        default gateway.

        :type  route: :class:`Routes.Route`
        :param route: Static routing rule.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('add',
                            {
                            'route': route,
                            })

    def set(self,
            routes,
            ):
        """
        Set static routing rules. A destination of 0.0.0.0 and prefix 0 (for
        IPv4) or destination of :: and prefix 0 (for IPv6) refers to the
        default gateway.

        :type  routes: :class:`list` of :class:`Routes.Route`
        :param routes: Static routing rules.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'routes': routes,
                            })

    def list(self):
        """
        Get main routing table. A destination of 0.0.0.0 and prefix 0 (for
        IPv4) or destination of :: and prefix 0 (for IPv6) refers to the
        default gateway.


        :rtype: :class:`list` of :class:`Routes.RouteReadOnly`
        :return: Routing table.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def delete(self,
               route,
               ):
        """
        Delete static routing rules.

        :type  route: :class:`Routes.Route`
        :param route: Static routing rule.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('delete',
                            {
                            'route': route,
                            })

class _Ipv4Stub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for renew operation
        renew_input_type = type.StructType('operation-input', {
            'interfaces': type.ListType(type.StringType()),
        })
        renew_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        renew_input_validator_list = [
        ]
        renew_output_validator_list = [
        ]

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv4.IPv4Config')),
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
            'interfaces': type.ListType(type.StringType()),
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
            'renew': {
                'input_type': renew_input_type,
                'output_type': type.VoidType(),
                'errors': renew_error_dict,
                'input_validator_list': renew_input_validator_list,
                'output_validator_list': renew_output_validator_list,
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
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv4.IPv4ConfigReadOnly')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv4.IPv4ConfigReadOnly')),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.networking.ipv4',
                                  config=config,
                                  operations=operations)
class _Ipv6Stub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6Config')),
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
            'interfaces': type.ListType(type.StringType()),
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
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_validator_list': set_input_validator_list,
                'output_validator_list': set_output_validator_list,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6ConfigReadOnly')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Ipv6.IPv6ConfigReadOnly')),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.networking.ipv6',
                                  config=config,
                                  operations=operations)
class _ProxyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyConfigTest'),
        })
        test_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        test_input_validator_list = [
        ]
        test_output_validator_list = [
        ]

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyConfigMultiple'),
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
            'protocol': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyProtocol'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        delete_input_validator_list = [
        ]
        delete_output_validator_list = [
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
                'output_type': type.ReferenceType(sys.modules[__name__], 'Proxy.TestStatusInfo'),
                'errors': test_error_dict,
                'input_validator_list': test_input_validator_list,
                'output_validator_list': test_output_validator_list,
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Proxy.ProxyConfigMultiple'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.networking.proxy',
                                  config=config,
                                  operations=operations)
class _RoutesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'gateways': type.ListType(type.StringType()),
        })
        test_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        test_input_validator_list = [
        ]
        test_output_validator_list = [
        ]

        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'route': type.ReferenceType(sys.modules[__name__], 'Routes.Route'),
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
            'routes': type.ListType(type.ReferenceType(sys.modules[__name__], 'Routes.Route')),
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

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'route': type.ReferenceType(sys.modules[__name__], 'Routes.Route'),
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
            'test': {
                'input_type': test_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Routes.TestStatusInfo'),
                'errors': test_error_dict,
                'input_validator_list': test_input_validator_list,
                'output_validator_list': test_output_validator_list,
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
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Routes.RouteReadOnly')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_validator_list': delete_input_validator_list,
                'output_validator_list': delete_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.networking.routes',
                                  config=config,
                                  operations=operations)

