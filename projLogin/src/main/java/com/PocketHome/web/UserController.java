package com.PocketHome.web;

import com.PocketHome.model.User;
import com.PocketHome.service.SecurityService;
import com.PocketHome.service.UserService;
import com.PocketHome.validator.UserValidator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

@Controller
public class UserController {
    @Autowired
    private UserService userService;

    @Autowired
    private SecurityService securityService;

    @Autowired
    private UserValidator userValidator;

    @GetMapping("/register")
    public String registration(Model model) {
        model.addAttribute("userForm", new User());

        return "register";
    }

    @PostMapping("/register")
    public String registration(@ModelAttribute("userForm") User userForm, BindingResult bindingResult) {
        System.out.println("OLA-1");
        userValidator.validate(userForm, bindingResult);
        System.out.println("OLA0");
        if (bindingResult.hasErrors()) {
            return "register";
        }
        System.out.println("OLA1");
        userService.save(userForm);
        System.out.println("OLA2");
        securityService.autoLogin(userForm.getUsername(), userForm.getPassword());

        return "redirect:/index";
    }

    @GetMapping("/login")
    public String login(Model model, String error, String logout) {
        if (error != null)
            model.addAttribute("error", "Your username and password is invalid.");

        if (logout != null)
            model.addAttribute("message", "You have been logged out successfully.");

        return "login";
    }

    @GetMapping({"/", "/index"})
    public String welcome(Model model) {
        return "index";
    }
}
