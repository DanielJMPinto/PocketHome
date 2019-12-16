
package ua.rfo.ies.PocketHomeRest;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HomeController {
    @GetMapping({"/", "/index"})
    public String hello(Model model) {
        model.addAttribute("index", index);
        return "index";
    }
}