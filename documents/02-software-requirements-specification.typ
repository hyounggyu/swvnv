#import "../shared/template.typ": document-template
#import "../document-data.typ": project, doc, revision-history, requirements, risk-controls
#import "../shared/sections.typ": product-summary
#import "../shared/tables.typ": requirements-table, risk-control-table
#import "../shared/traceability.typ": requirement-traceability

#show: document-template.with(
  project: project(),
  doc: doc("srs"),
  revision_history: revision-history(),
)

#product-summary(project())

= Software Requirements

#requirements-table(requirements())

= Risk Controls Referenced by Requirements

#risk-control-table(risk-controls())

= Requirement Traceability

#requirement-traceability(requirements())
