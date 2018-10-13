package com.rgrohitg.controller;

import com.rgrohitg.dto.UserDTO;
import com.rgrohitg.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/")
public class UserController {


    @Autowired
    private UserService service;

    @ResponseBody
    @RequestMapping(value = "/user/{id}",method = RequestMethod.GET,produces = MediaType.APPLICATION_JSON_VALUE)
    public UserDTO getUser(@PathVariable Long id){
        return service.getUser(id);
    }

    @ResponseBody
    @RequestMapping(value = "/user",method = RequestMethod.PUT,produces = MediaType.APPLICATION_JSON_VALUE)
    public void insertUser(@RequestBody UserDTO body){
        service.insertUser(body);

    }
}