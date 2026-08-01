
# Schema for theme (Schema)

`ogc.api.records.v1.schemas.theme` *v0.1*

This building block corresponds to the schema for an OGC API Records theme. This is generalised for reuse by STAC themes extension by allowing either name or title to be mapped to dct:title .

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Themes using URIs
#### json
```json
{
  "concepts": [
    {
      "id": "dobson",
      "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson"
    },
    {
      "id": "filter",
      "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter"
    }
  ],
  "scheme": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/context.jsonld",
  "concepts": [
    {
      "id": "dobson",
      "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson"
    },
    {
      "id": "filter",
      "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter"
    }
  ],
  "scheme": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode"
}
```

#### ttl
```ttl
@prefix thns: <https://w3id.org/ogc/stac/themes/> .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson> thns:id "dobson" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter> thns:id "filter" .

[] thns:concepts <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson>,
        <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter> ;
    thns:scheme "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode" .


```


### Themes using schemes
#### json
```json
{
  "concepts": [
    {
      "id": "geonames::2976077",
      "title": "Forêt de Saou",
      "description": "A very nice forest"
    },
    {
      "id": "geonames::11071625",
      "title": "Auvergne-Rhône-Alpes",
      "description": "A wonderful place for cheese"
    }
  ],
  "scheme": "https://www.geonames.org"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/context.jsonld",
  "concepts": [
    {
      "id": "geonames::2976077",
      "title": "For\u00eat de Saou",
      "description": "A very nice forest"
    },
    {
      "id": "geonames::11071625",
      "title": "Auvergne-Rh\u00f4ne-Alpes",
      "description": "A wonderful place for cheese"
    }
  ],
  "scheme": "https://www.geonames.org"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .

[] thns:concepts [ dcterms:description "A wonderful place for cheese" ;
            dcterms:title "Auvergne-Rhône-Alpes" ;
            thns:id "geonames::11071625" ],
        [ dcterms:description "A very nice forest" ;
            dcterms:title "Forêt de Saou" ;
            thns:id "geonames::2976077" ] ;
    thns:scheme "https://www.geonames.org" .


```

## Schema

```yaml
type: object
required:
- concepts
- scheme
properties:
  concepts:
    type: array
    description: 'One or more entity/concept identifiers from this knowledge

      system. it is recommended that a resolvable URI be used for

      each entity/concept identifier.'
    minItems: 1
    items:
      type: object
      required:
      - id
      properties:
        id:
          type: string
          description: An identifier for the concept.
          x-jsonld-id: https://w3id.org/ogc/stac/themes/id
        title:
          type: string
          description: A human readable title for the concept.
          x-jsonld-id: http://purl.org/dc/terms/title
        description:
          type: string
          description: A human readable description for the concept.
          x-jsonld-id: http://purl.org/dc/terms/description
        url:
          type: string
          format: uri
          description: A URI providing further description of the concept.
          x-jsonld-id: '@id'
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
  scheme:
    type: string
    description: 'An identifier for the knowledge organization system used

      to classify the resource.  It is recommended that the

      identifier be a resolvable URI.  The list of schemes used

      in a searchable catalog can be determined by inspecting

      the server''s OpenAPI document or, if the server implements

      CQL2, by exposing a queryable (e.g. named `scheme`) and

      enumerating the list of schemes in the queryable''s schema

      definition.'
    x-jsonld-id: https://w3id.org/ogc/stac/themes/scheme
x-jsonld-prefixes:
  thns: https://w3id.org/ogc/stac/themes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "thns": "https://w3id.org/ogc/stac/themes/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/theme`

