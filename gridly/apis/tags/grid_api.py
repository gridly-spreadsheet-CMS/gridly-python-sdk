# coding: utf-8

"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 5.9.0
    Contact: support@gridly.com
    Generated by: https://openapi-generator.tech
"""

from gridly.paths.v1_grids.get import CallList
from gridly.paths.v1_grids.post import Create
from gridly.paths.v1_grids_grid_id_settings_categories.post import CreateCategory
from gridly.paths.v1_grids_grid_id.delete import Delete
from gridly.paths.v1_grids_grid_id_settings_categories_category_id.delete import DeleteCategory
from gridly.paths.v1_grids_grid_id_settings_categories_category_id_files_file_id.delete import DeleteFile
from gridly.paths.v1_grids_grid_id.get import Get
from gridly.paths.v1_grids_grid_id_settings.get import GetSetting
from gridly.paths.v1_grids_grid_id_settings_files.get import ListFiles
from gridly.paths.v1_template_grids.get import ListTemplateGrids
from gridly.paths.v1_grids_grid_id.patch import Update
from gridly.paths.v1_grids_grid_id_settings_categories_category_id.put import UpdateCategory
from gridly.paths.v1_grids_grid_id_settings.patch import UpdateSetting
from gridly.paths.v1_grids_grid_id_settings_categories_category_id_files.post import UploadSettingFile


class GridApi(
    CallList,
    Create,
    CreateCategory,
    Delete,
    DeleteCategory,
    DeleteFile,
    Get,
    GetSetting,
    ListFiles,
    ListTemplateGrids,
    Update,
    UpdateCategory,
    UpdateSetting,
    UploadSettingFile,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
