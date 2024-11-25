# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from gridly.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_VIEWS_VIEW_ID_SHARES = "/v1/views/{viewId}/shares"
    V1_VIEWS_VIEW_ID_PATHS_PATH = "/v1/views/{viewId}/paths/{path}"
    V1_VIEWS_VIEW_ID_DEPENDENCIES_DEPENDENCY_ID = "/v1/views/{viewId}/dependencies/{dependencyId}"
    V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID = "/v1/grids/{gridId}/settings/categories/{categoryId}"
    V1_CDNS_CDN_ID_UNPUBLISH = "/v1/cdns/{cdnId}/unpublish"
    V1_CDNS_CDN_ID_PUBLISH = "/v1/cdns/{cdnId}/publish"
    V1_VIEWS = "/v1/views"
    V1_VIEWS_VIEW_ID_RECORDS = "/v1/views/{viewId}/records"
    V1_VIEWS_VIEW_ID_PATHS = "/v1/views/{viewId}/paths"
    V1_VIEWS_VIEW_ID_PATHS_MOVE = "/v1/views/{viewId}/paths/move"
    V1_VIEWS_VIEW_ID_MERGE = "/v1/views/{viewId}/merge"
    V1_VIEWS_VIEW_ID_IMPORT = "/v1/views/{viewId}/import"
    V1_VIEWS_VIEW_ID_FILES = "/v1/views/{viewId}/files"
    V1_VIEWS_VIEW_ID_FILES_ZIP = "/v1/views/{viewId}/files/zip"
    V1_VIEWS_VIEW_ID_DEPENDENCIES = "/v1/views/{viewId}/dependencies"
    V1_VIEWS_VIEW_ID_COLUMNS = "/v1/views/{viewId}/columns"
    V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID_REMOVE = "/v1/views/{viewId}/columns/{columnId}/remove"
    V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID_ADD = "/v1/views/{viewId}/columns/{columnId}/add"
    V1_VIEWS_VIEW_ID_COLUMNS_BULK = "/v1/views/{viewId}/columns/bulk"
    V1_GRIDS = "/v1/grids"
    V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES = "/v1/grids/{gridId}/settings/categories"
    V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID_FILES = "/v1/grids/{gridId}/settings/categories/{categoryId}/files"
    V1_BRANCHES = "/v1/branches"
    V1_BRANCHES_BRANCH_ID_MERGE = "/v1/branches/{branchId}/merge"
    V1_BRANCHES_DIFFCHECK = "/v1/branches/diffcheck"
    V1_VIEWS_VIEW_ID_RECORDS_ID = "/v1/views/{viewId}/records/{id}"
    V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID = "/v1/views/{viewId}/columns/{columnId}"
    V1_GRIDS_GRID_ID = "/v1/grids/{gridId}"
    V1_GRIDS_GRID_ID_SETTINGS = "/v1/grids/{gridId}/settings"
    V1_VIEWS_VIEW_ID = "/v1/views/{viewId}"
    V1_VIEWS_VIEW_ID_STATISTIC = "/v1/views/{viewId}/statistic"
    V1_VIEWS_VIEW_ID_RECORDS_RECORD_ID_HISTORIES = "/v1/views/{viewId}/records/{recordId}/histories"
    V1_VIEWS_VIEW_ID_PATHS_TREE = "/v1/views/{viewId}/paths/tree"
    V1_VIEWS_VIEW_ID_FILES_FILE_ID = "/v1/views/{viewId}/files/{fileId}"
    V1_VIEWS_VIEW_ID_EXPORT = "/v1/views/{viewId}/export"
    V1_TEMPLATEGRIDS = "/v1/template-grids"
    V1_TASKS_TASK_ID = "/v1/tasks/{taskId}"
    V1_GRIDS_GRID_ID_SETTINGS_FILES = "/v1/grids/{gridId}/settings/files"
    V1_CDNS = "/v1/cdns"
    V1_BRANCHES_BRANCH_ID = "/v1/branches/{branchId}"
    V1_BRANCHES_DIFFCHECK_TASK_ID = "/v1/branches/diffcheck/{taskId}"
    V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID_FILES_FILE_ID = "/v1/grids/{gridId}/settings/categories/{categoryId}/files/{fileId}"
    V1_PROJECTS_PROJECT_ID = "/v1/projects/{projectId}"
    V1_DATABASES_DB_ID = "/v1/databases/{dbId}"
    V1_PROJECTS = "/v1/projects"
    V1_DATABASES = "/v1/databases"
    V1_DATABASES_DB_ID_DUPLICATE = "/v1/databases/{dbId}/duplicate"
    V1_GLOSSARIES = "/v1/glossaries"
    V1_GLOSSARIES_ID = "/v1/glossaries/{id}"
    V1_GLOSSARIES_ID_EXPORT = "/v1/glossaries/{id}/export"
    V1_GLOSSARIES_ID_IMPORT = "/v1/glossaries/{id}/import"
    V1_TRANSMEMS = "/v1/transmems"
    V1_TRANSMEMS_UPLOAD = "/v1/transmems/upload"
    V1_TRANSMEMS_TM_ID = "/v1/transmems/{tmId}"
    V1_TRANSMEMS_TM_ID_CLEANUP = "/v1/transmems/{tmId}/cleanup"
    V1_TRANSMEMS_TM_ID_EXPORT = "/v1/transmems/{tmId}/export"
    V1_TRANSMEMS_TM_ID_IMPORT = "/v1/transmems/{tmId}/import"
