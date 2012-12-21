
import sparql
import networkx as nx

endpoint="http://dbpedia.org/sparql"
query="""PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select ?philosopher,?influenced,?who,?whom where {
?philosopher rdf:type dbpedia-owl:Philosopher.
?philosopher dbpedia-owl:influenced ?influenced.
?philosopher rdfs:label ?who.
?influenced rdfs:label ?whom.

FILTER (LANG (?who)='en')
FILTER (LANG (?whom)='en')

}"""

s=sparql.Service(endpoint)
result=s.query(query)

g=nx.Graph()
for row in result.fetchall():
  g.add_edge(unicode(row[2]),unicode(row[3]))

nx.write_gexf(g, "philosophers.gexf")  
