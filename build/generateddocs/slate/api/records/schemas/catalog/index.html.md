---
title: Schema for catalog (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>Schema for catalog</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Schema for catalog (Schema)
---


# Schema for catalog `ogc.api.records.schemas.catalog`

This building block corresponds to the schema for an OGC API Records catalog

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
allOf:
- $ref: https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/collection.yaml
- type: object
- required:
  - type
  - title
  properties:
    itemType:
      description: If this collection is a homogenous collection of records then itemType
        is a string of fixed value of record. If this collection is a homogenous collection
        of other catalogs then itemType is a string of fixed value of catalog. If
        this collection is a heterogenous collection of records and catalogs then
        itemType is a array indicated that item types of the members of this collections
        (i.e. record and/or catalog).
      oneOf:
      - type: string
        enum:
        - record
        - catalog
      - type: array
        items:
          type: string
          enum:
          - record
          - catalog
    type:
      descripton: Fixed to catalog for collections of records and/or subordinate catalogs.
      type: string
      enum:
      - catalog
    keywords:
      type: array
      description: The topic or topics of the resource. Typically represented using
        free-form keywords, tags, key phrases, or classification codes.
      items:
        type: string
    language:
      description: The language used for textual values in this catalog representation.
      $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/language/schema.yaml
    languages:
      type: array
      description: The list of languages in which this catalog object is available.
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/language/schema.yaml
    recordLanguages:
      type: array
      description: The list of languages in which the records of this catalog available.
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/language/schema.yaml
    created:
      type: string
      description: Date of creation of this catalog.
      format: date-time
    updated:
      type: string
      description: The most recent date on which the catalog was changed.
      format: date-time
    contacts:
      type: array
      description: A list of contacts qualified by their role(s) in association to
        the catalog.
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/contact/schema.yaml
    themes:
      type: array
      description: A knowledge organization system used to classify this catalog.
      minItems: 1
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/theme/schema.yaml
    license:
      $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/license/schema.yaml
    rights:
      type: string
      description: A statement that concerns all rights not addressed by the license
        such as a copyright statement.
    conformsTo:
      type: array
      description: The extensions/conformance classes this catalog object implements.
      items:
        type: string
    linkTemplates:
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/linkTemplate/schema.yaml

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-ogcapi-records%2Fbuild%2Fannotated%2Fapi%2Frecords%2Fschemas%2Fcatalog%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/catalog/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/catalog/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/catalog/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/catalog/schema.json</a>

# References

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-ogcapi-records" target="_blank">https://github.com/ogcincubator/bblocks-ogcapi-records</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-ogcapi-records/blob/HEAD/_sources/schemas/catalog" target="_blank">_sources/schemas/catalog</a></code>

