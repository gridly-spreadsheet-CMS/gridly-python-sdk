# coding: utf-8

"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 5.9.0
    Contact: support@gridly.com
    Generated by: https://openapi-generator.tech
"""

from gridly.paths.v1_transmems_tm_id_cleanup.put import Cleanup
from gridly.paths.v1_transmems.post import Create
from gridly.paths.v1_transmems_upload.post import CreateWithFile
from gridly.paths.v1_transmems_tm_id.delete import Delete
from gridly.paths.v1_transmems_tm_id_export.get import Export
from gridly.paths.v1_transmems_tm_id.get import Get
from gridly.paths.v1_transmems_tm_id_import.post import ImportTmx
from gridly.paths.v1_transmems.get import ListTm
from gridly.paths.v1_transmems_tm_id.put import Update


class TransmemApi(
    Cleanup,
    Create,
    CreateWithFile,
    Delete,
    Export,
    Get,
    ImportTmx,
    ListTm,
    Update,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
