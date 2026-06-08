#import "../shared/template.typ": document
#import "../document-data.typ": project, doc, revision-history, integration-tests
#import "../shared/sections.typ": product-summary
#import "../shared/tests.typ": integration-test-section

#show: document.with(
  project: project(),
  doc: doc("integration-test"),
  revision_history: revision-history(),
)

#product-summary(project())

#integration-test-section(integration-tests())
