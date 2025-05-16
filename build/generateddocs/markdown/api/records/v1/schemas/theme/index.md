
# Schema for theme (Schema)

`ogc.api.records.v1.schemas.theme` *v0.1*

This building block corresponds to the schema for an OGC API Records theme

[*Status*](http://www.opengis.net/def/status): Under development

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
        title:
          type: string
          description: A human readable title for the concept.
        description:
          type: string
          description: A human readable description for the concept.
        url:
          type: string
          format: uri
          description: A URI providing further description of the concept.
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

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/theme/schema.yaml)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/theme`

