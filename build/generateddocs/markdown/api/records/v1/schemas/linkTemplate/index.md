
# Schema for linkTemplate (Schema)

`ogc.api.records.v1.schemas.linkTemplate` *v0.1*

This building block corresponds to the schema for an OGC API Records linkTemplate

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$comment: Adapted from https://raw.githubusercontent.com/opengeospatial/ogcapi-records/master/core/openapi/schemas/linkTemplate.yaml
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.yaml
- type: object
  required:
  - uriTemplate
  properties:
    uriTemplate:
      type: string
      description: Supplies a resolvable URI to a remote resource (or resource fragment).
      example: http://data.example.com/buildings/(building-id}
      x-jsonld-type: xsd:string
      x-jsonld-id: https://www.opengis.net/def/ogc-api/records/uriTemplate
    varBase:
      type: string
      description: The base URI to which the variable name can be appended to retrieve
        the definition of the variable as a JSON Schema fragment.
      format: url
      x-jsonld-id: https://www.opengis.net/def/ogc-api/records/varBase
    variables:
      type: object
      description: This object contains one key per substitution variable in the templated
        URL.  Each key defines the schema of one substitution variable using a JSON
        Schema fragment and can thus include things like the data type of the variable,
        enumerations, minimum values, maximum values, etc.
      x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
      x-jsonld-container: '@index'
      x-jsonld-index: http://purl.org/dc/terms/identifier
      x-jsonld-type: '@json'
x-jsonld-prefixes:
  rec: https://www.opengis.net/def/ogc-api/records/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/schema.yaml)


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
      "@index": "dct:identifier",
      "@type": "@json"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/linkTemplate`

