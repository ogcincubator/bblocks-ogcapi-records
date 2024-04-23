---
title: Schema for recordsGeoJSON (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>Schema for recordsGeoJSON</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Schema for recordsGeoJSON (Schema)
---


# Schema for recordsGeoJSON `ogc.api.records.schemas.recordsGeoJSON`

This building block corresponds to the schema for an OGC API Records recordsGeoJSON

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
allOf:
- $ref: https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/featureCollectionGeoJSON.yaml
- type: object
  properties:
    features:
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/recordGeoJSON/schema.yaml
    linkTemplates:
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/linkTemplate/schema.yaml

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-ogcapi-records%2Fbuild%2Fannotated%2Fapi%2Frecords%2Fschemas%2FrecordsGeoJSON%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/recordsGeoJSON/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/recordsGeoJSON/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/recordsGeoJSON/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/schemas/recordsGeoJSON/schema.json</a>

# References

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-ogcapi-records" target="_blank">https://github.com/ogcincubator/bblocks-ogcapi-records</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-ogcapi-records/blob/HEAD/_sources/schemas/recordsGeoJSON" target="_blank">_sources/schemas/recordsGeoJSON</a></code>
