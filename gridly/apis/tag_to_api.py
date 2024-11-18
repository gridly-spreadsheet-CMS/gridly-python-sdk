import typing_extensions

from gridly.apis.tags import TagValues
from gridly.apis.tags.share_view_api import ShareViewApi
from gridly.apis.tags.database_api import DatabaseApi
from gridly.apis.tags.project_api import ProjectApi
from gridly.apis.tags.glossary_api import GlossaryApi
from gridly.apis.tags.transmem_api import TransmemApi
from gridly.apis.tags.path_api import PathApi
from gridly.apis.tags.branch_api import BranchApi
from gridly.apis.tags.cdn_api import CdnApi
from gridly.apis.tags.grid_api import GridApi
from gridly.apis.tags.record_api import RecordApi
from gridly.apis.tags.task_api import TaskApi
from gridly.apis.tags.view_api import ViewApi
from gridly.apis.tags.view_column_api import ViewColumnApi
from gridly.apis.tags.view_dependency_api import ViewDependencyApi
from gridly.apis.tags.view_file_api import ViewFileApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SHAREVIEW: ShareViewApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.GLOSSARY: GlossaryApi,
        TagValues.TRANSMEM: TransmemApi,
        TagValues.PATH: PathApi,
        TagValues.BRANCH: BranchApi,
        TagValues.CDN: CdnApi,
        TagValues.GRID: GridApi,
        TagValues.RECORD: RecordApi,
        TagValues.TASK: TaskApi,
        TagValues.VIEW: ViewApi,
        TagValues.VIEWCOLUMN: ViewColumnApi,
        TagValues.VIEWDEPENDENCY: ViewDependencyApi,
        TagValues.VIEWFILE: ViewFileApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SHAREVIEW: ShareViewApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.GLOSSARY: GlossaryApi,
        TagValues.TRANSMEM: TransmemApi,
        TagValues.PATH: PathApi,
        TagValues.BRANCH: BranchApi,
        TagValues.CDN: CdnApi,
        TagValues.GRID: GridApi,
        TagValues.RECORD: RecordApi,
        TagValues.TASK: TaskApi,
        TagValues.VIEW: ViewApi,
        TagValues.VIEWCOLUMN: ViewColumnApi,
        TagValues.VIEWDEPENDENCY: ViewDependencyApi,
        TagValues.VIEWFILE: ViewFileApi,
    }
)
