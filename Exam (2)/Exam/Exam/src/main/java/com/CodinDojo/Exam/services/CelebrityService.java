package com.CodinDojo.Exam.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.CodinDojo.Exam.models.Celebrity;
import com.CodinDojo.Exam.repositories.CelebrityRepository;

@Service
public class CelebrityService {

    @Autowired
    private CelebrityRepository repo;

    // Find a celebrity by ID
    public Celebrity findById(Long id) {
        Optional<Celebrity> result = repo.findById(id);
        if (result.isPresent()) {
            return result.get();
        }
        return null;
    }

    // Find all celebrities
    public List<Celebrity> all() {
        return repo.findAll();
    }

    // Create a new celebrity
    public Celebrity create(Celebrity celebrity) {
        return repo.save(celebrity);
    }

    // Update an existing celebrity
    public Celebrity update(Celebrity celebrity) {
        // Verify the celebrity exists before updating
        Celebrity existingCelebrity = findById(celebrity.getId());
        if (existingCelebrity != null) {
            return repo.save(celebrity);
        }
        return null;
    }

    // Delete a celebrity
    public void delete(Long id) {
        // Verify the celebrity exists before deleting
        Celebrity existingCelebrity = findById(id);
        if (existingCelebrity != null) {
            repo.deleteById(id);
        }
    }

    // Validate ownership of the celebrity
    public boolean validateOwner(Long celebrityId, Long userId) {
        Celebrity celebrity = findById(celebrityId);
        if (celebrity != null) {
            return celebrity.getUser().getId().equals(userId);
        }
        return false;
    }
}
