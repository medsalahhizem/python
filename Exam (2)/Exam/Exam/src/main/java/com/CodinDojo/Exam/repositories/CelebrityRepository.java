package com.CodinDojo.Exam.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.CodinDojo.Exam.models.Celebrity;

public interface CelebrityRepository extends CrudRepository <Celebrity, Long> {
	List<Celebrity> findAll();
}



