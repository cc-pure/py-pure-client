# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_2 import models

class SoftwareInstallations(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'current_step_id': 'str',
        'details': 'str',
        'mode': 'str',
        'override_checks': 'list[OverrideCheck]',
        'software': 'Reference',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'current_step_id': 'current_step_id',
        'details': 'details',
        'mode': 'mode',
        'override_checks': 'override_checks',
        'software': 'software',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        start_time=None,  # type: int
        end_time=None,  # type: int
        current_step_id=None,  # type: str
        details=None,  # type: str
        mode=None,  # type: str
        override_checks=None,  # type: List[models.OverrideCheck]
        software=None,  # type: models.Reference
        status=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified.
            name (str): Name of the resource. The name cannot be modified.
            start_time (int): Start time in milliseconds since the UNIX epoch.
            end_time (int): End time in milliseconds since the UNIX epoch.
            current_step_id (str): The `id` of the current step, or `null` if the upgrade is not active.
            details (str): The detailed reason of the `status`.
            mode (str): Which mode the upgrade is in. Valid values are `interactive`, `one_click`, and `check_only`. In `interactive` mode, the upgrade process pauses at several points, at which users must enter certain commands to proceed. In `one_click` mode, the upgrade proceeds automatically without pausing. In `check_only` mode, the upgrade only runs pre-upgrade checks and returns.
            override_checks (list[OverrideCheck]): A list of upgrade checks whose failure will be overridden during the upgrade. If any optional `args` are provided, they are validated later when the corresponding check script runs.
            software (Reference): Referenced `software` to which the upgrade belongs.
            status (str): Status of the upgrade. Valid values are `installing`, `paused`, `aborting`, `aborted`, and `finished`. A status of `installing` indicates that the upgrade is running. A status of `paused` indicates that the upgrade is paused and waiting for user input. A status of `aborting` indicates that the upgrade is being aborted. A status of `aborted` indicates that the upgrade has stopped due to an abort. A status of `finished` indicates that the upgrade has finished successfully.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if current_step_id is not None:
            self.current_step_id = current_step_id
        if details is not None:
            self.details = details
        if mode is not None:
            self.mode = mode
        if override_checks is not None:
            self.override_checks = override_checks
        if software is not None:
            self.software = software
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallations`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(SoftwareInstallations, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SoftwareInstallations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
