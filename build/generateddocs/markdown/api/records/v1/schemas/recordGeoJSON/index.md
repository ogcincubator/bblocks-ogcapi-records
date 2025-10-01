
# Schema for recordGeoJSON (Schema)

`ogc.api.records.v1.schemas.recordGeoJSON` *v0.1*

This building block corresponds to the schema for an OGC API Records recordGeoJSON

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## OGC API records schema

OGC API Record schema as a building block, with documented examples.
## Examples

### OGC API spec example of record
This example is to test records examples.
#### json
```json
{
  "id": "urn:x-wmo:md:int.wmo.wis::https://geo.woudc.org/def/data/ozone/total-column-ozone/totalozone",
  "type": "Feature",
  "time": {
    "interval": [
      "1924-08-17T00:00:00Z",
      ".."
    ],
    "resolution": "P1D"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180,
          -90
        ],
        [
          -180,
          90
        ],
        [
          180,
          90
        ],
        [
          180,
          -90
        ],
        [
          -180,
          -90
        ]
      ]
    ]
  },
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/record-core"
  ],
  "properties": {
    "created": "2021-02-08T00:00:00Z",
    "updated": "2021-02-08T00:00:00Z",
    "type": "dataset",
    "title": "Total Ozone - daily observations",
    "description": "A measurement of the total amount of atmospheric ozone in a given column from the surface to the edge of the atmosphere. Ground based instruments such as spectrophotometers and ozonemeters are used to measure results daily",
    "keywords": [
      "total",
      "ozone",
      "level 1.0",
      "column",
      "dobson",
      "brewer",
      "saoz"
    ],
    "language": {
      "code": "en-CA",
      "name": "English (Canada)"
    },
    "languages": [
      {
        "code": "en-CA",
        "name": "English (Canada)"
      },
      {
        "code": "fr-CA",
        "name": "French (Canada)"
      }
    ],
    "externalIds": [
      {
        "scheme": "WMO:WIS",
        "value": "urn:x-wmo:md:int.wmo.wis::https://geo.woudc.org/def/data/ozone/total-column-ozone/totalozone"
      }
    ],
    "contacts": [
      {
        "name": "World Ozone and Ultraviolet Radiation Data Centre",
        "links": [
          {
            "href": "https://woudc.org",
            "rel": "about",
            "type": "text/html"
          }
        ],
        "contactInstructions": "SEE PAGE: https://woudc.org/contact.php",
        "roles": [
          "publisher"
        ]
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "dobson",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson"
          },
          {
            "id": "brewer",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_brewer"
          },
          {
            "id": "vassey",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_vassey"
          },
          {
            "id": "pion",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_pion"
          },
          {
            "id": "microtops",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_microtops"
          },
          {
            "id": "spectral",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_spectral"
          },
          {
            "id": "hoelper",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_hoelper"
          },
          {
            "id": "saoz",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_saoz"
          },
          {
            "id": "filter",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter"
          }
        ],
        "scheme": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode"
      },
      {
        "concepts": [
          {
            "id": "atmosphericComposition",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_atmosphericComposition"
          },
          {
            "id": "pollution",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_pollution"
          },
          {
            "id": "observationPlatform",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_observationPlatform"
          },
          {
            "id": "rocketSounding",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_rocketSounding"
          }
        ],
        "scheme": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode"
      }
    ],
    "formats": [
      {
        "name": "TEXT",
        "mediaType": "text/plain"
      },
      {
        "name": "CSV",
        "mediaType": "text/csv"
      },
      {
        "name": "GML2",
        "mediaType": "text/xml; subtype=gml/2.1.2"
      },
      {
        "name": "GML3",
        "mediaType": "text/xml; subtype=gml/3.1.1"
      },
      {
        "name": "SHAPEFILE",
        "mediaType": "application/vnd.shp"
      },
      {
        "name": "KML",
        "mediaType": "application/vnd.google-earth.kml+xml"
      },
      {
        "name": "KMZ",
        "mediaType": "application/vnd.google-earth.kmz"
      },
      {
        "name": "GeoJSON",
        "mediaType": "application/geo+json"
      },
      {
        "name": "PNG",
        "mediaType": "image/png"
      },
      {
        "name": "JPEG",
        "mediaType": "image/jpeg"
      },
      {
        "name": "GIF",
        "mediaType": "image/gif"
      },
      {
        "name": "PDF",
        "mediaType": "application/x-pdf"
      },
      {
        "name": "SVG",
        "mediaType": "image/svg+xml"
      },
      {
        "name": "TIFF",
        "mediaType": "image/tiff"
      }
    ],
    "license": "other"
  },
  "linkTemplates": [
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
    },
    {
      "rel": "describes",
      "title": "World Ozone and Ultraviolet Radiation Data Centre (WOUDC) stations",
      "uriTemplate": "https://geo.woudc.org/ows?service=WFS&version=1.1.0&request=GetFeature&typeName=woudc:totalozone&maxFeatures={maxFeatures}&outputFormat={outputFormat}",
      "variables": {
        "maxFeatures": {
          "type": "number",
          "default": 10
        },
        "outputFormat": {
          "type": "string",
          "enum": [
            "text/xml; subtype=gml/3.1.1",
            "text/xml; subtype=gml/2.1.2; driver=ogr",
            "application/json; subtype=geojson",
            "application/vnd.google-earth.kml+xml",
            "application/vnd.shp",
            "text/plain",
            "text/csv"
          ],
          "default": "text/xml; subtype=gml/2.1.2; driver=ogr"
        }
      }
    }
  ],
  "links": [
    {
      "rel": "collection",
      "href": "https://woudc.org/data/dataset_info.php"
    },
    {
      "rel": "describes",
      "title": "OGC Web Map Service (WMS)",
      "href": "https://geo.woudc.org/ows?service=WMS&request=GetCapabilities"
    },
    {
      "rel": "describes",
      "title": "OGC Web Feature Service (WFS)",
      "href": "https://geo.woudc.org/ows?service=WFS&request=GetCapabilities"
    },
    {
      "rel": "preview",
      "type": "image/png",
      "title": "Total Ozone Preview Image",
      "href": "https://woudc.org/data/preview.png"
    },
    {
      "rel": "enclosure",
      "type": "text/html",
      "title": "Web Accessible Folder (WAF)",
      "href": "https://woudc.org/archive/Archive-NewFormat/TotalOzone_1.0_1",
      "created": "2015-01-23T00:00:00Z",
      "updated": "2015-01-23T00:00:00Z"
    },
    {
      "rel": "enclosure",
      "type": "application/zip",
      "title": "Static dataset archive file",
      "href": "https://woudc.org/archive/Summaries/dataset-snapshots/totalozone.zip",
      "created": "2015-01-23T00:00:00Z",
      "updated": "2015-01-23T00:00:00Z"
    },
    {
      "rel": "search",
      "type": "text/html",
      "title": "Data Search / Download User Interface",
      "href": "https://woudc.org/data/explore.php?dataset=totalozone"
    },
    {
      "rel": "license",
      "href": "https://woudc.org/about/data-policy.php"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/context.jsonld",
  "id": "urn:x-wmo:md:int.wmo.wis::https://geo.woudc.org/def/data/ozone/total-column-ozone/totalozone",
  "type": "Feature",
  "time": {
    "interval": [
      "1924-08-17T00:00:00Z",
      ".."
    ],
    "resolution": "P1D"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180,
          -90
        ],
        [
          -180,
          90
        ],
        [
          180,
          90
        ],
        [
          180,
          -90
        ],
        [
          -180,
          -90
        ]
      ]
    ]
  },
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-records-1/1.0/conf/record-core"
  ],
  "properties": {
    "created": "2021-02-08T00:00:00Z",
    "updated": "2021-02-08T00:00:00Z",
    "type": "dataset",
    "title": "Total Ozone - daily observations",
    "description": "A measurement of the total amount of atmospheric ozone in a given column from the surface to the edge of the atmosphere. Ground based instruments such as spectrophotometers and ozonemeters are used to measure results daily",
    "keywords": [
      "total",
      "ozone",
      "level 1.0",
      "column",
      "dobson",
      "brewer",
      "saoz"
    ],
    "language": {
      "code": "en-CA",
      "name": "English (Canada)"
    },
    "languages": [
      {
        "code": "en-CA",
        "name": "English (Canada)"
      },
      {
        "code": "fr-CA",
        "name": "French (Canada)"
      }
    ],
    "externalIds": [
      {
        "scheme": "WMO:WIS",
        "value": "urn:x-wmo:md:int.wmo.wis::https://geo.woudc.org/def/data/ozone/total-column-ozone/totalozone"
      }
    ],
    "contacts": [
      {
        "name": "World Ozone and Ultraviolet Radiation Data Centre",
        "links": [
          {
            "href": "https://woudc.org",
            "rel": "about",
            "type": "text/html"
          }
        ],
        "contactInstructions": "SEE PAGE: https://woudc.org/contact.php",
        "roles": [
          "publisher"
        ]
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "dobson",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson"
          },
          {
            "id": "brewer",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_brewer"
          },
          {
            "id": "vassey",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_vassey"
          },
          {
            "id": "pion",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_pion"
          },
          {
            "id": "microtops",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_microtops"
          },
          {
            "id": "spectral",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_spectral"
          },
          {
            "id": "hoelper",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_hoelper"
          },
          {
            "id": "saoz",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_saoz"
          },
          {
            "id": "filter",
            "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter"
          }
        ],
        "scheme": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode"
      },
      {
        "concepts": [
          {
            "id": "atmosphericComposition",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_atmosphericComposition"
          },
          {
            "id": "pollution",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_pollution"
          },
          {
            "id": "observationPlatform",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_observationPlatform"
          },
          {
            "id": "rocketSounding",
            "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_rocketSounding"
          }
        ],
        "scheme": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode"
      }
    ],
    "formats": [
      {
        "name": "TEXT",
        "mediaType": "text/plain"
      },
      {
        "name": "CSV",
        "mediaType": "text/csv"
      },
      {
        "name": "GML2",
        "mediaType": "text/xml; subtype=gml/2.1.2"
      },
      {
        "name": "GML3",
        "mediaType": "text/xml; subtype=gml/3.1.1"
      },
      {
        "name": "SHAPEFILE",
        "mediaType": "application/vnd.shp"
      },
      {
        "name": "KML",
        "mediaType": "application/vnd.google-earth.kml+xml"
      },
      {
        "name": "KMZ",
        "mediaType": "application/vnd.google-earth.kmz"
      },
      {
        "name": "GeoJSON",
        "mediaType": "application/geo+json"
      },
      {
        "name": "PNG",
        "mediaType": "image/png"
      },
      {
        "name": "JPEG",
        "mediaType": "image/jpeg"
      },
      {
        "name": "GIF",
        "mediaType": "image/gif"
      },
      {
        "name": "PDF",
        "mediaType": "application/x-pdf"
      },
      {
        "name": "SVG",
        "mediaType": "image/svg+xml"
      },
      {
        "name": "TIFF",
        "mediaType": "image/tiff"
      }
    ],
    "license": "other"
  },
  "linkTemplates": [
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
    },
    {
      "rel": "describes",
      "title": "World Ozone and Ultraviolet Radiation Data Centre (WOUDC) stations",
      "uriTemplate": "https://geo.woudc.org/ows?service=WFS&version=1.1.0&request=GetFeature&typeName=woudc:totalozone&maxFeatures={maxFeatures}&outputFormat={outputFormat}",
      "variables": {
        "maxFeatures": {
          "type": "number",
          "default": 10
        },
        "outputFormat": {
          "type": "string",
          "enum": [
            "text/xml; subtype=gml/3.1.1",
            "text/xml; subtype=gml/2.1.2; driver=ogr",
            "application/json; subtype=geojson",
            "application/vnd.google-earth.kml+xml",
            "application/vnd.shp",
            "text/plain",
            "text/csv"
          ],
          "default": "text/xml; subtype=gml/2.1.2; driver=ogr"
        }
      }
    }
  ],
  "links": [
    {
      "rel": "collection",
      "href": "https://woudc.org/data/dataset_info.php"
    },
    {
      "rel": "describes",
      "title": "OGC Web Map Service (WMS)",
      "href": "https://geo.woudc.org/ows?service=WMS&request=GetCapabilities"
    },
    {
      "rel": "describes",
      "title": "OGC Web Feature Service (WFS)",
      "href": "https://geo.woudc.org/ows?service=WFS&request=GetCapabilities"
    },
    {
      "rel": "preview",
      "type": "image/png",
      "title": "Total Ozone Preview Image",
      "href": "https://woudc.org/data/preview.png"
    },
    {
      "rel": "enclosure",
      "type": "text/html",
      "title": "Web Accessible Folder (WAF)",
      "href": "https://woudc.org/archive/Archive-NewFormat/TotalOzone_1.0_1",
      "created": "2015-01-23T00:00:00Z",
      "updated": "2015-01-23T00:00:00Z"
    },
    {
      "rel": "enclosure",
      "type": "application/zip",
      "title": "Static dataset archive file",
      "href": "https://woudc.org/archive/Summaries/dataset-snapshots/totalozone.zip",
      "created": "2015-01-23T00:00:00Z",
      "updated": "2015-01-23T00:00:00Z"
    },
    {
      "rel": "search",
      "type": "text/html",
      "title": "Data Search / Download User Interface",
      "href": "https://woudc.org/data/explore.php?dataset=totalozone"
    },
    {
      "rel": "license",
      "href": "https://woudc.org/about/data-policy.php"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:x-wmo:md:int.wmo.wis::https://geo.woudc.org/def/data/ozone/total-column-ozone/totalozone> rdfs:label "Total Ozone - daily observations" ;
    dct:created "2021-02-08T00:00:00Z" ;
    dct:format "Feature",
        "dataset" ;
    dct:modified "2021-02-08T00:00:00Z" ;
    rdfs:seeAlso [ rdfs:label "Web Accessible Folder (WAF)" ;
            dct:created "2015-01-23T00:00:00Z" ;
            dct:modified "2015-01-23T00:00:00Z" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/enclosure> ;
            oa:hasTarget <https://woudc.org/archive/Archive-NewFormat/TotalOzone_1.0_1> ],
        [ rdfs:label "Data Search / Download User Interface" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/search> ;
            oa:hasTarget <https://woudc.org/data/explore.php?dataset=totalozone> ],
        [ rdfs:label "OGC Web Feature Service (WFS)" ;
            ns1:relation <http://www.iana.org/assignments/relation/describes> ;
            oa:hasTarget <https://geo.woudc.org/ows?service=WFS&request=GetCapabilities> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://woudc.org/data/dataset_info.php> ],
        [ rdfs:label "OGC Web Map Service (WMS)" ;
            ns1:relation <http://www.iana.org/assignments/relation/describes> ;
            oa:hasTarget <https://geo.woudc.org/ows?service=WMS&request=GetCapabilities> ],
        [ rdfs:label "Static dataset archive file" ;
            dct:created "2015-01-23T00:00:00Z" ;
            dct:modified "2015-01-23T00:00:00Z" ;
            dct:type "application/zip" ;
            ns1:relation <http://www.iana.org/assignments/relation/enclosure> ;
            oa:hasTarget <https://woudc.org/archive/Summaries/dataset-snapshots/totalozone.zip> ],
        [ rdfs:label "Total Ozone Preview Image" ;
            dct:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/preview> ;
            oa:hasTarget <https://woudc.org/data/preview.png> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://woudc.org/about/data-policy.php> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -180 -90 ) ( -180 90 ) ( 180 90 ) ( 180 -90 ) ( -180 -90 ) ) ) ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Normative records schema - adapted from https://raw.githubusercontent.com/opengeospatial/ogcapi-records/master/core/openapi/schemas/recordGeoJSON.yaml
type: object
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
required:
- id
- type
- geometry
- properties
- links
properties:
  id:
    type: string
    description: A unique identifier of the catalog record.
  conformsTo:
    type: array
    items:
      type: string
  type:
    type: string
    enum:
    - Feature
  time:
    oneOf:
    - enum:
      - null
    - $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/time/schema.yaml
  geometry:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml#/properties/geometry
  properties:
    type: object
    properties:
      created:
        type: string
        description: Date of creation of this record.
        format: date-time
      updated:
        type: string
        description: The most recent date on which the record was changed.
        format: date-time
      type:
        type: string
        description: The nature or genre of the resource. The value should be a code,
          convenient for filtering records. Where available, a link to the canonical
          URI of the record type resource will be added to the 'links' property.
        maxLength: 64
      title:
        type: string
        description: A human-readable name given to the resource.
      description:
        type: string
        description: A free-text account of the resource.
      keywords:
        type: array
        description: The topic or topics of the resource. Typically represented using
          free-form keywords, tags, key phrases, or classification codes.
        items:
          type: string
      language:
        description: The language used for textual values in this record representation.
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml
      languages:
        type: array
        description: This list of languages in which this record is available.
        items:
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml
      resourceLanguages:
        type: array
        description: The list of languages in which the resource described by this
          record is available.
        items:
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/language/schema.yaml
      externalIds:
        type: array
        description: An identifier for the resource assigned by an external (to the
          catalog) entity.
        items:
          type: object
          properties:
            scheme:
              type: string
              description: A reference to an authority or identifier for a knowledge
                organization system from which the external identifier was obtained.
                It is recommended that the identifier be a resolvable URI.
            value:
              type: string
              description: The value of the identifier.
          required:
          - value
      themes:
        type: array
        description: A knowledge organization system used to classify the resource.
        minItems: 1
        items:
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/schema.yaml
      formats:
        type: array
        description: A list of available distributions of the resource.
        items:
          type: string
      contacts:
        type: array
        description: A list of contacts qualified by their role(s) in association
          to the record or the resource described by the record.
        items:
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/contact/schema.yaml
      license:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/license/schema.yaml
      rights:
        type: string
        description: A statement that concerns all rights not addressed by the license
          such as a copyright statement.
  links:
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/link/schema.yaml
  linkTemplates:
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/linkTemplate/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "type": "dct:format",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type"
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "type": "dct:type"
      },
      "@id": "rdfs:seeAlso"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
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
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "created": "dct:created",
    "updated": "dct:modified",
    "uriTemplate": {
      "@type": "xsd:string",
      "@id": "oa:hasTarget"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/recordGeoJSON`

