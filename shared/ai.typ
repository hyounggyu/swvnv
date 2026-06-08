#import "utils.typ": join-ids, para-list

#let ai-model-table(items) = {
  table(
    columns: (auto, 1.2fr, 1fr, 1.6fr, 1fr),
    table.header([ID], [Model], [Task], [Limitation], [System Tests]),
    ..items.map(item => (
      [#item.id],
      [#item.name + " " + item.version],
      [#item.task],
      [#item.intended_use_limitation],
      [#join-ids(item.related_system_tests)]
    )).flatten()
  )
}

#let dataset-table(items) = {
  table(
    columns: (auto, 1.3fr, auto, 1.4fr, 1fr),
    table.header([ID], [Dataset], [Samples], [Purpose], [System Tests]),
    ..items.map(item => (
      [#item.id],
      [#item.name],
      [#str(item.sample_count)],
      [#item.purpose + " / " + item.modality],
      [#join-ids(item.related_system_tests)]
    )).flatten()
  )
}

#let metric-table(items) = {
  table(
    columns: (auto, 1.3fr, 2fr, 1fr),
    table.header([ID], [Metric], [Acceptance Criterion], [System Tests]),
    ..items.map(item => (
      [#item.id],
      [#item.name],
      [#item.acceptance_criterion],
      [#join-ids(item.related_system_tests)]
    )).flatten()
  )
}

#let ai-summary(models, datasets, metrics) = [
  = AI Segmentation Verification Summary

  == AI Model
  #ai-model-table(models)

  == Validation Dataset
  #dataset-table(datasets)

  == Planned Performance Metrics
  #metric-table(metrics)
]

