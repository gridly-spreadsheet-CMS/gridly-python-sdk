# gridly.model.create_column.CreateColumn

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**type** | str,  | str,  |  | must be one of ["singleLine", "multipleLines", "richText", "markdown", "singleSelection", "multipleSelections", "boolean", "number", "datetime", "files", "reference", "lookup", "language", "json", "yaml", "html", "formula", ] 
**id** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**editable** | bool,  | BoolClass,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] must be one of ["enUS", "arSA", "caES", "zhCN", "zhTW", "deDE", "itIT", "jaJP", "koKR", "plPL", "ptAO", "ptBR", "ruRU", "esMX", "esLA", "esES", "bnBD", "bgBG", "zhHK", "csCZ", "daDK", "nlNL", "fiFI", "frFR", "frCA", "elGR", "heIL", "hiIN", "huHU", "idID", "jwID", "lvLV", "msMY", "noNO", "ptPT", "roRO", "skSK", "svSE", "tlPH", "thTH", "trTR", "ukUA", "urIN", "viVN", "afZA", "arAE", "arBH", "arDZ", "arEG", "arIQ", "arJO", "arKW", "arLB", "arLY", "arMA", "arOM", "arQA", "arSY", "arTN", "arYE", "azAZ", "beBY", "bsBA", "cyGB", "deAT", "deCH", "deLI", "deLU", "dvMV", "enAU", "enBZ", "enCA", "enGB", "enIE", "enJM", "enNZ", "enPH", "enTT", "enZA", "enZW", "enSG", "enIN", "enGH", "enRW", "enZM", "enKE", "enNG", "esAR", "esBO", "esCL", "esCO", "esCR", "esDO", "esEC", "esGT", "esHN", "esNI", "esPA", "esPE", "esPR", "esPY", "esSV", "esUY", "esVE", "etEE", "euES", "faIR", "foFO", "frBE", "frCH", "frLU", "frMC", "glES", "guIN", "hrBA", "hrHR", "hyAM", "isIS", "itCH", "kaGE", "kkKZ", "knIN", "kokIN", "kyKG", "ltLT", "miNZ", "mkMK", "mnMN", "mrIN", "msBN", "mtMT", "nbNO", "nlBE", "nnNO", "nsZA", "paIN", "psAR", "quBO", "quEC", "quPE", "saIN", "seFI", "seNO", "seSE", "slSI", "sqAL", "srBA", "srRS", "srME", "svFI", "swKE", "syrSY", "taIN", "teIN", "tnZA", "ttRU", "urPK", "uzUZ", "xhZA", "zhMO", "zhSG", "zuZA", "am", "hy", "az", "bn", "bs", "ca", "hr", "da", "nl", "en", "fi", "fr", "hi", "hu", "id", "it", "km", "mi", "ps", "ru", "sl", "es", "sw", "ta", "ur", "af", "et", "gl", "ja", "kk", "ky", "mk", "ms", "se", "pl", "pa", "ro", "sk", "sv", "tt", "te", "tr", "uz", "vi", "eu", "be", "cs", "de", "gu", "he", "is", "ko", "lt", "mr", "mn", "nb", "nn", "pt", "sa", "tn", "uk", "xh", "sq", "ar", "bg", "zh", "dv", "fo", "fa", "ka", "el", "kn", "lv", "mt", "qu", "sr", "si", "tl", "th", "cy", "zu", "no", ] 
**localizationType** | str,  | str,  |  | [optional] must be one of ["sourceLanguage", "targetLanguage", ] 
**numberFormat** | [**NumberFormat**](NumberFormat.md) | [**NumberFormat**](NumberFormat.md) |  | [optional] 
**[selectionOptions](#selectionOptions)** | list, tuple,  | tuple,  |  | [optional] 
**reference** | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | [optional] 
**formula** | [**Formula**](Formula.md) | [**Formula**](Formula.md) |  | [optional] 
**dateTimeFormat** | [**DateTimeFormat**](DateTimeFormat.md) | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# selectionOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

