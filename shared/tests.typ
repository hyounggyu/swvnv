#import "tables.typ": test-table

#let unit-test-section(items) = [
  = Unit Test Cases
  #test-table(items)
]

#let integration-test-section(items) = [
  = Integration Test Cases
  #test-table(items)
]

#let system-test-section(items) = [
  = System Test Cases
  #test-table(items)
]

