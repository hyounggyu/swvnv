#let join-ids(ids) = {
  if ids == none or ids.len() == 0 {
    [N/A]
  } else {
    ids.join(", ")
  }
}

#let para-list(items) = {
  if items == none or items.len() == 0 {
    [N/A]
  } else {
    list(..items.map(item => [#item]))
  }
}

