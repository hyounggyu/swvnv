#import "../shared/template.typ": document
#import "../document-data.typ": project, doc, revision-history, plan, ai-models, datasets, performance-metrics
#import "../shared/sections.typ": product-summary
#import "../shared/ai.typ": ai-summary

#show: document.with(
  project: project(),
  doc: doc("sdp"),
  revision_history: revision-history(),
)

#product-summary(project())

= Software Development Process

The project uses an incremental software lifecycle with controlled document updates, version control, and review before release.

== Lifecycle Model
#plan().lifecycle_model

== Configuration Management
#plan().configuration_management

== Problem Resolution
#plan().problem_resolution

== Verification Strategy
#plan().verification_strategy

= AI Model Development Controls

#for control in plan().ai_model_controls [
- #control
]

#ai-summary(ai-models(), datasets(), performance-metrics())
