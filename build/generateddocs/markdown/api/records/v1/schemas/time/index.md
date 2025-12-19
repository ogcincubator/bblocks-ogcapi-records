
# Schema for time (Schema)

`ogc.api.records.v1.schemas.time` *v0.1*

This building block corresponds to the schema for an OGC API Records time

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
nullable: true
type: object
properties:
  date:
    type: string
    pattern: ^\d{4}-\d{2}-\d{2}$
  timestamp:
    type: string
    pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$
  interval:
    type: array
    minItems: 2
    maxItems: 2
    items:
      oneOf:
      - type: string
        pattern: ^\d{4}-\d{2}-\d{2}$
      - type: string
        pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$
      - type: string
        enum:
        - ..
  resolution:
    type: string
    description: Minimum time period resolvable in the dataset, as an ISO 8601 duration

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/time/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/time/schema.yaml)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/time`

