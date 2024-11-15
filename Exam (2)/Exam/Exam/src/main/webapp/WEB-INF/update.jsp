<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>   
<%@ page isErrorPage="true" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"  %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Update Celebrity</title>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/welcome">Home</a>    
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

    <!-- Update Celebrity Form -->
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-body">
                        <h1 class="card-title text-center">Edit Celebrity Page</h1>
                     
                        <form:form action="/celebrities/${celebrity.id}" modelAttribute="celebrity" method="post">
                            <input type="hidden" name="_method" value="put">
                            <form:input type="hidden" path="user" value="${userId}"/>
        
                        
                            
                            <div class="mb-3">
                                <form:label path="name" for="name" class="form-label">Name</form:label>
                                <form:input path="name" id="name" class="form-control" placeholder="Enter celebrity's name" />
                                <form:errors path="name" cssClass="text-danger" />
                            </div>
                        
                           
                            <div class="mb-3">
                                <form:label path="details" for="details" class="form-label">Details</form:label>
                                <form:textarea path="details" id="details" class="form-control" rows="4" placeholder="Enter celebrity details" />
                                <form:errors path="details" cssClass="text-danger"/>
                            </div>
                        
                          
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg">Update</button>
                            </div>
			              <div class="d-flex gap-3">						
						   <form action="/celebrities/${celebrity.id}/delete" method="post">
							    <input type="hidden" name="_method" value="DELETE">
							    <input type="submit" value="Delete" class="btn btn-danger">
							</form>
			              </div>
                        </form:form>
                    </div>
                </div>
            </div>
        </div>
    </div>


  
</body>
</html>
