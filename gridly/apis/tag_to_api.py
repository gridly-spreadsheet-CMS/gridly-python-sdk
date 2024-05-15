import typing_extensions

from gridly.apis.tags import TagValues
from gridly.apis.tags.view_dependency_api import ViewDependencyApi
from gridly.apis.tags.task_api import TaskApi
from gridly.apis.tags.view_api import ViewApi
from gridly.apis.tags.path_api import PathApi
from gridly.apis.tags.record_api import RecordApi
from gridly.apis.tags.branch_api import BranchApi
from gridly.apis.tags.grid_api import GridApi
from gridly.apis.tags.share_view_api import ShareViewApi
from gridly.apis.tags.view_file_api import ViewFileApi
from gridly.apis.tags.view_column_api import ViewColumnApi
from gridly.apis.tags.database_api import DatabaseApi
from gridly.apis.tags.project_api import ProjectApi
from gridly.apis.tags.glossary_api import GlossaryApi
from gridly.apis.tags.transmem_api import TransmemApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VIEWDEPENDENCY: ViewDependencyApi,
        TagValues.TASK: TaskApi,
        TagValues.VIEW: ViewApi,
        TagValues.PATH: PathApi,
        TagValues.RECORD: RecordApi,
        TagValues.BRANCH: BranchApi,
        TagValues.GRID: GridApi,
        TagValues.SHAREVIEW: ShareViewApi,
        TagValues.VIEWFILE: ViewFileApi,
        TagValues.VIEWCOLUMN: ViewColumnApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.GLOSSARY: GlossaryApi,
        TagValues.TRANSMEM: TransmemApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VIEWDEPENDENCY: ViewDependencyApi,
        TagValues.TASK: TaskApi,
        TagValues.VIEW: ViewApi,
        TagValues.PATH: PathApi,
        TagValues.RECORD: RecordApi,
        TagValues.BRANCH: BranchApi,
        TagValues.GRID: GridApi,
        TagValues.SHAREVIEW: ShareViewApi,
        TagValues.VIEWFILE: ViewFileApi,
        TagValues.VIEWCOLUMN: ViewColumnApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.GLOSSARY: GlossaryApi,
        TagValues.TRANSMEM: TransmemApi,
    }
)
