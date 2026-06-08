#import "utils.typ": para-list

#let product-summary(project) = [
  = Product Overview

  *Product name:* #project.name \
  *Product code:* #project.product_code \
  *Version:* #project.version \
  *Software safety class:* Class #project.software_safety_class

  == Intended Use
  #project.intended_use

  == Intended Users
  #para-list(project.intended_users)

  == Operating Environment
  #para-list(project.operating_environment)

  == Limitations
  #para-list(project.limitations)
]

#let scope-section(text) = [
  = Scope
  #text
]

