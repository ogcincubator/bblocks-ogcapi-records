
# Schema for linkTemplate (Schema)

`ogc.api.records.v1.schemas.linkTemplate` *v0.1*

This building block corresponds to the schema for an OGC API Records linkTemplate.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Link Template

### JSON-LD mapping

This Building block maps variables to **blank nodes** - this means that multiple mappings can co-exist in a system without clashing, even if the same variable name is re-used.

(if identification of variables is required at a global level @id can be used in variable names)

### Tests:
 
tests if variables present in uriTemplates exist in variable declarations using SHACL
## Examples

### OGC API spec example of record
This example is to test records examples.
#### json
```json
{
  "rel": "describes",
  "title": "World Ozone and Ultraviolet Radiation Data Centre (WOUDC) stations",
  "uriTemplate": "https://geo.woudc.org/ows?service=WMS&version=1.3.0&request=GetMap&crs={crs}&bbox={bbox}&layers=stations&width={width}&height={height}&format={format}",
  "variables": {
    "bbox": {
      "description": "...",
      "type": "array",
      "items": {
        "type": "number",
        "format": "double"
      },
      "minItems": 4,
      "maxItems": 4
    },
    "crs": {
      "@id": "https://org.org/some-standard-param-set/crs",
      "description": "...",
      "type": "string",
      "enum": [
        "EPSG:4326",
        "EPSG:3857"
      ]
    },
    "width": {
      "description": "...",
      "type": "number",
      "format": "integer",
      "minimum": 600,
      "maximum": 5000
    },
    "height": {
      "description": "...",
      "type": "number",
      "format": "integer",
      "minimum": 600,
      "maximum": 5000
    },
    "format": {
      "type": "string",
      "enum": [
        "application/vnd.google-earth.kml+xml",
        "application/vnd.google-earth.kmz",
        "image/png",
        "image/jpeg",
        "image/gif",
        "image/png; mode=8bit",
        "application/x-pdf",
        "image/svg+xml",
        "image/tiff"
      ]
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/context.jsonld",
  "rel": "describes",
  "title": "World Ozone and Ultraviolet Radiation Data Centre (WOUDC) stations",
  "uriTemplate": "https://geo.woudc.org/ows?service=WMS&version=1.3.0&request=GetMap&crs={crs}&bbox={bbox}&layers=stations&width={width}&height={height}&format={format}",
  "variables": {
    "bbox": {
      "description": "...",
      "type": "array",
      "items": {
        "type": "number",
        "format": "double"
      },
      "minItems": 4,
      "maxItems": 4
    },
    "crs": {
      "@id": "https://org.org/some-standard-param-set/crs",
      "description": "...",
      "type": "string",
      "enum": [
        "EPSG:4326",
        "EPSG:3857"
      ]
    },
    "width": {
      "description": "...",
      "type": "number",
      "format": "integer",
      "minimum": 600,
      "maximum": 5000
    },
    "height": {
      "description": "...",
      "type": "number",
      "format": "integer",
      "minimum": 600,
      "maximum": 5000
    },
    "format": {
      "type": "string",
      "enum": [
        "application/vnd.google-earth.kml+xml",
        "application/vnd.google-earth.kmz",
        "image/png",
        "image/jpeg",
        "image/gif",
        "image/png; mode=8bit",
        "application/x-pdf",
        "image/svg+xml",
        "image/tiff"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://org.org/some-standard-param-set/crs> dct:format "string" ;
    dct:identifier "crs" .

[] rdfs:label "World Ozone and Ultraviolet Radiation Data Centre (WOUDC) stations" ;
    ns1:relation <http://www.iana.org/assignments/relation/describes> ;
    rec:hasVariable [ dct:format "number" ;
            dct:identifier "height" ],
        [ dct:format "number" ;
            dct:identifier "width" ],
        [ dct:format "string" ;
            dct:identifier "format" ],
        [ dct:format "array" ;
            dct:identifier "bbox" ],
        <https://org.org/some-standard-param-set/crs> ;
    rec:uriTemplate "https://geo.woudc.org/ows?service=WMS&version=1.3.0&request=GetMap&crs={crs}&bbox={bbox}&layers=stations&width={width}&height={height}&format={format}"^^xsd:string .


```

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
      "@index": "dct:identifier"
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

