#import "../shared/template.typ": document-template
#import "../document-data.typ": project, doc, revision-history, system-tests, datasets, performance-metrics
#import "../shared/sections.typ": product-summary
#import "../shared/tests.typ": system-test-section
#import "../shared/ai.typ": dataset-table, metric-table

#show: document-template.with(
  project: project(),
  doc: doc("system-test"),
  revision_history: revision-history(),
)

#product-summary(project())

#system-test-section(system-tests())

= AI Segmentation Validation Dataset

#dataset-table(datasets())

= Planned AI Performance Metrics

#metric-table(performance-metrics())
