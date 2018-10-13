package com.rgrohitg.service;

import com.rgrohitg.dao.UserDao;
import com.rgrohitg.dto.UserDTO;
import com.rgrohitg.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class UserServiceImpl implements UserService {

    @Autowired
    UserDao dao;

    @Override
    public UserDTO getUser(Long id){

        return dao.getUser(id).toDto();
    }

    @Override
    public UserDTO insertUser(UserDTO dto) {
        User entity = new User();
        dao.insertUser(entity.fromDto(dto));
        return dto;
    }
}
