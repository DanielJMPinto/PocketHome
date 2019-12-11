package com.PocketHome.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.PocketHome.model.Divisao;

@Repository
public interface DivisaoRepository extends JpaRepository<Divisao, Long>{

}
