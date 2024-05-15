from gridly.paths.v1_glossaries_id.get import ApiForget
from gridly.paths.v1_glossaries_id.put import ApiForput
from gridly.paths.v1_glossaries_id.delete import ApiFordelete


class V1GlossariesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
