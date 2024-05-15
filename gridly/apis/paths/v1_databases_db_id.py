from gridly.paths.v1_databases_db_id.get import ApiForget
from gridly.paths.v1_databases_db_id.put import ApiForput
from gridly.paths.v1_databases_db_id.delete import ApiFordelete


class V1DatabasesDbId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
