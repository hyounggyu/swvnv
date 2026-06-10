#let project-data = yaml("records/project.yaml")
#let document-data = yaml("records/documents.yaml")
#let plan-data = yaml("records/software-development-plan.yaml")
#let requirement-data = yaml("records/requirements.yaml")
#let architecture-data = yaml("records/architecture.yaml")
#let design-data = yaml("records/detailed-design.yaml")
#let test-data = yaml("records/tests.yaml")
#let ai-model-data = yaml("records/ai-models.yaml")
#let dataset-data = yaml("records/datasets.yaml")
#let metric-data = yaml("records/performance-metrics.yaml")
#let risk-control-data = yaml("records/risk-controls.yaml")

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
