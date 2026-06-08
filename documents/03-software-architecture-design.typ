#import "../shared/template.typ": document
#import "../document-data.typ": project, doc, revision-history, architecture-items, ai-models
#import "../shared/sections.typ": product-summary
#import "../shared/tables.typ": architecture-table
#import "../shared/traceability.typ": architecture-traceability
#import "../shared/ai.typ": ai-model-table

#show: document.with(
  project: project(),
  doc: doc("sad"),
  revision_history: revision-history(),
)

#product-summary(project())

= Architecture Overview

The software architecture separates CT data import, image viewing, measurement, AI segmentation, overlay rendering, and report export responsibilities.

= Architecture Items

#architecture-table(architecture-items())

= AI Segmentation Architecture

#ai-model-table(ai-models())

= Architecture Traceability

#architecture-traceability(architecture-items())
