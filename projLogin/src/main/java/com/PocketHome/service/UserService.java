package com.PocketHome.service;

import com.PocketHome.model.User;

public interface UserService {
    void save(User user);

    User findByUsername(String username);
}
