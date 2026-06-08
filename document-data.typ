#let project-data = yaml("sot/project.yaml")
#let document-data = yaml("sot/documents.yaml")
#let plan-data = yaml("sot/software-development-plan.yaml")
#let requirement-data = yaml("sot/requirements.yaml")
#let architecture-data = yaml("sot/architecture.yaml")
#let design-data = yaml("sot/detailed-design.yaml")
#let test-data = yaml("sot/tests.yaml")
#let ai-model-data = yaml("sot/ai-models.yaml")
#let dataset-data = yaml("sot/datasets.yaml")
#let metric-data = yaml("sot/performance-metrics.yaml")
#let risk-control-data = yaml("sot/risk-controls.yaml")

#let project() = project-data.project
#let documents() = document-data.documents
#let revision-history() = document-data.revision_history
#let doc(id) = document-data.documents.find(item => item.id == id)
#let plan() = plan-data.plan
#let requirements() = requirement-data.requirements
#let architecture-items() = architecture-data.architecture_items
#let design-items() = design-data.design_items
#let unit-tests() = test-data.unit_tests
#let integration-tests() = test-data.integration_tests
#let system-tests() = test-data.system_tests
#let ai-models() = ai-model-data.ai_models
#let datasets() = dataset-data.datasets
#let performance-metrics() = metric-data.performance_metrics
#let risk-controls() = risk-control-data.risk_controls
