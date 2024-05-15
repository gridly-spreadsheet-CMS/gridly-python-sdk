# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from gridly.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    VIEWDEPENDENCY = "view-dependency"
    TASK = "task"
    VIEW = "view"
    PATH = "Path"
    RECORD = "record"
    BRANCH = "branch"
    GRID = "grid"
    SHAREVIEW = "share-view"
    VIEWFILE = "view-file"
    VIEWCOLUMN = "view-column"
    DATABASE = "database"
    PROJECT = "project"
    GLOSSARY = "glossary"
    TRANSMEM = "transmem"
