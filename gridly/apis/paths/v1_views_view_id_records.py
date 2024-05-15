from gridly.paths.v1_views_view_id_records.get import ApiForget
from gridly.paths.v1_views_view_id_records.post import ApiForpost
from gridly.paths.v1_views_view_id_records.delete import ApiFordelete
from gridly.paths.v1_views_view_id_records.patch import ApiForpatch


class V1ViewsViewIdRecords(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
