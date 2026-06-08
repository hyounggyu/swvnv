#import "utils.typ": join-ids

#let approvals(approvers) = {
  table(
    columns: (1fr, 1fr, 1fr),
    table.header([Role], [Name], [Signature / Date]),
    ..approvers.map(person => (
      [#person.role],
      [#person.name],
      []
    )).flatten()
  )
}

#let revision-table(history) = {
  table(
    columns: (auto, auto, 2fr, 1fr),
    table.header([Version], [Date], [Description], [Author]),
    ..history.map(item => (
      [#item.version],
      [#item.date],
      [#item.description],
      [#item.author]
    )).flatten()
  )
}

#let document(project: (:), doc: (:), revision_history: (), body) = {
  set document(title: doc.title, author: project.manufacturer.name)
  set page(
    paper: "a4",
    margin: (x: 20mm, y: 18mm),
    header: align(right)[#doc.number #h(1em) #doc.version],
    footer: align(center)[Page #counter(page).display("1")]
  )
  set text(font: "New Computer Modern", size: 10pt)
  set heading(numbering: "1.1")

  align(center)[
    #v(24mm)
    #text(size: 22pt, weight: "bold")[#doc.title]
    #v(8mm)
    #text(size: 14pt)[#project.name]
    #v(16mm)
    #table(
      columns: (45mm, 80mm),
      [Document Number], [#doc.number],
      [Version], [#doc.version],
      [Status], [#doc.status],
      [Manufacturer], [#project.manufacturer.name],
      [Software Safety Class], [Class #project.software_safety_class],
    )
  ]

  pagebreak()

  = Document Control

  == Revision History
  #revision-table(revision_history)

  == Approval
  #approvals(doc.approvers)

  pagebreak()
  outline()
  pagebreak()

  body
}

