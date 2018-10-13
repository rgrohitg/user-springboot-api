package com.rgrohitg.dao;

import com.rgrohitg.model.User;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;



@Repository
@Slf4j

public class UserDaoImpl implements UserDao{

    @PersistenceContext
    EntityManager manager;

    @Override
    public User getUser(Long id) {
            String sql = "FROM User WHERE id=:id";
            Query query = manager.createQuery(sql);
            query.setParameter("id", id);
            return (User) query.getSingleResult();
    }

    @Override
    public User insertUser(User user) {
        log.info("------Saving User----------");
        log.info(user.toString());
        manager.persist(user);
        manager.flush();
        return user;
    }
}
