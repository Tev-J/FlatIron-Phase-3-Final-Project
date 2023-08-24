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

# Project Proposals

## Idea 1

### Main idea:

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

### Database Design

### Tables

#### user

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- username: STRING NOT NULL UNIQUE
- password: STRING NOT NULL
- email: STRING NOT NULL UNIQUE

#### recipe

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- name: STRING NOT NULL

#### ingredient

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- name: STRING NOT NULL UNIQUE

#### user recipes (join table)

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- user ID: INTEGER NOT NULL
- recipe ID: INTEGER NOT NULL

#### recipe ingredients (join table)

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- recipe id: INTEGER NOT NULL
- ingredient id: INTEGER NOT NULL
- ingredient quantity: INTEGER NOT NULL

## Idea 2

#### Main idea:

"Lets Learn Networking CLI"
A CLI app designed store, save, and access study flashcards, categorizing and retrieving them based on distinct subject names.

#### User Story

- Users will be able to create flashcards with networking questions, categorized by subject
- Users can view and save other flash cards by subject

#### Concepts I will use to meet project requirements:

- Object Oriented Python

  - Class for User, Flashcards with attributes

- Database Tables

  - user
    - id
    - user_name
    - email_address
  - flashcard
    - id
    - question
    - answer
    - subject
  - user_flashcard
    - id
    - user_id
    - flashcard_id
  - subject
    - id
    - subject_name
  - flashcard_subject
    - flashcard_id
    - subject_id

- Object Relationships

  - Users can have many flashcards, flashcards can be used by many users. // many to many
  - Flashcard can contain than one subjects. Subject likely have more than one flashcard // many to many

- Aggregate and Association Methods | CRUD
  - Create
    - create flashcard
  - Read
    - read a question
    - read an answer
    - read all flashcards by a user
    - read all flashcards by a subject
  - Update
    - display flashcard as studied/known/checked-off?
  - Delete
    - user should be able to delete own flashcard
- Data Structures
  - List:
    - list of flashcards for user by id
  - Dict:
    - flashcard has a set of attribute and values // question, answer, subject
  - Tuple
    - subjects for flashcards

#### What area I think will be most challenging:

- How can users delete their own flashcards while other users are allowed to read/interact with it?

### Database Design

### Tables

#### user

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- username: STRING NOT NULL UNIQUE
- password: STRING NOT NULL
- email: STRING NOT NULL UNIQUE

#### flashcard

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- subject name: STRING NOT NULL UNIQUE
- question: STRING NOT NULL
- answer: STRING NOT NULL

#### user_flashcard (join table)

- user ID: INTEGER NOT NULL
- flashcard ID: INTEGER NOT NULL
- learned/known/pass: INTEGER NOT NULL

#### subject

- id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
- subject name: INTEGER NOT NULL

#### flashcard_subject (join table)

- subject ID: INTEGER NOT NULL
- flahcard ID: INTEGER NOT NULL
