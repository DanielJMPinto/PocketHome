package com.PocketHome.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.PocketHome.model.Casa;

@Repository
public interface CasaRepository extends JpaRepository<Casa, Long>{

}
