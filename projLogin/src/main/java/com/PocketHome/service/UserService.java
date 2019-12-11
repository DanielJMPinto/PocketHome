package com.PocketHome.service;

import com.PocketHome.model.User;
import org.springframework.stereotype.Service;

@Service
public interface UserService {
    void save(User user);

    User findByEmail(String email);
}
