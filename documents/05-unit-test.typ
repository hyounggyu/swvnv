#import "../shared/template.typ": document
#import "../document-data.typ": project, doc, revision-history, unit-tests
#import "../shared/sections.typ": product-summary
#import "../shared/tests.typ": unit-test-section

#show: document.with(
  project: project(),
  doc: doc("unit-test"),
  revision_history: revision-history(),
)

#product-summary(project())

#unit-test-section(unit-tests())
