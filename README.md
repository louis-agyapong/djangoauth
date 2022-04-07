# Django authentication and authorization playground

1. Authentication: Determining the identity of a user, server or client
2. Authorization: Determines what resources a user can access

## User Objects

User objects core to Django Authentication System

1. Superusers: is_superuser, is_staff and is_active
2. Staff: is_active and is_staff
3. User: is_active

## Common Authorization Methodologies

1. Role-based acces controls (RBAC)
2. Attribute-based access control (ABAC)

## Permissions (Authorization)

1. Django comes with a built-in permissions or authorization system (Django admin site).
2. This allows you to manage access to the database models
3. By default anytime we create a new model, Django creates four different permissions

### Django Creates Four Default Permissions When a new Model is created

1. Add
2. Change
3. Delete
4. View

This is created for each Django model
