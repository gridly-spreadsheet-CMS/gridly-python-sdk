import typing_extensions

from gridly.paths import PathValues
from gridly.apis.paths.v1_views_view_id_shares import V1ViewsViewIdShares
from gridly.apis.paths.v1_views_view_id_paths_path import V1ViewsViewIdPathsPath
from gridly.apis.paths.v1_views_view_id_dependencies_dependency_id import V1ViewsViewIdDependenciesDependencyId
from gridly.apis.paths.v1_grids_grid_id_settings_categories_category_id import V1GridsGridIdSettingsCategoriesCategoryId
from gridly.apis.paths.v1_views import V1Views
from gridly.apis.paths.v1_views_view_id_records import V1ViewsViewIdRecords
from gridly.apis.paths.v1_views_view_id_paths import V1ViewsViewIdPaths
from gridly.apis.paths.v1_views_view_id_paths_move import V1ViewsViewIdPathsMove
from gridly.apis.paths.v1_views_view_id_merge import V1ViewsViewIdMerge
from gridly.apis.paths.v1_views_view_id_import import V1ViewsViewIdImport
from gridly.apis.paths.v1_views_view_id_files import V1ViewsViewIdFiles
from gridly.apis.paths.v1_views_view_id_files_zip import V1ViewsViewIdFilesZip
from gridly.apis.paths.v1_views_view_id_dependencies import V1ViewsViewIdDependencies
from gridly.apis.paths.v1_views_view_id_columns import V1ViewsViewIdColumns
from gridly.apis.paths.v1_views_view_id_columns_column_id_remove import V1ViewsViewIdColumnsColumnIdRemove
from gridly.apis.paths.v1_views_view_id_columns_column_id_add import V1ViewsViewIdColumnsColumnIdAdd
from gridly.apis.paths.v1_views_view_id_columns_bulk import V1ViewsViewIdColumnsBulk
from gridly.apis.paths.v1_grids import V1Grids
from gridly.apis.paths.v1_grids_grid_id_settings_categories import V1GridsGridIdSettingsCategories
from gridly.apis.paths.v1_grids_grid_id_settings_categories_category_id_files import V1GridsGridIdSettingsCategoriesCategoryIdFiles
from gridly.apis.paths.v1_branches import V1Branches
from gridly.apis.paths.v1_branches_branch_id_merge import V1BranchesBranchIdMerge
from gridly.apis.paths.v1_branches_diffcheck import V1BranchesDiffcheck
from gridly.apis.paths.v1_views_view_id_records_id import V1ViewsViewIdRecordsId
from gridly.apis.paths.v1_views_view_id_columns_column_id import V1ViewsViewIdColumnsColumnId
from gridly.apis.paths.v1_grids_grid_id import V1GridsGridId
from gridly.apis.paths.v1_grids_grid_id_settings import V1GridsGridIdSettings
from gridly.apis.paths.v1_views_view_id import V1ViewsViewId
from gridly.apis.paths.v1_views_view_id_statistic import V1ViewsViewIdStatistic
from gridly.apis.paths.v1_views_view_id_records_record_id_histories import V1ViewsViewIdRecordsRecordIdHistories
from gridly.apis.paths.v1_views_view_id_paths_tree import V1ViewsViewIdPathsTree
from gridly.apis.paths.v1_views_view_id_files_file_id import V1ViewsViewIdFilesFileId
from gridly.apis.paths.v1_views_view_id_export import V1ViewsViewIdExport
from gridly.apis.paths.v1_template_grids import V1TemplateGrids
from gridly.apis.paths.v1_tasks_task_id import V1TasksTaskId
from gridly.apis.paths.v1_grids_grid_id_settings_files import V1GridsGridIdSettingsFiles
from gridly.apis.paths.v1_branches_branch_id import V1BranchesBranchId
from gridly.apis.paths.v1_branches_diffcheck_task_id import V1BranchesDiffcheckTaskId
from gridly.apis.paths.v1_grids_grid_id_settings_categories_category_id_files_file_id import V1GridsGridIdSettingsCategoriesCategoryIdFilesFileId
from gridly.apis.paths.v1_projects_project_id import V1ProjectsProjectId
from gridly.apis.paths.v1_databases_db_id import V1DatabasesDbId
from gridly.apis.paths.v1_projects import V1Projects
from gridly.apis.paths.v1_databases import V1Databases
from gridly.apis.paths.v1_databases_db_id_duplicate import V1DatabasesDbIdDuplicate
from gridly.apis.paths.v1_glossaries import V1Glossaries
from gridly.apis.paths.v1_glossaries_id import V1GlossariesId
from gridly.apis.paths.v1_glossaries_id_export import V1GlossariesIdExport
from gridly.apis.paths.v1_glossaries_id_import import V1GlossariesIdImport
from gridly.apis.paths.v1_transmems import V1Transmems
from gridly.apis.paths.v1_transmems_upload import V1TransmemsUpload
from gridly.apis.paths.v1_transmems_tm_id import V1TransmemsTmId
from gridly.apis.paths.v1_transmems_tm_id_cleanup import V1TransmemsTmIdCleanup
from gridly.apis.paths.v1_transmems_tm_id_export import V1TransmemsTmIdExport
from gridly.apis.paths.v1_transmems_tm_id_import import V1TransmemsTmIdImport

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_VIEWS_VIEW_ID_SHARES: V1ViewsViewIdShares,
        PathValues.V1_VIEWS_VIEW_ID_PATHS_PATH: V1ViewsViewIdPathsPath,
        PathValues.V1_VIEWS_VIEW_ID_DEPENDENCIES_DEPENDENCY_ID: V1ViewsViewIdDependenciesDependencyId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID: V1GridsGridIdSettingsCategoriesCategoryId,
        PathValues.V1_VIEWS: V1Views,
        PathValues.V1_VIEWS_VIEW_ID_RECORDS: V1ViewsViewIdRecords,
        PathValues.V1_VIEWS_VIEW_ID_PATHS: V1ViewsViewIdPaths,
        PathValues.V1_VIEWS_VIEW_ID_PATHS_MOVE: V1ViewsViewIdPathsMove,
        PathValues.V1_VIEWS_VIEW_ID_MERGE: V1ViewsViewIdMerge,
        PathValues.V1_VIEWS_VIEW_ID_IMPORT: V1ViewsViewIdImport,
        PathValues.V1_VIEWS_VIEW_ID_FILES: V1ViewsViewIdFiles,
        PathValues.V1_VIEWS_VIEW_ID_FILES_ZIP: V1ViewsViewIdFilesZip,
        PathValues.V1_VIEWS_VIEW_ID_DEPENDENCIES: V1ViewsViewIdDependencies,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS: V1ViewsViewIdColumns,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID_REMOVE: V1ViewsViewIdColumnsColumnIdRemove,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID_ADD: V1ViewsViewIdColumnsColumnIdAdd,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_BULK: V1ViewsViewIdColumnsBulk,
        PathValues.V1_GRIDS: V1Grids,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES: V1GridsGridIdSettingsCategories,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID_FILES: V1GridsGridIdSettingsCategoriesCategoryIdFiles,
        PathValues.V1_BRANCHES: V1Branches,
        PathValues.V1_BRANCHES_BRANCH_ID_MERGE: V1BranchesBranchIdMerge,
        PathValues.V1_BRANCHES_DIFFCHECK: V1BranchesDiffcheck,
        PathValues.V1_VIEWS_VIEW_ID_RECORDS_ID: V1ViewsViewIdRecordsId,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID: V1ViewsViewIdColumnsColumnId,
        PathValues.V1_GRIDS_GRID_ID: V1GridsGridId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS: V1GridsGridIdSettings,
        PathValues.V1_VIEWS_VIEW_ID: V1ViewsViewId,
        PathValues.V1_VIEWS_VIEW_ID_STATISTIC: V1ViewsViewIdStatistic,
        PathValues.V1_VIEWS_VIEW_ID_RECORDS_RECORD_ID_HISTORIES: V1ViewsViewIdRecordsRecordIdHistories,
        PathValues.V1_VIEWS_VIEW_ID_PATHS_TREE: V1ViewsViewIdPathsTree,
        PathValues.V1_VIEWS_VIEW_ID_FILES_FILE_ID: V1ViewsViewIdFilesFileId,
        PathValues.V1_VIEWS_VIEW_ID_EXPORT: V1ViewsViewIdExport,
        PathValues.V1_TEMPLATEGRIDS: V1TemplateGrids,
        PathValues.V1_TASKS_TASK_ID: V1TasksTaskId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_FILES: V1GridsGridIdSettingsFiles,
        PathValues.V1_BRANCHES_BRANCH_ID: V1BranchesBranchId,
        PathValues.V1_BRANCHES_DIFFCHECK_TASK_ID: V1BranchesDiffcheckTaskId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID_FILES_FILE_ID: V1GridsGridIdSettingsCategoriesCategoryIdFilesFileId,
        PathValues.V1_PROJECTS_PROJECT_ID: V1ProjectsProjectId,
        PathValues.V1_DATABASES_DB_ID: V1DatabasesDbId,
        PathValues.V1_PROJECTS: V1Projects,
        PathValues.V1_DATABASES: V1Databases,
        PathValues.V1_DATABASES_DB_ID_DUPLICATE: V1DatabasesDbIdDuplicate,
        PathValues.V1_GLOSSARIES: V1Glossaries,
        PathValues.V1_GLOSSARIES_ID: V1GlossariesId,
        PathValues.V1_GLOSSARIES_ID_EXPORT: V1GlossariesIdExport,
        PathValues.V1_GLOSSARIES_ID_IMPORT: V1GlossariesIdImport,
        PathValues.V1_TRANSMEMS: V1Transmems,
        PathValues.V1_TRANSMEMS_UPLOAD: V1TransmemsUpload,
        PathValues.V1_TRANSMEMS_TM_ID: V1TransmemsTmId,
        PathValues.V1_TRANSMEMS_TM_ID_CLEANUP: V1TransmemsTmIdCleanup,
        PathValues.V1_TRANSMEMS_TM_ID_EXPORT: V1TransmemsTmIdExport,
        PathValues.V1_TRANSMEMS_TM_ID_IMPORT: V1TransmemsTmIdImport,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_VIEWS_VIEW_ID_SHARES: V1ViewsViewIdShares,
        PathValues.V1_VIEWS_VIEW_ID_PATHS_PATH: V1ViewsViewIdPathsPath,
        PathValues.V1_VIEWS_VIEW_ID_DEPENDENCIES_DEPENDENCY_ID: V1ViewsViewIdDependenciesDependencyId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID: V1GridsGridIdSettingsCategoriesCategoryId,
        PathValues.V1_VIEWS: V1Views,
        PathValues.V1_VIEWS_VIEW_ID_RECORDS: V1ViewsViewIdRecords,
        PathValues.V1_VIEWS_VIEW_ID_PATHS: V1ViewsViewIdPaths,
        PathValues.V1_VIEWS_VIEW_ID_PATHS_MOVE: V1ViewsViewIdPathsMove,
        PathValues.V1_VIEWS_VIEW_ID_MERGE: V1ViewsViewIdMerge,
        PathValues.V1_VIEWS_VIEW_ID_IMPORT: V1ViewsViewIdImport,
        PathValues.V1_VIEWS_VIEW_ID_FILES: V1ViewsViewIdFiles,
        PathValues.V1_VIEWS_VIEW_ID_FILES_ZIP: V1ViewsViewIdFilesZip,
        PathValues.V1_VIEWS_VIEW_ID_DEPENDENCIES: V1ViewsViewIdDependencies,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS: V1ViewsViewIdColumns,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID_REMOVE: V1ViewsViewIdColumnsColumnIdRemove,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID_ADD: V1ViewsViewIdColumnsColumnIdAdd,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_BULK: V1ViewsViewIdColumnsBulk,
        PathValues.V1_GRIDS: V1Grids,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES: V1GridsGridIdSettingsCategories,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID_FILES: V1GridsGridIdSettingsCategoriesCategoryIdFiles,
        PathValues.V1_BRANCHES: V1Branches,
        PathValues.V1_BRANCHES_BRANCH_ID_MERGE: V1BranchesBranchIdMerge,
        PathValues.V1_BRANCHES_DIFFCHECK: V1BranchesDiffcheck,
        PathValues.V1_VIEWS_VIEW_ID_RECORDS_ID: V1ViewsViewIdRecordsId,
        PathValues.V1_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID: V1ViewsViewIdColumnsColumnId,
        PathValues.V1_GRIDS_GRID_ID: V1GridsGridId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS: V1GridsGridIdSettings,
        PathValues.V1_VIEWS_VIEW_ID: V1ViewsViewId,
        PathValues.V1_VIEWS_VIEW_ID_STATISTIC: V1ViewsViewIdStatistic,
        PathValues.V1_VIEWS_VIEW_ID_RECORDS_RECORD_ID_HISTORIES: V1ViewsViewIdRecordsRecordIdHistories,
        PathValues.V1_VIEWS_VIEW_ID_PATHS_TREE: V1ViewsViewIdPathsTree,
        PathValues.V1_VIEWS_VIEW_ID_FILES_FILE_ID: V1ViewsViewIdFilesFileId,
        PathValues.V1_VIEWS_VIEW_ID_EXPORT: V1ViewsViewIdExport,
        PathValues.V1_TEMPLATEGRIDS: V1TemplateGrids,
        PathValues.V1_TASKS_TASK_ID: V1TasksTaskId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_FILES: V1GridsGridIdSettingsFiles,
        PathValues.V1_BRANCHES_BRANCH_ID: V1BranchesBranchId,
        PathValues.V1_BRANCHES_DIFFCHECK_TASK_ID: V1BranchesDiffcheckTaskId,
        PathValues.V1_GRIDS_GRID_ID_SETTINGS_CATEGORIES_CATEGORY_ID_FILES_FILE_ID: V1GridsGridIdSettingsCategoriesCategoryIdFilesFileId,
        PathValues.V1_PROJECTS_PROJECT_ID: V1ProjectsProjectId,
        PathValues.V1_DATABASES_DB_ID: V1DatabasesDbId,
        PathValues.V1_PROJECTS: V1Projects,
        PathValues.V1_DATABASES: V1Databases,
        PathValues.V1_DATABASES_DB_ID_DUPLICATE: V1DatabasesDbIdDuplicate,
        PathValues.V1_GLOSSARIES: V1Glossaries,
        PathValues.V1_GLOSSARIES_ID: V1GlossariesId,
        PathValues.V1_GLOSSARIES_ID_EXPORT: V1GlossariesIdExport,
        PathValues.V1_GLOSSARIES_ID_IMPORT: V1GlossariesIdImport,
        PathValues.V1_TRANSMEMS: V1Transmems,
        PathValues.V1_TRANSMEMS_UPLOAD: V1TransmemsUpload,
        PathValues.V1_TRANSMEMS_TM_ID: V1TransmemsTmId,
        PathValues.V1_TRANSMEMS_TM_ID_CLEANUP: V1TransmemsTmIdCleanup,
        PathValues.V1_TRANSMEMS_TM_ID_EXPORT: V1TransmemsTmIdExport,
        PathValues.V1_TRANSMEMS_TM_ID_IMPORT: V1TransmemsTmIdImport,
    }
)
