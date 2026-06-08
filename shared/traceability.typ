#import "utils.typ": join-ids

#let requirement-traceability(requirements) = {
  table(
    columns: (auto, 1.2fr, 1fr, 1fr, 1fr),
    table.header([Requirement], [Title], [Architecture], [Design], [System Test]),
    ..requirements.map(item => (
      [#item.id],
      [#item.title],
      [#join-ids(item.related_architecture)],
      [#join-ids(item.related_design)],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

#let architecture-traceability(items) = {
  table(
    columns: (auto, 1.2fr, 1fr, 1fr, 1fr),
    table.header([Architecture], [Title], [Requirements], [Design], [Integration Test]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#join-ids(item.related_requirements)],
      [#join-ids(item.related_design)],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

#let design-traceability(items) = {
  table(
    columns: (auto, 1.2fr, 1fr, 1fr),
    table.header([Design], [Title], [Architecture], [Unit Test]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#join-ids(item.related_architecture)],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

