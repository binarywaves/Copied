# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2016 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.
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


class Monitoring(VapiInterface):
    """
    ``Monitoring`` class provides methods Get and list monitoring data for
    requested item.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MonitoringStub)

    class FunctionType(Enum):
        """
        ``Monitoring.FunctionType`` class Defines aggregation function

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        COUNT = None
        """
        Aggregation takes count per period (sum)

        """
        MAX = None
        """
        Aggregation takes maximums per period

        """
        AVG = None
        """
        Aggregation takes average per period

        """
        MIN = None
        """
        Aggregation takes minimums per period

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`FunctionType` instance.
            """
            Enum.__init__(string)

    FunctionType._set_values([
        FunctionType('COUNT'),
        FunctionType('MAX'),
        FunctionType('AVG'),
        FunctionType('MIN'),
    ])
    FunctionType._set_binding_type(type.EnumType(
        'com.vmware.appliance.monitoring.function_type',
        FunctionType))


    class IntervalType(Enum):
        """
        ``Monitoring.IntervalType`` class Defines interval between the values in
        hours and mins, for which aggregation will apply

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        MINUTES30 = None
        """
        Thirty minutes interval between values. One week is 336 values.

        """
        HOURS2 = None
        """
        Two hours interval between values. One month has 360 values.

        """
        MINUTES5 = None
        """
        Five minutes interval between values (finest). One day would have 288
        values, one week is 2016.

        """
        DAY1 = None
        """
        24 hours interval between values. One year has 365 values.

        """
        HOURS6 = None
        """
        Six hour interval between values. One quarter is 360 values.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IntervalType` instance.
            """
            Enum.__init__(string)

    IntervalType._set_values([
        IntervalType('MINUTES30'),
        IntervalType('HOURS2'),
        IntervalType('MINUTES5'),
        IntervalType('DAY1'),
        IntervalType('HOURS6'),
    ])
    IntervalType._set_binding_type(type.EnumType(
        'com.vmware.appliance.monitoring.interval_type',
        IntervalType))


    class MonitoredItemData(VapiStruct):
        """
        ``Monitoring.MonitoredItemData`` class Structure representing monitored
        item data.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     name=None,
                     interval=None,
                     function=None,
                     start_time=None,
                     end_time=None,
                     data=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Monitored item IDs Ex: CPU, MEMORY, STORAGE_TOTAL
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.monitoring``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.appliance.monitoring``.
            :type  interval: :class:`Monitoring.IntervalType`
            :param interval: interval between values in hours, minutes
            :type  function: :class:`Monitoring.FunctionType`
            :param function: aggregation function
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Starting time
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Ending time
            :type  data: :class:`list` of :class:`str`
            :param data: list of values
            """
            self.name = name
            self.interval = interval
            self.function = function
            self.start_time = start_time
            self.end_time = end_time
            self.data = data
            VapiStruct.__init__(self)

    MonitoredItemData._set_binding_type(type.StructType(
        'com.vmware.appliance.monitoring.monitored_item_data', {
            'name': type.IdType(resource_types='com.vmware.appliance.monitoring'),
            'interval': type.ReferenceType(sys.modules[__name__], 'Monitoring.IntervalType'),
            'function': type.ReferenceType(sys.modules[__name__], 'Monitoring.FunctionType'),
            'start_time': type.DateTimeType(),
            'end_time': type.DateTimeType(),
            'data': type.ListType(type.StringType()),
        },
        MonitoredItemData,
        False,
        None))


    class MonitoredItemDataRequest(VapiStruct):
        """
        ``Monitoring.MonitoredItemDataRequest`` class Structure representing
        requested monitored item data.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     names=None,
                     interval=None,
                     function=None,
                     start_time=None,
                     end_time=None,
                    ):
            """
            :type  names: :class:`list` of :class:`str`
            :param names: monitored item IDs Ex: CPU, MEMORY
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.appliance.monitoring``. When methods return a value of
                this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.appliance.monitoring``.
            :type  interval: :class:`Monitoring.IntervalType`
            :param interval: interval between values in hours, minutes
            :type  function: :class:`Monitoring.FunctionType`
            :param function: aggregation function
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Starting time
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Ending time
            """
            self.names = names
            self.interval = interval
            self.function = function
            self.start_time = start_time
            self.end_time = end_time
            VapiStruct.__init__(self)

    MonitoredItemDataRequest._set_binding_type(type.StructType(
        'com.vmware.appliance.monitoring.monitored_item_data_request', {
            'names': type.ListType(type.IdType()),
            'interval': type.ReferenceType(sys.modules[__name__], 'Monitoring.IntervalType'),
            'function': type.ReferenceType(sys.modules[__name__], 'Monitoring.FunctionType'),
            'start_time': type.DateTimeType(),
            'end_time': type.DateTimeType(),
        },
        MonitoredItemDataRequest,
        False,
        None))


    class MonitoredItem(VapiStruct):
        """
        ``Monitoring.MonitoredItem`` class Structure representing requested
        monitored item data.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        def __init__(self,
                     id=None,
                     name=None,
                     units=None,
                     category=None,
                     instance=None,
                     description=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: monitored item ID Ex: CPU, MEMORY
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.monitoring``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.appliance.monitoring``.
            :type  name: :class:`str`
            :param name: monitored item name Ex: "Network write speed"
            :type  units: :class:`str`
            :param units: Y-axis label EX: "Mbps", "%"
            :type  category: :class:`str`
            :param category: category Ex: network, storage etc
            :type  instance: :class:`str`
            :param instance: instance name Ex: eth0
            :type  description: :class:`str`
            :param description: monitored item description Ex:
                com.vmware.applmgmt.mon.descr.net.rx.packetRate.eth0
            """
            self.id = id
            self.name = name
            self.units = units
            self.category = category
            self.instance = instance
            self.description = description
            VapiStruct.__init__(self)

    MonitoredItem._set_binding_type(type.StructType(
        'com.vmware.appliance.monitoring.monitored_item', {
            'id': type.IdType(resource_types='com.vmware.appliance.monitoring'),
            'name': type.StringType(),
            'units': type.StringType(),
            'category': type.StringType(),
            'instance': type.StringType(),
            'description': type.StringType(),
        },
        MonitoredItem,
        False,
        None))



    def query(self,
              item,
              ):
        """
        Get monitoring data.

        :type  item: :class:`Monitoring.MonitoredItemDataRequest`
        :param item: MonitoredItemDataRequest Structure
        :rtype: :class:`list` of :class:`Monitoring.MonitoredItemData`
        :return: list of MonitoredItemData structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('query',
                            {
                            'item': item,
                            })

    def list(self):
        """
        Get monitored items list


        :rtype: :class:`list` of :class:`Monitoring.MonitoredItem`
        :return: list of names
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            stat_id,
            ):
        """
        Get monitored item info

        :type  stat_id: :class:`str`
        :param stat_id: statistic item id
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.monitoring``.
        :rtype: :class:`Monitoring.MonitoredItem`
        :return: MonitoredItem structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'stat_id': stat_id,
                            })

class _MonitoringStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for query operation
        query_input_type = type.StructType('operation-input', {
            'item': type.ReferenceType(sys.modules[__name__], 'Monitoring.MonitoredItemDataRequest'),
        })
        query_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType(com.vmware.vapi.std.errors_client, 'Error'),

        }
        query_input_validator_list = [
        ]
        query_output_validator_list = [
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
            'stat_id': type.IdType(resource_types='com.vmware.appliance.monitoring'),
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
            'query': {
                'input_type': query_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Monitoring.MonitoredItemData')),
                'errors': query_error_dict,
                'input_validator_list': query_input_validator_list,
                'output_validator_list': query_output_validator_list,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(sys.modules[__name__], 'Monitoring.MonitoredItem')),
                'errors': list_error_dict,
                'input_validator_list': list_input_validator_list,
                'output_validator_list': list_output_validator_list,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(sys.modules[__name__], 'Monitoring.MonitoredItem'),
                'errors': get_error_dict,
                'input_validator_list': get_input_validator_list,
                'output_validator_list': get_output_validator_list,
            },
        }
        ApiInterfaceStub.__init__(self, iface_name='com.vmware.appliance.monitoring',
                                  config=config,
                                  operations=operations)

