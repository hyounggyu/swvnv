#import "../shared/template.typ": document-template
#import "../document-data.typ": project, doc, revision-history, design-items, ai-models
#import "../shared/sections.typ": product-summary
#import "../shared/tables.typ": design-table
#import "../shared/traceability.typ": design-traceability
#import "../shared/ai.typ": ai-model-table

#show: document-template.with(
  project: project(),
  doc: doc("sdd"),
  revision_history: revision-history(),
)

#product-summary(project())

= Detailed Design Items

#design-table(design-items())

= AI Segmentation Design Context

#ai-model-table(ai-models())

= Design Traceability

#design-traceability(design-items())
