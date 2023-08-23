# Phase 3 Final Project Requirements

In this project, we're going to use these skills to create a CLI. You won't be able to fit everything in from phase 3, but the following are the minimum requirements:

- A CLI application that
  - solves a real-world problem
  - adheres to best practices.
- A database created with SQLAlchemy
  - Modified with SQLAlchemy ORM
  - 2+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists
- Use of dictionaries

Stretch goals for project:

- A database created and modified with SQLAlchemy ORM with 3+ related tables.
- Use of many-to-many relationships with SQLAlchemy ORM.
- Use of additional data structures, such as ranges and tuples.

## Project Proposals

# Idea 1

#### Main idea:

A smoothie recipe app, "SmoothiePy", that allows users to add and view smoothie recipes.

#### User Story

- Users will be able to create their own smoothie recipes
- Users can generate a random recipe suggestion
- Users can view other user's recipes

#### Concepts I will use to meet project requirements:

- Object Oriented Python

  - Class for User, Recipe, and Ingredient; each with attributes

- Database Tables

  - user
    - id
    - user_name
    - email_add
  - recipe
    - id
    - recipe_name
    - ingredients
  - ingredient
    - id
    - ingredient_name
  - user_recipe
    - id
    - user_id
    - recipe_id
  - recipe_ingredient
    - id
    - recipe_id
    - ingredient_id
    - ingredient_quantity

- Object Relationships

  - Users can have many unique recipes // one to many - using 'user_recipe' join table
  - recipes will have many ingredients, while ingredients belong to many recipes // many to many
    - using recipe_ingredient join table

- Aggregate and Association Methods | CRUD
  - Create
    - create recipe
  - Read
    - read a recipe
    - view a random recipe
    - read all recipes by user
    - read all recipes including an ingredient
  - Update
    - change ingredient quantity in recipe
    - change recipe name
  - Delete
    - delete recipe
- Data Structures
  - List:
    - user has a list of recipe IDs
  - Dict:
    - recipe has a set of attribute and values
  - Tuple
    - persisted recipe return ingredients as tuple

#### What area I think will be most challenging:

- determining how to make each recipe unique. Can two recipes with all but one similar attribute, like the quantity of an ingredient, be easily determined unique? How do I write its validity test?
