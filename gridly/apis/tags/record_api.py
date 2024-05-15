# coding: utf-8

"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 4.33.0
    Contact: support@gridly.com
    Generated by: https://openapi-generator.tech
"""

from gridly.paths.v1_views_view_id_records.post import Create
from gridly.paths.v1_views_view_id_records.delete import Delete
from gridly.paths.v1_views_view_id_records.get import Fetch
from gridly.paths.v1_views_view_id_records_record_id_histories.get import FetchHistories
from gridly.paths.v1_views_view_id_records.patch import Update
from gridly.paths.v1_views_view_id_records_id.patch import UpdateRecord


class RecordApi(
    Create,
    Delete,
    Fetch,
    FetchHistories,
    Update,
    UpdateRecord,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
