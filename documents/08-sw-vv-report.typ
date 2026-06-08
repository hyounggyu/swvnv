#import "../shared/template.typ": document
#import "../document-data.typ": project, doc, revision-history, requirements, architecture-items, design-items, unit-tests, integration-tests, system-tests, ai-models, datasets, performance-metrics, risk-controls
#import "../shared/sections.typ": product-summary
#import "../shared/tables.typ": requirements-table, architecture-table, design-table, risk-control-table
#import "../shared/tests.typ": unit-test-section, integration-test-section, system-test-section
#import "../shared/traceability.typ": requirement-traceability, architecture-traceability, design-traceability
#import "../shared/ai.typ": ai-summary

#show: document.with(
  project: project(),
  doc: doc("vv-report"),
  revision_history: revision-history(),
)

#product-summary(project())

= Verification and Validation Summary

This report summarizes planned verification coverage for CT Analysis Workstation. Test execution results and evidence are intentionally out of scope for this initial documentation package.

= Requirements Under Verification

#requirements-table(requirements())

= Architecture and Design Under Verification

== Architecture
#architecture-table(architecture-items())

== Detailed Design
#design-table(design-items())

= Test Coverage

#unit-test-section(unit-tests())

#integration-test-section(integration-tests())

#system-test-section(system-tests())

#ai-summary(ai-models(), datasets(), performance-metrics())

= AI Segmentation Risk Controls

#risk-control-table(risk-controls())

= Traceability Matrices

== Requirement to System Test
#requirement-traceability(requirements())

== Architecture to Integration Test
#architecture-traceability(architecture-items())

== Design to Unit Test
#design-traceability(design-items())
