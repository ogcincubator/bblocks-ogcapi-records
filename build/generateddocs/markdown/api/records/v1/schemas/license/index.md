
# Schema for license (Schema)

`ogc.api.records.v1.schemas.license` *v0.1*

This building block corresponds to the schema for an OGC API Records license

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
type: string
description: 'A legal document under which the resource is made available.

  If the resource is being made available under a common license

  then use an SPDX license id (https://spdx.org/licenses/).

  If the resource is being made available under multiple common

  licenses then use an SPDX license expression v2.3 string

  (https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/)

  If the resource is being made available under one or more licenses

  that haven''t been assigned an SPDX identifier or one or more custom

  licenses then use a string value of ''other'' and include one or more

  links (rel="license") in the `link` section of the record to the

  file(s) that contains the text of the license(s).

  There is also the case of a resource that is private or unpublished

  and is thus unlicensed; in this case do not register such a resource

  in the catalog in the first place since there is no point in making

  such a resource discoverable.'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/license/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/license/schema.yaml)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/license`

