# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.techpreview.monitoring.
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


class Snmp(VapiInterface):
    """
    ``Snmp`` class provides methods SNMP agent operations.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SnmpStub)

    class SNMPAuthProto(Enum):
        """
        ``Snmp.SNMPAuthProto`` class Defines SNMP authentication protocols

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        none = None
        """
        NONE

        """
        SHA1 = None
        """
        SHA1

        """
        MD5 = None
        """
        MD5

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SNMPAuthProto` instance.
            """
            Enum.__init__(string)

    SNMPAuthProto._set_values([
        SNMPAuthProto('none'),
        SNMPAuthProto('SHA1'),
        SNMPAuthProto('MD5'),
    ])
    SNMPAuthProto._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_auth_proto',
        SNMPAuthProto))


    class SNMPPrivProto(Enum):
        """
        ``Snmp.SNMPPrivProto`` class Defines SNMP privacy protocols

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        AES128 = None
        """
        AES128

        """
        none = None
        """
        NONE

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SNMPPrivProto` instance.
            """
            Enum.__init__(string)

    SNMPPrivProto._set_values([
        SNMPPrivProto('AES128'),
        SNMPPrivProto('none'),
    ])
    SNMPPrivProto._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_priv_proto',
        SNMPPrivProto))


    class SNMPSecLevel(Enum):
        """
        ``Snmp.SNMPSecLevel`` class Defines SNMP decurity levels

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        none = None
        """
        none

        """
        auth = None
        """
        auth

        """
        priv = None
        """
        priv

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SNMPSecLevel` instance.
            """
            Enum.__init__(string)

    SNMPSecLevel._set_values([
        SNMPSecLevel('none'),
        SNMPSecLevel('auth'),
        SNMPSecLevel('priv'),
    ])
    SNMPSecLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_sec_level',
        SNMPSecLevel))


    class SNMPv3Notfication(Enum):
        """
        ``Snmp.SNMPv3Notfication`` class Defines SNMP v3 notification types

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        inform = None
        """
        inform

        """
        trap = None
        """
        trap

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SNMPv3Notfication` instance.
            """
            Enum.__init__(string)

    SNMPv3Notfication._set_values([
        SNMPv3Notfication('inform'),
        SNMPv3Notfication('trap'),
    ])
    SNMPv3Notfication._set_binding_type(type.EnumType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNM_pv3_notfication',
        SNMPv3Notfication))


    class SNMPLimits(VapiStruct):
        """
        ``Snmp.SNMPLimits`` class Structure that provides various limits of the
        SNMP agent.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     max_communities=None,
                     max_trap_destinations_v1=None,
                     max_destinations_v3=None,
                     max_notification_filters=None,
                     max_community_length=None,
                     max_buffer_size=None,
                    ):
            """
            :type  max_communities: :class:`long`
            :param max_communities: Set up maximum communities limit
            :type  max_trap_destinations_v1: :class:`long`
            :param max_trap_destinations_v1: Set up max trap destinations limit
            :type  max_destinations_v3: :class:`long`
            :param max_destinations_v3: Set up max destinations limit
            :type  max_notification_filters: :class:`long`
            :param max_notification_filters: Set up max notification Filters
            :type  max_community_length: :class:`long`
            :param max_community_length: Set up max community length
            :type  max_buffer_size: :class:`long`
            :param max_buffer_size: Set up max buffer size
            """
            self.max_communities = max_communities
            self.max_trap_destinations_v1 = max_trap_destinations_v1
            self.max_destinations_v3 = max_destinations_v3
            self.max_notification_filters = max_notification_filters
            self.max_community_length = max_community_length
            self.max_buffer_size = max_buffer_size
            VapiStruct.__init__(self)

    SNMPLimits._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_limits', {
            'max_communities': type.IntegerType(),
            'max_trap_destinations_v1': type.IntegerType(),
            'max_destinations_v3': type.IntegerType(),
            'max_notification_filters': type.IntegerType(),
            'max_community_length': type.IntegerType(),
            'max_buffer_size': type.IntegerType(),
        },
        SNMPLimits,
        False,
        None))


    class SNMPTestResults(VapiStruct):
        """
        ``Snmp.SNMPTestResults`` class Structure to provide operators diagnostics
        test results.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     success=None,
                     message=None,
                    ):
            """
            :type  success: :class:`bool`
            :param success: Set success to true/false
            :type  message: :class:`str`
            :param message: message
            """
            self.success = success
            self.message = message
            VapiStruct.__init__(self)

    SNMPTestResults._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_test_results', {
            'success': type.BooleanType(),
            'message': type.StringType(),
        },
        SNMPTestResults,
        False,
        None))


    class SNMPStats(VapiStruct):
        """
        ``Snmp.SNMPStats`` class Structure to provide operators diagnostics on snmp
        agent itself.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     sysuptime=None,
                     worstrtimelast=None,
                     avgresponsetime=None,
                     worstresponsetime=None,
                     inpkts=None,
                     outpkts=None,
                     usmstatsnotintimewindows=None,
                     usmstatsunknownusernames=None,
                     usmstatsunknownengineids=None,
                     usmstatswrongdigests=None,
                     usmstatsdecryptionerrors=None,
                     inbadversions=None,
                     inbadcommunitynames=None,
                     inbadcommunityuses=None,
                     inasnparseerrs=None,
                     intoobigs=None,
                     innosuchnames=None,
                     inbadvalues=None,
                     ingenerrs=None,
                     outtoobigs=None,
                     outnosuchnames=None,
                     outbadvalues=None,
                     outgenerrs=None,
                     outtraps=None,
                     silentdrops=None,
                     avgvarbinds=None,
                     maxvarbinds=None,
                    ):
            """
            :type  sysuptime: :class:`str`
            :param sysuptime: System uptime
            :type  worstrtimelast: :class:`str`
            :param worstrtimelast: Last updated time
            :type  avgresponsetime: :class:`str`
            :param avgresponsetime: Average response time
            :type  worstresponsetime: :class:`str`
            :param worstresponsetime: Response time
            :type  inpkts: :class:`long`
            :param inpkts: No of input packets
            :type  outpkts: :class:`long`
            :param outpkts: No of output packets
            :type  usmstatsnotintimewindows: :class:`long`
            :param usmstatsnotintimewindows: No of stats not in time window
            :type  usmstatsunknownusernames: :class:`long`
            :param usmstatsunknownusernames: No of usm stats unknown
            :type  usmstatsunknownengineids: :class:`long`
            :param usmstatsunknownengineids: No of usm stats unknown engine ids
            :type  usmstatswrongdigests: :class:`long`
            :param usmstatswrongdigests: No of wrogn digests
            :type  usmstatsdecryptionerrors: :class:`long`
            :param usmstatsdecryptionerrors: No. of decryption errors
            :type  inbadversions: :class:`long`
            :param inbadversions: No of bad versions
            :type  inbadcommunitynames: :class:`long`
            :param inbadcommunitynames: No of bad community names
            :type  inbadcommunityuses: :class:`long`
            :param inbadcommunityuses: No of bad community uses
            :type  inasnparseerrs: :class:`long`
            :param inasnparseerrs: No of parse errors
            :type  intoobigs: :class:`long`
            :param intoobigs: No of too bigs
            :type  innosuchnames: :class:`long`
            :param innosuchnames: No of no such names
            :type  inbadvalues: :class:`long`
            :param inbadvalues: No of bad values
            :type  ingenerrs: :class:`long`
            :param ingenerrs: No of gen errors
            :type  outtoobigs: :class:`long`
            :param outtoobigs: No out output too bigs
            :type  outnosuchnames: :class:`long`
            :param outnosuchnames: No of no such names
            :type  outbadvalues: :class:`long`
            :param outbadvalues: No of bad values
            :type  outgenerrs: :class:`long`
            :param outgenerrs: No of gen errors
            :type  outtraps: :class:`long`
            :param outtraps: No of output traps
            :type  silentdrops: :class:`long`
            :param silentdrops: No of silent drops
            :type  avgvarbinds: :class:`long`
            :param avgvarbinds: No of ave:rage var binds
            :type  maxvarbinds: :class:`long`
            :param maxvarbinds: No of max var binds
            """
            self.sysuptime = sysuptime
            self.worstrtimelast = worstrtimelast
            self.avgresponsetime = avgresponsetime
            self.worstresponsetime = worstresponsetime
            self.inpkts = inpkts
            self.outpkts = outpkts
            self.usmstatsnotintimewindows = usmstatsnotintimewindows
            self.usmstatsunknownusernames = usmstatsunknownusernames
            self.usmstatsunknownengineids = usmstatsunknownengineids
            self.usmstatswrongdigests = usmstatswrongdigests
            self.usmstatsdecryptionerrors = usmstatsdecryptionerrors
            self.inbadversions = inbadversions
            self.inbadcommunitynames = inbadcommunitynames
            self.inbadcommunityuses = inbadcommunityuses
            self.inasnparseerrs = inasnparseerrs
            self.intoobigs = intoobigs
            self.innosuchnames = innosuchnames
            self.inbadvalues = inbadvalues
            self.ingenerrs = ingenerrs
            self.outtoobigs = outtoobigs
            self.outnosuchnames = outnosuchnames
            self.outbadvalues = outbadvalues
            self.outgenerrs = outgenerrs
            self.outtraps = outtraps
            self.silentdrops = silentdrops
            self.avgvarbinds = avgvarbinds
            self.maxvarbinds = maxvarbinds
            VapiStruct.__init__(self)

    SNMPStats._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_stats', {
            'sysuptime': type.StringType(),
            'worstrtimelast': type.StringType(),
            'avgresponsetime': type.StringType(),
            'worstresponsetime': type.StringType(),
            'inpkts': type.IntegerType(),
            'outpkts': type.IntegerType(),
            'usmstatsnotintimewindows': type.IntegerType(),
            'usmstatsunknownusernames': type.IntegerType(),
            'usmstatsunknownengineids': type.IntegerType(),
            'usmstatswrongdigests': type.IntegerType(),
            'usmstatsdecryptionerrors': type.IntegerType(),
            'inbadversions': type.IntegerType(),
            'inbadcommunitynames': type.IntegerType(),
            'inbadcommunityuses': type.IntegerType(),
            'inasnparseerrs': type.IntegerType(),
            'intoobigs': type.IntegerType(),
            'innosuchnames': type.IntegerType(),
            'inbadvalues': type.IntegerType(),
            'ingenerrs': type.IntegerType(),
            'outtoobigs': type.IntegerType(),
            'outnosuchnames': type.IntegerType(),
            'outbadvalues': type.IntegerType(),
            'outgenerrs': type.IntegerType(),
            'outtraps': type.IntegerType(),
            'silentdrops': type.IntegerType(),
            'avgvarbinds': type.IntegerType(),
            'maxvarbinds': type.IntegerType(),
        },
        SNMPStats,
        False,
        None))


    class SNMPConfig(VapiStruct):
        """
        ``Snmp.SNMPConfig`` class Structure that defines the SNMP configuration,
        provided as input to set(), and never the result of get(). See
        SNMPConfigReadOnly. This structure is used to configure SNMP v1, v2c, and
        v3.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     authentication=None,
                     communities=None,
                     engineid=None,
                     loglevel=None,
                     notraps=None,
                     port=None,
                     privacy=None,
                     remoteusers=None,
                     syscontact=None,
                     syslocation=None,
                     targets=None,
                     users=None,
                     v3targets=None,
                    ):
            """
            :type  authentication: :class:`Snmp.SNMPAuthProto`
            :param authentication: Set the default authentication protocol. Values can be none, MD5,
                or SHA1.
            :type  communities: :class:`list` of :class:`str`
            :param communities: Set up to ten communities, each of no more than 64 characters long.
                The format is: community1[,community2,...]. This setting overwrites
                any previous settings.
            :type  engineid: :class:`str`
            :param engineid: Set SNMPv3 engine ID. The engine ID must contain 5 to 32
                hexadecimal characters. "0x" and colon (:) are removed from the ID.
            :type  loglevel: :class:`str`
            :param loglevel: System Agent syslog logging level: debug|info|warning|error.
            :type  notraps: :class:`list` of :class:`str`
            :param notraps: Comma-separated list of trap OIDs (object identifiers) for traps
                not to be sent by the agent. Use 'reset' to clear the setting.
            :type  port: :class:`long`
            :param port: Set up a UDP port which the SNMP agent uses to listen on for
                polling requests. The default UDP port is 161.
            :type  privacy: :class:`Snmp.SNMPPrivProto`
            :param privacy: Set the default privacy protocol. Values: none or AES128.
            :type  remoteusers: :class:`list` of :class:`str`
            :param remoteusers: Set up to five inform user IDs. The format is:
                user/auth-proto/-|auth-hash/priv-proto/-|priv-hash/engine-id[,...].
                Here, user must be maximum 32 characters long; auth-proto is none,
                MD5 or SHA1; priv-proto is none or AES; '-' indicates no hash;
                engine-id is a hexadecimal string '0x0-9a-f' and must be up to 32
                characters long.
            :type  syscontact: :class:`str`
            :param syscontact: System contact string as presented in sysContact.0. Up to 255
                characters long.
            :type  syslocation: :class:`str`
            :param syslocation: System location string as presented in sysLocation.0. Up to 255
                characters long.
            :type  targets: :class:`list` of :class:`str`
            :param targets: Set up to three targets to which to send SNMPv1 traps. The format
                is: ip-or-hostname[\\\\@port]/community[,...]. The default port is
                UDP 162. This setting overwrites any previous settings.
            :type  users: :class:`list` of :class:`str`
            :param users: Set up to five local users. The format is:
                user/-|auth-hash/-|priv-hash/model[,...]. Here user is maximum 32
                characters long; '-' indicates no hash; model is one of none, auth
                or priv.
            :type  v3targets: :class:`list` of :class:`str`
            :param v3targets: Set up to three SNMPv3 notification targets. Format is:
                ip-or-hostname[\\\\@port]/remote-user/security-level/trap|inform[,...].
            """
            self.authentication = authentication
            self.communities = communities
            self.engineid = engineid
            self.loglevel = loglevel
            self.notraps = notraps
            self.port = port
            self.privacy = privacy
            self.remoteusers = remoteusers
            self.syscontact = syscontact
            self.syslocation = syslocation
            self.targets = targets
            self.users = users
            self.v3targets = v3targets
            VapiStruct.__init__(self)

    SNMPConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_config', {
            'authentication': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPAuthProto'),
            'communities': type.ListType(type.StringType()),
            'engineid': type.StringType(),
            'loglevel': type.StringType(),
            'notraps': type.ListType(type.StringType()),
            'port': type.IntegerType(),
            'privacy': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPPrivProto'),
            'remoteusers': type.ListType(type.StringType()),
            'syscontact': type.StringType(),
            'syslocation': type.StringType(),
            'targets': type.ListType(type.StringType()),
            'users': type.ListType(type.StringType()),
            'v3targets': type.ListType(type.StringType()),
        },
        SNMPConfig,
        False,
        None))


    class SNMPUser(VapiStruct):
        """
        ``Snmp.SNMPUser`` class Structure that defines information associated with
        an SNMP user. authKey and privKey are localized keys defined in
        http://tools.ietf.org/html/rfc3826#section-1.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     username=None,
                     sec_level=None,
                     auth_key=None,
                     priv_key=None,
                    ):
            """
            :type  username: :class:`str`
            :param username: SNMP Username
            :type  sec_level: :class:`Snmp.SNMPSecLevel`
            :param sec_level: SNMP security level
            :type  auth_key: :class:`str`
            :param auth_key: SNMP authorization key
            :type  priv_key: :class:`str`
            :param priv_key: SNMP privacy key
            """
            self.username = username
            self.sec_level = sec_level
            self.auth_key = auth_key
            self.priv_key = priv_key
            VapiStruct.__init__(self)

    SNMPUser._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_user', {
            'username': type.StringType(),
            'sec_level': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPSecLevel'),
            'auth_key': type.StringType(),
            'priv_key': type.StringType(),
        },
        SNMPUser,
        False,
        None))


    class SNMPv3Target(VapiStruct):
        """
        ``Snmp.SNMPv3Target`` class Structure that defines an SNMP v3 inform or
        trap target.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     type=None,
                     sec_level=None,
                     ip=None,
                     port=None,
                     user=None,
                    ):
            """
            :type  type: :class:`Snmp.SNMPv3Notfication`
            :param type: SNMP target type
            :type  sec_level: :class:`Snmp.SNMPSecLevel`
            :param sec_level: SNMP security level
            :type  ip: :class:`str`
            :param ip: SNMP target ip
            :type  port: :class:`long`
            :param port: SNMP target port
            :type  user: :class:`str`
            :param user: SNMP User
            """
            self.type = type
            self.sec_level = sec_level
            self.ip = ip
            self.port = port
            self.user = user
            VapiStruct.__init__(self)

    SNMPv3Target._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNM_pv3_target', {
            'type': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPv3Notfication'),
            'sec_level': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPSecLevel'),
            'ip': type.StringType(),
            'port': type.IntegerType(),
            'user': type.StringType(),
        },
        SNMPv3Target,
        False,
        None))


    class SNMPv1TrapTarget(VapiStruct):
        """
        ``Snmp.SNMPv1TrapTarget`` class Structure that defines an SNMP v1/v2c trap
        target.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     ip=None,
                     port=None,
                     community=None,
                    ):
            """
            :type  ip: :class:`str`
            :param ip: SNMP target ip
            :type  port: :class:`long`
            :param port: SNMP target port
            :type  community: :class:`str`
            :param community: SNMP target community
            """
            self.ip = ip
            self.port = port
            self.community = community
            VapiStruct.__init__(self)

    SNMPv1TrapTarget._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNM_pv1_trap_target', {
            'ip': type.StringType(),
            'port': type.IntegerType(),
            'community': type.StringType(),
        },
        SNMPv1TrapTarget,
        False,
        None))


    class SNMPRemoteUser(VapiStruct):
        """
        ``Snmp.SNMPRemoteUser`` class Structure that defines a user at particular
        remote SNMPv3 entity needed when using informs. auth_key and priv_key
        contained localized keys as defined in
        http://tools.ietf.org/html/rfc3826#section-1.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     username=None,
                     sec_level=None,
                     authentication=None,
                     auth_key=None,
                     privacy=None,
                     priv_key=None,
                     engineid=None,
                    ):
            """
            :type  username: :class:`str`
            :param username: SNMP Username
            :type  sec_level: :class:`Snmp.SNMPSecLevel`
            :param sec_level: SNMP security level
            :type  authentication: :class:`Snmp.SNMPAuthProto`
            :param authentication: SNMP authorization protocol
            :type  auth_key: :class:`str`
            :param auth_key: SNMP authorization key
            :type  privacy: :class:`Snmp.SNMPPrivProto`
            :param privacy: SNMP privacy protocol
            :type  priv_key: :class:`str`
            :param priv_key: SNMP privacy key
            :type  engineid: :class:`str`
            :param engineid: SNMP v3 engine id
            """
            self.username = username
            self.sec_level = sec_level
            self.authentication = authentication
            self.auth_key = auth_key
            self.privacy = privacy
            self.priv_key = priv_key
            self.engineid = engineid
            VapiStruct.__init__(self)

    SNMPRemoteUser._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_remote_user', {
            'username': type.StringType(),
            'sec_level': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPSecLevel'),
            'authentication': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPAuthProto'),
            'auth_key': type.StringType(),
            'privacy': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPPrivProto'),
            'priv_key': type.StringType(),
            'engineid': type.StringType(),
        },
        SNMPRemoteUser,
        False,
        None))


    class SNMPConfigReadOnly(VapiStruct):
        """
        ``Snmp.SNMPConfigReadOnly`` class Structure that defines the SNMP
        configuration, the result of get(), and never provided as input to set().
        This structure differs from SNMPConfig because it contains localized keys
        (as defined in http://tools.ietf.org/html/rfc3826#section-1.2), instead of
        raw secret strings. This structure can be used to configure SNMP v1, v2c,
        and v3. Keep this structure in sync with vmw_snmp.py:_default_config().
        Note that if a field if left empty, it is considered unset and will be
        ignored. Existing array elements below can be unset by sending an element
        with the string 'reset'.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     authentication=None,
                     communities=None,
                     enable=None,
                     engineid=None,
                     loglevel=None,
                     notraps=None,
                     port=None,
                     privacy=None,
                     syscontact=None,
                     syslocation=None,
                     targets=None,
                     users=None,
                     remoteusers=None,
                     v3targets=None,
                     pid=None,
                    ):
            """
            :type  authentication: :class:`Snmp.SNMPAuthProto`
            :param authentication: Set the default authentication protocol. Values can be none, MD5,
                or SHA1.
            :type  communities: :class:`list` of :class:`str`
            :param communities: Set up to ten communities, each of no more than 64 characters long.
                The format is: community1[,community2,...]. This setting overwrites
                any previous settings.
            :type  enable: :class:`bool`
            :param enable: Set enable to true/false
            :type  engineid: :class:`str`
            :param engineid: Set SNMPv3 engine ID.
            :type  loglevel: :class:`str`
            :param loglevel: System Agent syslog logging level: debug|info|warning|error.
            :type  notraps: :class:`list` of :class:`str`
            :param notraps: Comma-separated list of trap OIDs (object identifiers) for traps
                not to be sent by the agent. Use 'reset' to clear the setting.
            :type  port: :class:`long`
            :param port: Set up a UDP port which the SNMP agent uses to listen on for
                polling requests. The default UDP port is 161.
            :type  privacy: :class:`Snmp.SNMPPrivProto`
            :param privacy: Set the default privacy protocol.
            :type  syscontact: :class:`str`
            :param syscontact: System contact string as presented in sysContact.0. Up to 255
                characters long.
            :type  syslocation: :class:`str`
            :param syslocation: System location string as presented in sysLocation.0. Up to 255
                characters long.
            :type  targets: :class:`list` of :class:`Snmp.SNMPv1TrapTarget`
            :param targets: Set up to three targets to which to send SNMPv1 traps.
            :type  users: :class:`list` of :class:`Snmp.SNMPUser`
            :param users: Set up to five local users.
            :type  remoteusers: :class:`list` of :class:`Snmp.SNMPRemoteUser`
            :param remoteusers: Set up remote users.
            :type  v3targets: :class:`list` of :class:`Snmp.SNMPv3Target`
            :param v3targets: Set up to three SNMPv3 notification targets. Format is:
                ip-or-hostname[\\\\@port]/remote-user/security-level/trap|inform[,...].
            :type  pid: :class:`str`
            :param pid: Set up pid
            """
            self.authentication = authentication
            self.communities = communities
            self.enable = enable
            self.engineid = engineid
            self.loglevel = loglevel
            self.notraps = notraps
            self.port = port
            self.privacy = privacy
            self.syscontact = syscontact
            self.syslocation = syslocation
            self.targets = targets
            self.users = users
            self.remoteusers = remoteusers
            self.v3targets = v3targets
            self.pid = pid
            VapiStruct.__init__(self)

    SNMPConfigReadOnly._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_config_read_only', {
            'authentication': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPAuthProto'),
            'communities': type.ListType(type.StringType()),
            'enable': type.BooleanType(),
            'engineid': type.StringType(),
            'loglevel': type.StringType(),
            'notraps': type.ListType(type.StringType()),
            'port': type.IntegerType(),
            'privacy': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPPrivProto'),
            'syscontact': type.StringType(),
            'syslocation': type.StringType(),
            'targets': type.ListType(type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPv1TrapTarget')),
            'users': type.ListType(type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPUser')),
            'remoteusers': type.ListType(type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPRemoteUser')),
            'v3targets': type.ListType(type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPv3Target')),
            'pid': type.StringType(),
        },
        SNMPConfigReadOnly,
        False,
        None))


    class SNMPHashConfig(VapiStruct):
        """
        ``Snmp.SNMPHashConfig`` class Structure to provide up to two secrets to
        combine with the SNMPv3 engine ID and authentication or privacy protocol to
        form a localized hash. auth_hash is always required, priv_hash can be
        empty. By default arguments are paths on the local filesystem, raw_secret
        takes path to be the actual raw secret. First implementation was in ESXi:
        esxcli system snmp hash --help

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     auth_hash=None,
                     priv_hash=None,
                     raw_secret=None,
                    ):
            """
            :type  auth_hash: :class:`str`
            :param auth_hash: Provide filename to secret for authentication hash, use in set
                --users (required secret)
            :type  priv_hash: :class:`str`
            :param priv_hash: Provide filename to secret for privacy hash, use in set --users
                (secret)
            :type  raw_secret: :class:`bool`
            :param raw_secret: Make --auth_path and --priv_path flags read raw secret from command
                line instead of file.
            """
            self.auth_hash = auth_hash
            self.priv_hash = priv_hash
            self.raw_secret = raw_secret
            VapiStruct.__init__(self)

    SNMPHashConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_hash_config', {
            'auth_hash': type.StringType(),
            'priv_hash': type.StringType(),
            'raw_secret': type.BooleanType(),
        },
        SNMPHashConfig,
        False,
        None))


    class SNMPHashResults(VapiStruct):
        """
        ``Snmp.SNMPHashResults`` class Structure to provide operators diagnostics
        test results.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     auth_key=None,
                     priv_key=None,
                    ):
            """
            :type  auth_key: :class:`str`
            :param auth_key: SNMP authentication key
            :type  priv_key: :class:`str`
            :param priv_key: SNMP privacy key
            """
            self.auth_key = auth_key
            self.priv_key = priv_key
            VapiStruct.__init__(self)

    SNMPHashResults._set_binding_type(type.StructType(
        'com.vmware.appliance.techpreview.monitoring.snmp.SNMP_hash_results', {
            'auth_key': type.StringType(),
            'priv_key': type.StringType(),
        },
        SNMPHashResults,
        False,
        None))



    def reset(self):
        """
        Restore settings to factory defaults.


        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('reset', None)

    def enable(self):
        """
        Start a disabled SNMP agent.


        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('enable', None)

    def hash(self,
             config,
             ):
        """
        Generate localized keys for secure SNMPv3 communications.

        :type  config: :class:`Snmp.SNMPHashConfig`
        :param config: SNMP hash configuration.
        :rtype: :class:`Snmp.SNMPHashResults`
        :return: SNMP hash result
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('hash',
                            {
                            'config': config,
                            })

    def limits(self):
        """
        Get SNMP limits information.


        :rtype: :class:`Snmp.SNMPLimits`
        :return: SNMP limits structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('limits', None)

    def get(self):
        """
        Return an SNMP agent configuration.


        :rtype: :class:`Snmp.SNMPConfigReadOnly`
        :return: SNMP config structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

    def disable(self):
        """
        Stop an enabled SNMP agent.


        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('disable', None)

    def set(self,
            config,
            ):
        """
        Set SNMP configuration.

        :type  config: :class:`Snmp.SNMPConfig`
        :param config: SNMP configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def test(self):
        """
        Send a warmStart notification to all configured traps and inform
        destinations (see RFC 3418).


        :rtype: :class:`Snmp.SNMPTestResults`
        :return: SNMP test result
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('test', None)

    def stats(self):
        """
        Generate diagnostics report for snmp agent.


        :rtype: :class:`Snmp.SNMPStats`
        :return: SNMP stats
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('stats', None)

class _SnmpStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for reset operation
        reset_input_type = type.StructType('operation-input', {})
        reset_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        reset_input_validator_list = [
        ]
        reset_output_validator_list = [
        ]

        # properties for enable operation
        enable_input_type = type.StructType('operation-input', {})
        enable_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        enable_input_validator_list = [
        ]
        enable_output_validator_list = [
        ]

        # properties for hash operation
        hash_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPHashConfig'),
        })
        hash_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        hash_input_validator_list = [
        ]
        hash_output_validator_list = [
        ]

        # properties for limits operation
        limits_input_type = type.StructType('operation-input', {})
        limits_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        limits_input_validator_list = [
        ]
        limits_output_validator_list = [
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

        # properties for disable operation
        disable_input_type = type.StructType('operation-input', {})
        disable_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        disable_input_validator_list = [
        ]
        disable_output_validator_list = [
        ]

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPConfig'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        set_input_validator_list = [
        ]
        set_output_validator_list = [
        ]

        # properties for test operation
        test_input_type = type.StructType('operation-input', {})
        test_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        test_input_validator_list = [
        ]
        test_output_validator_list = [
        ]

        # properties for stats operation
        stats_input_type = type.StructType('operation-input', {})
        stats_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        stats_input_validator_list = [
        ]
        stats_output_validator_list = [
        ]

        operations = {
            'reset': {
                'input_type': reset_input_type,
                'output_type': type.VoidType(),
                'errors': reset_error_dict,
                'input_validator_list': reset_input_validator_list,
                'output_validator_list': reset_output_validator_list,
            },
            'enable': {
                'input_type': enable_input_type,
                'output_type': type.VoidType(),
                'errors': enable_error_dict,
                'input_validator_list': enable_input_validator_list,
                'output_validator_list': enable_output_validator_list,
            },
            'hash': {
                'input_type': hash_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPHashResults'),
                'errors': hash_error_dict,
                'input_validator_list': hash_input_validator_list,
                'output_validator_list': hash_output_validator_list,
            },
            'limits': {
                'input_type': limits_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPLimits'),
                'errors': limits_error_dict,
                'input_validator_list': limits_input_validator_list,
                'output_validator_list': limits_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPConfigReadOnly'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
            'disable': {
                'input_type': disable_input_type,
                'output_type': type.VoidType(),
                'errors': disable_error_dict,
                'input_validator_list': disable_input_validator_list,
                'output_validator_list': disable_output_validator_list,
            },
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_validator_list': set_input_validator_list,
                'output_validator_list': set_output_validator_list,
            },
            'test': {
                'input_type': test_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPTestResults'),
                'errors': test_error_dict,
                'input_validator_list': test_input_validator_list,
                'output_validator_list': test_output_validator_list,
            },
            'stats': {
                'input_type': stats_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Snmp.SNMPStats'),
                'errors': stats_error_dict,
                'input_validator_list': stats_input_validator_list,
                'output_validator_list': stats_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.techpreview.monitoring.snmp',
                                  config=config,
                                  operations=operations)

