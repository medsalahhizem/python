package com.CodinDojo.Exam.controllers;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.CodinDojo.Exam.models.Celebrity;
import com.CodinDojo.Exam.models.LoginUser;
import com.CodinDojo.Exam.models.User;
import com.CodinDojo.Exam.services.CelebrityService;
import com.CodinDojo.Exam.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;



@Controller
public class MainController {

  @Autowired
  private UserService userServ;
  
	@Autowired
	private CelebrityService celebrities;
 
 @GetMapping("/")
 public String index(Model model) {
 
     model.addAttribute("newUser", new User());
     model.addAttribute("newLogin", new LoginUser());
     return "index.jsp";
 }
 
 @PostMapping("/register")
 public String register(@Valid @ModelAttribute("newUser") User newUser, 
         BindingResult result, Model model, HttpSession session) {
     
     userServ.register(newUser, result);
     
     if(result.hasErrors()) {
         // Be sure to send in the empty LoginUser before 
         // re-rendering the page.
         model.addAttribute("newLogin", new LoginUser());
         return "index.jsp";
     }
     
     session.setAttribute("userId", newUser.getId());
 
     return "redirect:/welcome";
 }
 
 @PostMapping("/login")
 public String login(@Valid @ModelAttribute("newLogin") LoginUser newLogin, 
         BindingResult result, Model model, HttpSession session) {
     
     // Add once service is implemented:
     User user = userServ.login(newLogin, result);
 
     if(result.hasErrors()) {
         model.addAttribute("newUser", new User());
         return "index.jsp";
     }
 
     session.setAttribute("userId", user.getId());
 
     return "redirect:/welcome";
 }
 
 @GetMapping("/logout")
 public String logout(HttpSession session) {
	 session.setAttribute("userId", null);
	 return "redirect:/";
 }
 
 @GetMapping("/welcome")
 public String welcome(Model model, HttpSession session) {
	 Long userId = (Long) session.getAttribute("userId");
	 if(userId==null) {
		 return "redirect:/";
	 }
	 User user = userServ.findById(userId);
	 model.addAttribute("user",user);	 
	 model.addAttribute("celebrities",celebrities.all());
 
	 return "dashboard.jsp";
 }
 
 
 
 @GetMapping("/add")
 public String addPage(@ModelAttribute("celebrity")  Celebrity  celebrity, Model model, HttpSession session) {
 	
 	User user = userServ.findById((Long)session.getAttribute("userId"));
 	model.addAttribute("user", user);
 	
 	return "add.jsp";
 }
 
 
 @PostMapping("/celebrities")
 public String createBook(@Valid @ModelAttribute("celebrity") Celebrity celebrity, BindingResult result) {

 	if (result.hasErrors()) {
 		return "add.jsp";
 	}
 	
 	celebrities.create(celebrity);
 	
 	return "redirect:/welcome";
 }
 
 
 @GetMapping("/celebrity/{id}")
 public String showPage(Model model, @PathVariable("id") Long id, HttpSession session) {
 	if(session.getAttribute("userId") == null) {
 		return "redirect:/";
 	}
 	Celebrity celebrity = celebrities.findById(id);
 	model.addAttribute("celebrity", celebrity);
 	model.addAttribute("user",  userServ.findById((Long)session.getAttribute("userId")));
 	
 	return "show.jsp";
 }
 

 
 
 @GetMapping("/celebrity/{id}/edit")
 public String editPage(Model model, @PathVariable("id") Long id, HttpSession session) {
 	if(session.getAttribute("userId") == null) {
 		return "redirect:/";
 	}
 	Celebrity celebrity = celebrities.findById(id);
 	model.addAttribute("celebrity", celebrity);
 	model.addAttribute("user",  userServ.findById((Long)session.getAttribute("userId")));
 	
 	return "update.jsp";
 }
 
 

 @PutMapping("/celebrities/{id}")
 public String update(@Valid @ModelAttribute("celebrity") Celebrity celebrity, 
                     BindingResult result, 
                     @PathVariable("id") Long id,
                     HttpSession session) {
     if (result.hasErrors()) {
         return "update.jsp";
     }
     Long userId = (Long) session.getAttribute("userId");
     if (celebrities.validateOwner(id, userId)) {
         celebrities.update(celebrity);
     }
     return "redirect:/celebrity/" + id ;
 }
 
 
 
 @DeleteMapping("/celebrities/{id}/delete")
 public String delete(@PathVariable("id") Long id, HttpSession session) {
     Long userId = (Long) session.getAttribute("userId");
     if (userId != null && celebrities.validateOwner(id, userId)) {
         celebrities.delete(id);
     }
  	return "redirect:/welcome";
 }
 
 
}

