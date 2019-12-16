package com.pockethome.login;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, Long>{
    User findById (long id);

<<<<<<< HEAD
public interface UserRepository extends JpaRepository<User, Long> {
    User findById (long id);
=======
>>>>>>> a6c00d8472227706e377564216f0c19b3b9a3aca
}