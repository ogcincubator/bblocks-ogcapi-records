
# Schema for contact (Schema)

`ogc.api.records.v1.schemas.contact` *v0.1*

This building block corresponds to the schema for an OGC API Records contact

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$comment: Adapted from https://raw.githubusercontent.com/opengeospatial/ogcapi-records/master/core/openapi/schemas/contact.yaml
type: object
description: 'Identification of, and means of communication with, person responsible

  for the resource.'
anyOf:
- required:
  - name
- required:
  - organization
properties:
  identifier:
    type: string
    description: A value uniquely identifying a contact.
  name:
    type: string
    description: The name of the responsible person.
  position:
    type: string
    description: The name of the role or position of the responsible person taken
      from the organization's formal organizational hierarchy or chart.
  organization:
    type: string
    description: Organization/affiliation of the contact.
  logo:
    description: Graphic identifying a contact. The link relation should be `icon`
      and the media type should be an image media type.
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
    - type: object
      required:
      - rel
      - type
      properties:
        rel:
          enum:
          - icon
  phones:
    type: array
    description: Telephone numbers at which contact can be made.
    items:
      type: object
      required:
      - value
      properties:
        value:
          type: string
          description: The value is the phone number itself.
          pattern: ^\+[1-9]{1}[0-9]{3,14}$
          example: '+14165550142'
        roles:
          description: The type of phone number (e.g. home, work, fax, etc.).
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/roles/schema.yaml
  emails:
    type: array
    description: Email addresses at which contact can be made.
    items:
      type: object
      required:
      - value
      properties:
        value:
          type: string
          description: The value is the email number itself.
          format: email
        roles:
          description: The type of email (e.g. home, work, etc.).
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/roles/schema.yaml
  addresses:
    type: array
    description: Physical location at which contact can be made.
    items:
      type: object
      properties:
        deliveryPoint:
          type: array
          description: Address lines for the location.
          items:
            type: string
        city:
          type: string
          description: City for the location.
        administrativeArea:
          type: string
          description: State or province of the location.
        postalCode:
          type: string
          description: ZIP or other postal code.
        country:
          type: string
          description: Country of the physical address.  ISO 3166-1 is recommended.
        roles:
          description: The type of address (e.g. office, home, etc.).
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/roles/schema.yaml
  links:
    type: array
    description: On-line information about the contact.
    items:
      allOf:
      - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
      - type: object
        required:
        - type
  hoursOfService:
    type: string
    description: Time period when the contact can be contacted.
    example: 'Hours: Mo-Fr 10am-7pm Sa 10am-22pm Su 10am-21pm'
  contactInstructions:
    type: string
    description: 'Supplemental instructions on how or when to contact the

      responsible party.'
  roles:
    description: The set of named duties, job functions and/or permissions associated
      with this contact. (e.g. developer, administrator, etc.).
    $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/roles/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/contact/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/contact/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "identifier": {},
    "name": {},
    "position": {},
    "organization": {},
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
    "anchor": {},
    "type": "dct:type",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "logo": {},
    "value": {},
    "roles": {},
    "phones": {},
    "emails": {},
    "deliveryPoint": {},
    "city": {},
    "administrativeArea": {},
    "postalCode": {},
    "country": {},
    "addresses": {},
    "links": {},
    "hoursOfService": {},
    "contactInstructions": {},
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/contact/context.jsonld)

## Sources

* [OGC API Records - Draft](https://docs.ogc.org/DRAFTS/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-ogcapi-records](https://github.com/ogcincubator/bblocks-ogcapi-records)
* Path: `_sources/v1/schemas/contact`

