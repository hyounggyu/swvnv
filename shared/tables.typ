#import "utils.typ": join-ids, para-list

#let requirements-table(items) = {
  table(
    columns: (auto, 1.1fr, 2fr, 1fr),
    table.header([ID], [Title], [Description], [Verified By]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#item.description],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

#let architecture-table(items) = {
  table(
    columns: (auto, 1.2fr, 2fr, 1fr),
    table.header([ID], [Component], [Description], [Verified By]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#item.description],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

#let design-table(items) = {
  table(
    columns: (auto, 1.2fr, 2fr, 1fr),
    table.header([ID], [Design Item], [Description], [Unit Test]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#item.description],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

#let test-table(items) = {
  table(
    columns: (auto, 1.2fr, 1.8fr, 1.8fr, 1fr),
    table.header([ID], [Title], [Procedure], [Acceptance Criteria], [Verifies]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#item.procedure],
      [#item.acceptance_criteria],
      [#join-ids(item.verifies)]
    )).flatten()
  )
}

#let risk-control-table(items) = {
  table(
    columns: (auto, 1.2fr, 1.8fr, 1.8fr, 1fr),
    table.header([ID], [Title], [Risk], [Control], [Verified By]),
    ..items.map(item => (
      [#item.id],
      [#item.title],
      [#item.risk],
      [#item.control],
      [#join-ids(item.verified_by)]
    )).flatten()
  )
}

