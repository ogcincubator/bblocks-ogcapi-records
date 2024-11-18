
# Schema for language (Schema)

`ogc.api.records.v1.schemas.language` *v0.1*

This building block corresponds to the schema for an OGC API Records language

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
type: object
description: The language used for textual values in this record.
required:
- code
properties:
  code:
    type: string
    description: The language tag as per RFC-5646.
    example:
    - el
  name:
    type: string
    minLength: 1
    description: The untranslated name of the language.
    example:
    - "\u0395\u03BB\u03BB\u03B7\u03BD\u03B9\u03BA\u03AC"
  alternate:
    type: string
    description: The name of the language in another well-understood language, usually
      English.
    example:
    - Greek
  dir:
    type: string
    description: The direction for text in this language. The default, `ltr` (left-to-right),
      represents the most common situation. However, care should be taken to set the
      value of `dir` appropriately if the language direction is not `ltr`. Other values
      supported are `rtl` (right-to-left), `ttb` (top-to-bottom), and `btt` (bottom-to-top).
    enum:
    - ltr
    - rtl
    - ttb
    - btt
    default: ltr

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/language`

