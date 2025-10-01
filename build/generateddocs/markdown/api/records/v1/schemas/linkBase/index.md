
# Schema for linkBase (Schema)

`ogc.api.records.v1.schemas.linkBase` *v0.1*

This building block corresponds to the schema for an OGC API Records linkBase

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$comment: Adapted from https://github.com/opengeospatial/ogcapi-records/raw/master/core/openapi/schemas/linkBase.yaml
type: object
properties:
  rel:
    type: string
    description: The type or semantics of the relation.
    example: alternate
    x-jsonld-id: http://www.iana.org/assignments/relation
    x-jsonld-type: '@id'
    x-jsonld-base: http://www.iana.org/assignments/relation/
  type:
    type: string
    description: A hint indicating what the media type of the result of dereferencing
      the link should be.
    example: application/geo+json
    x-jsonld-id: http://purl.org/dc/terms/format
  hreflang:
    type: string
    description: A hint indicating what the language of the result of dereferencing
      the link should be.
    example: en
    x-jsonld-id: http://purl.org/dc/terms/language
  title:
    type: string
    description: Used to label the destination of a link such that it can be used
      as a human-readable identifier.
    example: Trierer Strasse 70, 53115 Bonn
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
  length:
    type: integer
    x-jsonld-id: http://purl.org/dc/terms/extent
  created:
    type: string
    description: Date of creation of the resource pointed to by the link.
    format: date-time
    x-jsonld-id: http://purl.org/dc/terms/created
  updated:
    type: string
    description: Most recent date on which the resource pointed to by the link was
      changed.
    format: date-time
    x-jsonld-id: http://purl.org/dc/terms/modified
x-jsonld-extra-terms:
  href:
    x-jsonld-type: '@id'
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
x-jsonld-prefixes:
  oa: http://www.w3.org/ns/oa#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.yaml)


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
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/linkBase`

