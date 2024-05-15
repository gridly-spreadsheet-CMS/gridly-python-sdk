from gridly.paths.v1_views_view_id_dependencies.get import ApiForget
from gridly.paths.v1_views_view_id_dependencies.post import ApiForpost
from gridly.paths.v1_views_view_id_dependencies.delete import ApiFordelete


class V1ViewsViewIdDependencies(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
