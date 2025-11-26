import rdflib


g = rdflib.Graph()
g.parse('build-local/tests/api/records/v1/schemas/linkTemplate/var-exists-fail.ttl', format='turtle')

# Define the SPARQL query
query = """
            PREFIX rec:    <https://www.opengis.net/def/ogc-api/records/>
      prefix oa: <http://www.w3.org/ns/oa#>
      SELECT COUNT(?var) 
      WHERE {
        BIND (rec:hasVariable as ?path)
        $this rec:hasVariable/dct:identifier ?var .
        $this rec:uriTemplate ?template .
        
      }
      GROUP BY $this ?path ?value ?template
      
"""

# Run the query against the local graph
qres = g.query(query)

for row in qres:
    print(f"Subject: {row.s}, Predicate: {row.p}, Object: {row.o}")
    # Or by index:
    # print(f"Subject: {row[0]}, Predicate: {row[1]}, Object: {row[2]}")
