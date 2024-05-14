---
title: Schema for linkBase (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>Schema for linkBase</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Schema for linkBase (Schema)
---


# Schema for linkBase `ogc.api.records.v1.schemas.linkBase`

This building block corresponds to the schema for an OGC API Records linkBase

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-ogcapi-records%2Fbuild%2Fannotated%2Fapi%2Frecords%2Fv1%2Fschemas%2FlinkBase%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
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
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-ogcapi-records%2Fbuild%2Fannotated%2Fapi%2Frecords%2Fv1%2Fschemas%2FlinkBase%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/context.jsonld" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkBase/context.jsonld</a>

# References

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-ogcapi-records" target="_blank">https://github.com/ogcincubator/bblocks-ogcapi-records</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-ogcapi-records/blob/HEAD/_sources/v1/schemas/linkBase" target="_blank">_sources/v1/schemas/linkBase</a></code>

