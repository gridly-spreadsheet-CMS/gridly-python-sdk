from gridly.paths.v1_grids_grid_id.get import ApiForget
from gridly.paths.v1_grids_grid_id.delete import ApiFordelete
from gridly.paths.v1_grids_grid_id.patch import ApiForpatch


class V1GridsGridId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
