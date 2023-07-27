"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 4.15.1
    Contact: support@gridly.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gridly.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from gridly.exceptions import ApiAttributeError


def lazy_import():
    from gridly.model.date_time_format import DateTimeFormat
    from gridly.model.formula import Formula
    from gridly.model.number_format import NumberFormat
    from gridly.model.reference import Reference
    globals()['DateTimeFormat'] = DateTimeFormat
    globals()['Formula'] = Formula
    globals()['NumberFormat'] = NumberFormat
    globals()['Reference'] = Reference


class UpdateColumn(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('type',): {
            'SINGLELINE': "singleLine",
            'MULTIPLELINES': "multipleLines",
            'RICHTEXT': "richText",
            'MARKDOWN': "markdown",
            'SINGLESELECTION': "singleSelection",
            'MULTIPLESELECTIONS': "multipleSelections",
            'BOOLEAN': "boolean",
            'NUMBER': "number",
            'DATETIME': "datetime",
            'FILES': "files",
            'REFERENCE': "reference",
            'LOOKUP': "lookup",
            'LANGUAGE': "language",
            'JSON': "json",
            'YAML': "yaml",
            'HTML': "html",
            'FORMULA': "formula",
        },
        ('language_code',): {
            'ENUS': "enUS",
            'ARSA': "arSA",
            'CAES': "caES",
            'ZHCN': "zhCN",
            'ZHTW': "zhTW",
            'DEDE': "deDE",
            'ITIT': "itIT",
            'JAJP': "jaJP",
            'KOKR': "koKR",
            'PLPL': "plPL",
            'PTAO': "ptAO",
            'PTBR': "ptBR",
            'RURU': "ruRU",
            'ESMX': "esMX",
            'ESLA': "esLA",
            'ESES': "esES",
            'BNBD': "bnBD",
            'BGBG': "bgBG",
            'ZHHK': "zhHK",
            'CSCZ': "csCZ",
            'DADK': "daDK",
            'NLNL': "nlNL",
            'FIFI': "fiFI",
            'FRFR': "frFR",
            'FRCA': "frCA",
            'ELGR': "elGR",
            'HEIL': "heIL",
            'HIIN': "hiIN",
            'HUHU': "huHU",
            'IDID': "idID",
            'JWID': "jwID",
            'LVLV': "lvLV",
            'MSMY': "msMY",
            'NONO': "noNO",
            'PTPT': "ptPT",
            'RORO': "roRO",
            'SKSK': "skSK",
            'SVSE': "svSE",
            'TLPH': "tlPH",
            'THTH': "thTH",
            'TRTR': "trTR",
            'UKUA': "ukUA",
            'URIN': "urIN",
            'VIVN': "viVN",
            'AFZA': "afZA",
            'ARAE': "arAE",
            'ARBH': "arBH",
            'ARDZ': "arDZ",
            'AREG': "arEG",
            'ARIQ': "arIQ",
            'ARJO': "arJO",
            'ARKW': "arKW",
            'ARLB': "arLB",
            'ARLY': "arLY",
            'ARMA': "arMA",
            'AROM': "arOM",
            'ARQA': "arQA",
            'ARSY': "arSY",
            'ARTN': "arTN",
            'ARYE': "arYE",
            'AZAZ': "azAZ",
            'BEBY': "beBY",
            'BSBA': "bsBA",
            'CYGB': "cyGB",
            'DEAT': "deAT",
            'DECH': "deCH",
            'DELI': "deLI",
            'DELU': "deLU",
            'DVMV': "dvMV",
            'ENAU': "enAU",
            'ENBZ': "enBZ",
            'ENCA': "enCA",
            'ENGB': "enGB",
            'ENIE': "enIE",
            'ENJM': "enJM",
            'ENNZ': "enNZ",
            'ENPH': "enPH",
            'ENTT': "enTT",
            'ENZA': "enZA",
            'ENZW': "enZW",
            'ENSG': "enSG",
            'ENIN': "enIN",
            'ENGH': "enGH",
            'ENRW': "enRW",
            'ENZM': "enZM",
            'ENKE': "enKE",
            'ENNG': "enNG",
            'ESAR': "esAR",
            'ESBO': "esBO",
            'ESCL': "esCL",
            'ESCO': "esCO",
            'ESCR': "esCR",
            'ESDO': "esDO",
            'ESEC': "esEC",
            'ESGT': "esGT",
            'ESHN': "esHN",
            'ESNI': "esNI",
            'ESPA': "esPA",
            'ESPE': "esPE",
            'ESPR': "esPR",
            'ESPY': "esPY",
            'ESSV': "esSV",
            'ESUY': "esUY",
            'ESVE': "esVE",
            'ETEE': "etEE",
            'EUES': "euES",
            'FAIR': "faIR",
            'FOFO': "foFO",
            'FRBE': "frBE",
            'FRCH': "frCH",
            'FRLU': "frLU",
            'FRMC': "frMC",
            'GLES': "glES",
            'GUIN': "guIN",
            'HRBA': "hrBA",
            'HRHR': "hrHR",
            'HYAM': "hyAM",
            'ISIS': "isIS",
            'ITCH': "itCH",
            'KAGE': "kaGE",
            'KKKZ': "kkKZ",
            'KNIN': "knIN",
            'KOKIN': "kokIN",
            'KYKG': "kyKG",
            'LTLT': "ltLT",
            'MINZ': "miNZ",
            'MKMK': "mkMK",
            'MNMN': "mnMN",
            'MRIN': "mrIN",
            'MSBN': "msBN",
            'MTMT': "mtMT",
            'NBNO': "nbNO",
            'NLBE': "nlBE",
            'NNNO': "nnNO",
            'NSZA': "nsZA",
            'PAIN': "paIN",
            'PSAR': "psAR",
            'QUBO': "quBO",
            'QUEC': "quEC",
            'QUPE': "quPE",
            'SAIN': "saIN",
            'SEFI': "seFI",
            'SENO': "seNO",
            'SESE': "seSE",
            'SLSI': "slSI",
            'SQAL': "sqAL",
            'SRBA': "srBA",
            'SRRS': "srRS",
            'SRME': "srME",
            'SVFI': "svFI",
            'SWKE': "swKE",
            'SYRSY': "syrSY",
            'TAIN': "taIN",
            'TEIN': "teIN",
            'TNZA': "tnZA",
            'TTRU': "ttRU",
            'URPK': "urPK",
            'UZUZ': "uzUZ",
            'XHZA': "xhZA",
            'ZHMO': "zhMO",
            'ZHSG': "zhSG",
            'ZUZA': "zuZA",
            'AM': "am",
            'HY': "hy",
            'AZ': "az",
            'BN': "bn",
            'BS': "bs",
            'CA': "ca",
            'HR': "hr",
            'DA': "da",
            'NL': "nl",
            'EN': "en",
            'FI': "fi",
            'FR': "fr",
            'HI': "hi",
            'HU': "hu",
            'ID': "id",
            'IT': "it",
            'KM': "km",
            'MI': "mi",
            'PS': "ps",
            'RU': "ru",
            'SL': "sl",
            'ES': "es",
            'SW': "sw",
            'TA': "ta",
            'UR': "ur",
            'AF': "af",
            'ET': "et",
            'GL': "gl",
            'JA': "ja",
            'KK': "kk",
            'KY': "ky",
            'MK': "mk",
            'MS': "ms",
            'SE': "se",
            'PL': "pl",
            'PA': "pa",
            'RO': "ro",
            'SK': "sk",
            'SV': "sv",
            'TT': "tt",
            'TE': "te",
            'TR': "tr",
            'UZ': "uz",
            'VI': "vi",
            'EU': "eu",
            'BE': "be",
            'CS': "cs",
            'DE': "de",
            'GU': "gu",
            'HE': "he",
            'IS': "is",
            'KO': "ko",
            'LT': "lt",
            'MR': "mr",
            'MN': "mn",
            'NB': "nb",
            'NN': "nn",
            'PT': "pt",
            'SA': "sa",
            'TN': "tn",
            'UK': "uk",
            'XH': "xh",
            'SQ': "sq",
            'AR': "ar",
            'BG': "bg",
            'ZH': "zh",
            'DV': "dv",
            'FO': "fo",
            'FA': "fa",
            'KA': "ka",
            'EL': "el",
            'KN': "kn",
            'LV': "lv",
            'MT': "mt",
            'QU': "qu",
            'SR': "sr",
            'SI': "si",
            'TL': "tl",
            'TH': "th",
            'CY': "cy",
            'ZU': "zu",
            'NO': "no",
        },
        ('localization_type',): {
            'SOURCELANGUAGE': "sourceLanguage",
            'TARGETLANGUAGE': "targetLanguage",
        },
    }

    validations = {
        ('selection_options',): {
            'max_items': 1000,
            'min_items': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'language_code': (str,),  # noqa: E501
            'localization_type': (str,),  # noqa: E501
            'selection_options': ([str],),  # noqa: E501
            'number_format': (NumberFormat,),  # noqa: E501
            'reference': (Reference,),  # noqa: E501
            'formula': (Formula,),  # noqa: E501
            'date_time_format': (DateTimeFormat,),  # noqa: E501
            'new_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'type': 'type',  # noqa: E501
        'language_code': 'languageCode',  # noqa: E501
        'localization_type': 'localizationType',  # noqa: E501
        'selection_options': 'selectionOptions',  # noqa: E501
        'number_format': 'numberFormat',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'formula': 'formula',  # noqa: E501
        'date_time_format': 'dateTimeFormat',  # noqa: E501
        'new_id': 'newId',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """UpdateColumn - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            language_code (str): [optional]  # noqa: E501
            localization_type (str): [optional]  # noqa: E501
            selection_options ([str]): [optional]  # noqa: E501
            number_format (NumberFormat): [optional]  # noqa: E501
            reference (Reference): [optional]  # noqa: E501
            formula (Formula): [optional]  # noqa: E501
            date_time_format (DateTimeFormat): [optional]  # noqa: E501
            new_id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UpdateColumn - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            language_code (str): [optional]  # noqa: E501
            localization_type (str): [optional]  # noqa: E501
            selection_options ([str]): [optional]  # noqa: E501
            number_format (NumberFormat): [optional]  # noqa: E501
            reference (Reference): [optional]  # noqa: E501
            formula (Formula): [optional]  # noqa: E501
            date_time_format (DateTimeFormat): [optional]  # noqa: E501
            new_id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")