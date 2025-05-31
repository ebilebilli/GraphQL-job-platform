# GraphQL Job Platform

<div align="center">
  <img src="https://graphql.org/img/logo.svg" alt="GraphQL Logo" width="200"/>
</div>

> **Note**: This project uses GraphQL, which is considered a legacy technology. While it's still widely used and valuable to learn, it's important to be aware that newer alternatives exist in the API development landscape.

This is a learning project, so the code and structure may evolve as I learn more about GraphQL and its ecosystem. Feel free to explore the codebase and learn along with me

## 🎯 Learning Objectives

- Understanding GraphQL fundamentals and its advantages over REST
- Implementing GraphQL schemas and types
- Working with GraphQL queries and mutations
- Handling authentication and authorization in GraphQL
- Managing relationships between different data types
- Implementing real-time features using GraphQL subscriptions
- Best practices for GraphQL API design

## 🚀 Project Structure

The project follows Django's project structure with GraphQL integration:

```
job_platform/
├── jobs/              # Job-related models and GraphQL types
├── users/             # User authentication and management
├── graphql_api/       # GraphQL schema and resolvers
├── utils/            # Utility functions and helpers
└── job_platform/     # Main project settings
```

## 🛠️ Technologies Used

### Backend
- Python 3.13
- Django 5.2.1
- GraphQL (via graphene-django 3.2.3)
- JWT Authentication (django-graphql-jwt 0.4.0)
- SQLite Database

### Key Dependencies
- graphene==3.4.3
- graphene-django==3.2.3
- django-graphql-jwt==0.4.0
- PyJWT==2.10.1

## 📚 Learning Resources

While building this project, I'm following these resources:
- [GraphQL Official Documentation](https://graphql.org/learn/)
- [Graphene-Django Documentation](https://docs.graphene-python.org/projects/django/en/latest/)
- [Django Documentation](https://docs.djangoproject.com/)

## 🎓 Project Goals

This project serves as a practical learning ground for:
1. Understanding GraphQL's declarative data fetching
2. Implementing efficient data loading patterns
3. Building a scalable API architecture
4. Learning GraphQL security best practices
5. Understanding the relationship between GraphQL and databases

## 📝 Notes

