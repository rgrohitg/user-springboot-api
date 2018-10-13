package com.rgrohitg.dao;


import com.rgrohitg.model.User;


public interface UserDao {
    User getUser(Long id);
    User insertUser(User user);
}
