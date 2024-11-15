<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="ISO-8859-1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Fan Pages</title>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Home</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="/logout">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->

    <div class="container d-flex justify-content-center align-items-center flex-column vh-100">
    <div class="card text-center w-50">
        <div class="card-body">
            <h1 class="card-title">Welcome, <c:out value="${user.username}"/>!</h1>
            <a href="/add" class="btn btn-primary btn-lg mb-4">Add Celebrity Page</a>
            
            <!-- List of Celebrities -->
            <div class="mt-3">               
                <div class="list-group">
                    <c:forEach var="celebrity" items="${celebrities}">
                        <div class="list-group-item text-start">
                            <!-- Celebrity Name as a Link -->
                            <h4>
                                <a href="/celebrity/${celebrity.id}" class="text-decoration-none">
                                    <c:out value="${celebrity.name}" />
                                </a>
                            </h4>
                            <!-- Page Manager -->
                            <p class="text-muted mb-0">Page Manager: 
                                <c:out value="${celebrity.user.username}" />
                            </p>
                        </div>
                    </c:forEach>
                </div>
            </div>
        </div>
    </div>
</div>
    
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>