
# Schema for recordsGeoJSON (Schema)

`ogc.api.records.v1.schemas.recordsGeoJSON` *v0.1*

This building block corresponds to the schema for an OGC API Records recordsGeoJSON

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Adapted from https://raw.githubusercontent.com/opengeospatial/ogcapi-records/master/core/openapi/schemas/recordGeoJSON.yaml
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-features/build/annotated/api/features/v1/schemas/collections/schema.yaml
- type: object
  properties:
    features:
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/schema.yaml
    linkTemplates:
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordsGeoJSON/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordsGeoJSON/schema.yaml)


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
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "uriTemplate": {
      "@type": "xsd:string",
      "@id": "oa:hasTarget"
    },
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type"
      },
      "@id": "geojson:geometry"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "links": {
      "@context": {
        "type": "dct:type"
      },
      "@id": "rdfs:seeAlso"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "geojson": "https://purl.org/geojson/vocab#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordsGeoJSON/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/recordsGeoJSON`

