package com.rgrohitg.service;

import com.rgrohitg.dto.UserDTO;

public interface UserService {
    UserDTO getUser(Long id);
    UserDTO insertUser(UserDTO dto);
}
