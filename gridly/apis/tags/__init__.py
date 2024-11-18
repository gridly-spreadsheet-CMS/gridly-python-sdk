# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from gridly.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SHAREVIEW = "share-view"
    DATABASE = "database"
    PROJECT = "project"
    GLOSSARY = "glossary"
    TRANSMEM = "transmem"
    PATH = "Path"
    BRANCH = "branch"
    CDN = "cdn"
    GRID = "grid"
    RECORD = "record"
    TASK = "task"
    VIEW = "view"
    VIEWCOLUMN = "view-column"
    VIEWDEPENDENCY = "view-dependency"
    VIEWFILE = "view-file"
