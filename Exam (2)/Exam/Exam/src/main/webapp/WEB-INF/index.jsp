<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="ISO-8859-1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Fan Pages</title>
</head>
<body class="bg-light">
<div class="container mt-5">
    <h1 class="text-center mb-4">Welcome to Fan pages!</h1>
    
    <div class="row justify-content-center">
        <!-- Registration Form -->
        <div class="col-md-5 mb-4">
            <div class="card shadow">
                <div class="card-header bg-primary text-white">
                    <h4 class="mb-0">Register</h4>
                </div>
                <div class="card-body">
                    <form:form action="/register" method="post" modelAttribute="newUser">
                        <div class="mb-3">
                            <label for="username" class="form-label">Username:</label>
                            <form:input path="username" class="form-control"/>
                            <form:errors path="username" class="text-danger"/>
                        </div>
                        
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <form:input path="email" class="form-control"/>
                            <form:errors path="email" class="text-danger"/>
                        </div>
                        
                        <div class="mb-3">
                            <label for="password" class="form-label">Password:</label>
                            <form:input path="password" type="password" class="form-control"/>
                            <form:errors path="password" class="text-danger"/>
                        </div>
                        
                        <div class="mb-3">
                            <label for="confirm" class="form-label">Confirm Password:</label>
                            <form:input path="confirm" type="password" class="form-control"/>
                            <form:errors path="confirm" class="text-danger"/>
                        </div>
                        
                        <button type="submit" class="btn btn-primary w-100">Register</button>
                    </form:form>
                </div>
            </div>
        </div>

        <!-- Login Form -->
        <div class="col-md-5 mb-4">
            <div class="card shadow">
                <div class="card-header bg-success text-white">
                    <h4 class="mb-0">Login</h4>
                </div>
                <div class="card-body">
                    <form:form action="/login" method="post" modelAttribute="newLogin">
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <form:input path="email" class="form-control"/>
                            <form:errors path="email" class="text-danger"/>
                        </div>
                        
                        <div class="mb-3">
                            <label for="password" class="form-label">Password:</label>
                            <form:input path="password" type="password" class="form-control"/>
                            <form:errors path="password" class="text-danger"/>
                        </div>
                        
                        <button type="submit" class="btn btn-success w-100">Login</button>
                    </form:form>
                </div>
            </div>
        </div>
    </div>
</div>


    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>