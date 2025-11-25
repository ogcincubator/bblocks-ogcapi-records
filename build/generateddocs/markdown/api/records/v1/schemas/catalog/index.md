
# Schema for catalog (Schema)

`ogc.api.records.v1.schemas.catalog` *v0.1*

This building block corresponds to the schema for an OGC API Records catalog

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$comment: Adapted from https://raw.githubusercontent.com/opengeospatial/ogcapi-records/master/core/openapi/schemas/catalog.yaml
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-features/build/annotated/api/features/v1/schemas/collection/schema.yaml
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
      description: Fixed to catalog for collections of records and/or subordinate
        catalogs.
      type: string
      enum:
      - Catalog
    keywords:
      type: array
      description: The topic or topics of the resource. Typically represented using
        free-form keywords, tags, key phrases, or classification codes.
      items:
        type: string
    language:
      description: The language used for textual values in this catalog representation.
      $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml
    languages:
      type: array
      description: The list of languages in which this catalog object is available.
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml
    recordLanguages:
      type: array
      description: The list of languages in which the records of this catalog available.
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml
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
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/contact/schema.yaml
    themes:
      type: array
      description: A knowledge organization system used to classify this catalog.
      minItems: 1
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/schema.yaml
    license:
      $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/license/schema.yaml
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
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/catalog/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/catalog/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rel": {
      "@context": {
        "@base": "http://www.iana.org/assignments/relation/"
      },
      "@id": "http://www.iana.org/assignments/relation",
      "@type": "@id"
    },
    "type": "dct:format",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "concepts": {
      "@context": {
        "id": "thns:id",
        "title": "dct:title",
        "description": "dct:description",
        "url": "@id"
      },
      "@id": "thns:concepts",
      "@container": "@set"
    },
    "scheme": "thns:scheme",
    "created": "dct:created",
    "updated": "dct:modified",
    "uriTemplate": {
      "@type": "xsd:string",
      "@id": "rec:uriTemplate"
    },
    "varBase": "rec:varBase",
    "variables": {
      "@id": "rec:hasVariable",
      "@container": "@index",
      "@index": "dct:identifier"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/catalog/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/catalog`

